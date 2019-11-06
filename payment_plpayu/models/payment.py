# -*- coding: utf-8 -*-
#
# http://developers.payu.com/pl/restapi.html#references_form_parameters
#
import hashlib
try:
  from urllib.parse import quote_plus
except:
  from urllib import quote_plus
import time
try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse

from odoo import api, fields, models, _
from odoo.addons.payment.models.payment_acquirer import ValidationError
from odoo.tools.float_utils import float_compare

import logging

_logger = logging.getLogger(__name__)


class PaymentAcquirerPlPayu(models.Model):
    _inherit = 'payment.acquirer'

    test = False
    test_local = False
    sig_src = False


    provider = fields.Selection(selection_add=[('plpayu', 'PlPayu')])
    plpayu_pos_id = fields.Char(string='plpayu_pos_id', required_if_provider='plpayu', groups='base.group_user')
    plpayu_pos_auth_key = fields.Char(string='plpayu_pos_auth_key', required_if_provider='plpayu', groups='base.group_user')
    plpayu_key_md5 = fields.Char(string='plpayu_key_md5', required_if_provider='plpayu', groups='base.group_user')
    plpayu_key2_md5 = fields.Char(string='plpayu_key2_md5', required_if_provider='plpayu', groups='base.group_user')
    host_ip = fields.Char(string='host_ip', required_if_provider='plpayu', groups='base.group_user')

    test_pos_id = 123456
    test_pos_auth_key = 'AaBbCcD'
    test_payu_md5_key = '098f6bcd4621d373cade4e832627b4f6' 

    def _get_plpayu_urls(self, environment):
        """ PlPayu URLs"""
        if self.test_local:
            return {'plpayu_form_url': 'http://localhost/test.php'}
        elif environment == 'prod':
            return {'plpayu_form_url': 'https://secure.payu.com/paygw/UTF/NewPayment'}
        elif environment =='state':
            return {'plpayu_form_url': 'https://secure.payu.com/paygw/UTF/Payment/get'}
        else:
            return {'plpayu_form_url': 'https://secure.payu.com/paygw/UTF/NewPayment'}

    def _plpayu_generate_sign(self, inout, values):
        """http://developers.payu.com/pl/classic_api.html#classic_api_signing_parameters
1. Posortuj wszystkie pola formularza alfabetycznie według nazw parametrów (atrybut name elementu input) w porządku rosnącym. 
   Jeżeli dana wartość nie jest przekazywana w formularzu tworzącym nową płatność używamy pustego ciągu znaków.
2. Dokonaj konkatenacji kluczy i wartości wszystkich pól formularza zgodnie z wcześniej wyznaczonym porządkiem (klucz=wartość), rozdzielając je znakiem ampersand &. 
   Wartości parametrów muszą być poddane kodowaniu URL (URL encoding, application/x-www-form-urlencoded, znak spacji zamieniany na '+') 
   przy użyciu odpowiedniego kodowania strony.
3. Do tak powstałego ciągu znaków dodaj swój klucz prywatny (widoczny w Panelu Managera jako Drugi klucz (MD5)).
4. Użyj funkcji skrótu SHA-256.
        """
        content=u''
        if self.test:
          payu_md5_key = self.test_payu_md5_key 
          for name in ('amount','client_ip','desc','email','first_name','js',
                     'last_name','pos_auth_key','pos_id',
                     'session_id', 'ts'):
            if values[name]:
              content=content + name + '=' + quote_plus(str(values[name]))+ '&'
        else:
          payu_md5_key = self.plpayu_key_md5
          for name in ('amount','client_ip','desc','email','first_name','js',
                     'last_name', 'pos_auth_key','pos_id',
                     'session_id','ts'):
#          for name in sorted(values):
            if values[name]:
              content=content + name + '=' + quote_plus(str(values[name]))+ '&'
        content = content + payu_md5_key
        if self.sig_src: # or/and  self.test
          sig = content
        else:
          sig = hashlib.sha256(content).hexdigest()
        return sig

    @api.multi
    def plpayu_form_generate_values(self, values):
        self.ensure_one()
        base_url = self.env['ir.config_parameter'].get_param('web.base.url')
        plpayu_values = dict()
#           amount=int(100*float(values['amount'])), )

# test http://developers.payu.com/pl/classic_api.html

        if self.test:
          plpayu_values["first_name"] = ""
          plpayu_values["last_name"] = ""
          plpayu_values["email"] = ""
          plpayu_values["pos_id"] = self.test_pos_id
          plpayu_values["pos_auth_key"] = self.test_pos_auth_key
          plpayu_values["amount"] = "1000"
          plpayu_values["desc"] = "Opis płatności"
          plpayu_values["client_ip"] = "123.123.123.123"
          plpayu_values["js"] = "0"
          plpayu_values["ts"] = "124321878"
# sig ma byc 2d373a18641fbd6bcea6c86ec2c0554fa28eed244a2649bb638ee600a66100d2
        else:
#          plpayu_values['city'] = 'Jaroslaw' # 
          plpayu_values['amount']=int(100*float(values['amount']))
          plpayu_values['client_ip'] = self.host_ip 
#          plpayu_values['country'] = 'PL' # opcja
          plpayu_values['desc'] = values['reference']
          plpayu_values['email'] = values.get('partner_email')
          plpayu_values['first_name'] = values.get('partner_name'),
          plpayu_values['js'] = "1"  # opcja
#          plpayu_values['language'] = 'pl' # opcja
          plpayu_values['last_name'] = values.get('partner_last_name')
#          plpayu_values["phone"] = values.get('partner_phone') # opcja
          plpayu_values['pos_auth_key'] = self.plpayu_pos_auth_key # z parametrow nadanych przez PayU
          plpayu_values['pos_id'] = self.plpayu_pos_id  # z parametrow nadanych przez PayU
#          plpayu_values['post_code'] = '37-500' # opcja
          plpayu_values['session_id'] = int(time.time()) # values['reference']
#          plpayu_values['street'] = '' # opcja
          plpayu_values['ts'] = int(time.time()) # znacznik czasu

        plpayu_values['sig'] = self._plpayu_generate_sign('in', plpayu_values)
        return plpayu_values

    @api.multi
    def plpayu_get_form_action_url(self):
        self.ensure_one()
        return self._get_plpayu_urls(self.environment)['plpayu_form_url']


class PaymentTransactionPlPayu(models.Model):
    _inherit = 'payment.transaction'

    @api.model
    def _plpayu_form_get_tx_from_data(self, data):
        """ Given a data dict coming from plpayu, verify it and find the related  transaction record. """
        reference = data.get('session_id')

        transaction = self.search([('reference', '=', reference)])

        if not transaction:
            error_msg = (_('PlPayu: received data for reference %s; no order found') % (reference))
            raise ValidationError(error_msg)
        elif len(transaction) > 1:
            error_msg = (_('PlPayu: received data for reference %s; multiple orders found') % (reference))
            raise ValidationError(error_msg)
        return transaction

    @api.multi
    def _plpayu_form_get_invalid_parameters(self, data):
        invalid_parameters = []
        return invalid_parameters

    @api.multi
    def _plpayu_form_validate(self, data):
        status = data.get('status')
        transaction_status = {
            'COMPLETED': {
                'state': 'done',
#                'acquirer_reference': data.get('PlPayuId'),
                'date_validate': fields.Datetime.now(),
            },
            'PENDING': {
                'state': 'pending',
#                'acquirer_reference': data.get('PlPayuId'),
                'date_validate': fields.Datetime.now(),
            },
            'WAITING_FOR_CONFIRMATION': {
                'state': 'pending',
#                'acquirer_reference': data.get('PlPayuId'),
                'date_validate': fields.Datetime.now(),
            },
            'CANCELED': {
                'state': 'cancel',
#                'acquirer_reference': data.get('PlPayuId'),
                'date_validate': fields.Datetime.now(),
            },
            'REJECTED': {
                'state': 'error',
                'state_message': data.get('error_Message') or _('PlPayu: feedback error'),
#                'acquirer_reference': data.get('PlPayuId'),
                'date_validate': fields.Datetime.now(),
            }
        }
        vals = transaction_status.get(status, False)
        if not vals:
            vals = transaction_status['error']
            _logger.info(vals['state_message'])
        return self.write(vals)
