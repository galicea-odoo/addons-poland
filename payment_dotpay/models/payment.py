# -*- coding: utf-8 -*-
# 
import hashlib
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


"""
Podstawowe:
api_version=dev
id=123456 (ID sklepu sprzedawcy)
amount = kwotę transakcji (np. amount=12.42)
currency = waluta transakcji (np. currency=PLN)
description = opis transakcji (np. description=Zapłata za fakturę VAT 12345/2014)
lang=pl



Opcje:
URLC - Adres internetowy (HTTP lub HTTPS) do odbioru parametrów potwierdzających realizację lub odmowę operacji (transakcji).
zob str. 12/13 dokumentacji

control - Parametr w formie niezmienionej jest odsyłany do serwisu sprzedawcy w powiadomieniu URLC.
Przykład: control=ec4bf09d3dbe0cb71e6abc3ea44a7273


URL - Adres internetowy (HTTP lub HTTPS) na jaki ma powrócić kupujący po dokonaniu płatności. 
Sterowanie zachowaniem parametru URL określa parametr type.
Przykład:
URL=https://www.example.com/thanks_page.php

type:
0 – Po dokonaniu płatności Kupującemu zostanie udostępniony przycisk powrotu do serwisu sprzedawcy,
2 – Brak reakcji, nic nie jest wysyłane, brak przycisku (wartość domyślna).
4 – Nastąpi bezpośrednie przekierowanie do dostawcy kanału płatności (np. Banku),

Dla 4 trzeba dane zdefiniować channel:

channel
ch_lock
channel_groups

Inne:
ignore_last_pay
buttontext - wyświetlona na przycisku powrotu do serwisu sprzedawcy.
bylaw - Parametr informujący o zaakceptowaniu przez Klienta regulaminu płatności oraz polityki cookies Dotpay S.A..
personal_data - Parametr informujący o wyrażeniu przez Klienta zgody na przetwarzanie danych osobowych przez Dotpay S.A..
....

chk - Suma kontrolna służąca do weryfikacji poprawności przesłanych danych.

suma=PIN + api_version + charset + lang + id + pid + amount + currency + description +
control + channel + credit_card_brand + ch_lock + channel_groups + onlinetransfer +
url + type + buttontext + urlc + firstname + lastname + email + street + street_n1 +
street_n2 + state + addr3 + city + postcode + phone + country + code + p_info +
p_email + n_email + expiration_date + deladdr + recipient_account_number +
recipient_company + recipient_first_name + recipient_last_name +
recipient_address_street + recipient_address_building + recipient_address_apartment +
recipient_address_postcode + recipient_address_city + application +
application_version + warranty + bylaw + personal_data + credit_card_number +
credit_card_expiration_date_year + credit_card_expiration_date_month +
credit_card_security_code + credit_card_store + credit_card_store_security_code +
credit_card_customer_id + credit_card_id + blik_code + credit_card_registration +
recurring_frequency + recurring_interval + recurring_start + recurring_count +
surcharge_amount + surcharge + ignore_last_payment_channel + id1 + amount1 +
currency1 + description1 + control1 + ... + id(n) + amount(n) + currency(n) +
description(n) + control(n)

chk=SHA-256(suma)

"""


class PaymentAcquirerDotpay(models.Model):
    _inherit = 'payment.acquirer'

    test = True
    test_pos_id = 123456

    provider = fields.Selection(selection_add=[('dotpay', 'Dotpay')])

    dotpay_pos_id = fields.Char(string='dotpay_pos_id', required_if_provider='dotpay', groups='base.group_user')
    dotpay_pin = fields.Char(string='dotpay_pin', required_if_provider='dotpay', groups='base.group_user')
    dotpay_urlc = fields.Char(string='dotpay_urlc', required_if_provider='dotpay', groups='base.group_user')
    dotpay_url = fields.Char(string='dotpay_url', required_if_provider='dotpay', groups='base.group_user')

    def compute_chk(self,params):

        def v(par):
            try:
                return str(params[par])
            except:
                return ''

        DotpayPin=self.dotpay_pin
        chk = DotpayPin+ \
         v('api_version')+ \
         v('charset')+ \
         v('lang')+ \
         v('id')+ \
         v('pid')+ \
         v('amount')+ \
         v('currency')+ \
         v('description')+ \
         v('control')+ \
         v('channel')+ \
         v('credit_card_brand')+ \
         v('ch_lock')+ \
         v('channel_groups')+ \
         v('onlinetransfer')+ \
         v('url')+ \
         v('type')+ \
         v('buttontext')+ \
         v('urlc')+ \
         v('firstname')+ \
         v('lastname')+ \
         v('email')+ \
         v('street')+ \
         v('street_n1')+ \
         v('street_n2')+ \
         v('state')+ \
         v('addr3')+ \
         v('city')+ \
         v('postcode')+ \
         v('phone')+ \
         v('country')+ \
         v('code')+ \
         v('p_info')+ \
         v('p_email')+ \
         v('n_email')+ \
         v('expiration_date')+ \
         v('deladdr')+ \
         v('recipient_account_number')+ \
         v('recipient_company')+ \
         v('recipient_first_name')+ \
         v('recipient_last_name')+ \
         v('recipient_address_street')+ \
         v('recipient_address_building')+ \
         v('recipient_address_apartment')+ \
         v('recipient_address_postcode')+ \
         v('recipient_address_city')+ \
         v('application')+ \
         v('application_version')+ \
         v('warranty')+ \
         v('bylaw')+ \
         v('personal_data')+ \
         v('credit_card_number')+ \
         v('credit_card_expiration_date_year')+ \
         v('credit_card_expiration_date_month')+ \
         v('credit_card_security_code')+ \
         v('credit_card_store')+ \
         v('credit_card_store_security_code')+ \
         v('credit_card_customer_id')+ \
         v('credit_card_id')+ \
         v('blik_code')+ \
         v('credit_card_registration')+ \
         v('recurring_frequency')+ \
         v('recurring_interval')+ \
         v('recurring_start')+ \
         v('recurring_count')+ \
         v('surcharge_amount')+ \
         v('surcharge')+ \
         v('ignore_last_payment_channel')        # pominieto MultiMerchantList
        #3deab373c427df84e53bbee01dff220539553056d8456108ff3c7234
        # but expected Chk "4a33e6f894476a462fd9f70f91a1dbfce58b0db2d89b1b5eeacc89d9c578b206"
        return hashlib.sha256(chk).hexdigest()


    @api.multi
    def dotpay_form_generate_values(self, values):
        self.ensure_one()
        base_url = self.env['ir.config_parameter'].get_param('web.base.url')
        self.test = False
        dotpay_values = dict()

        if self.test:
            dotpay_values['api_version'] = 'dev'
            dotpay_values["id"] = "123456"
            dotpay_values["amount"] = "320.00"
            dotpay_values["currency"] = "PLN"
            dotpay_values["description"] = "Płatność za 12345/2014"
            dotpay_values["control"] = "202cb962ac590"
#            dotpay_values["channel"] = "248"
#            dotpay_values["ch_lock"] = "1"
            dotpay_values["firstname"] = "John"
            dotpay_values["lastname"] = "Smith"
            dotpay_values["email"] = "john.smith@example.com"
            dotpay_values["type"] = "0"
            dotpay_values["url"] = "https://www.example.com/thanks_page.php"
            dotpay_values["urlc"] = "https://www.example.com/urlc_receiver.php"
#            dotpay_values["credit_card_store"] = "1"
#            dotpay_values["credit_card_customer_id"] = "f9c6a4-25473"
            dotpay_values["chk"] = self.compute_chk(dotpay_values)
                # ma być: "11ac1938ac47ddd53815b4aeb6230ab9fe4554d82ee11e39c41b9055f38f5c08"
        else:
            partner=values['billing_partner']
            partner_id = partner.id if partner else 0
            reference=values['reference'] # niestety reference wywoływany z renderowania buttona płatności
                                          # zawiera zawsze '/' - zob website_sale.controllers.main.WebsiteSale
            if reference=='/':
                control=partner_id
            else:
                control=reference  # w module vt w miejsce / wstawia payment_tx_id
                                   # brzydkie obejscie problemu  po modyfikacji mogę dostać id z order
                reference=values.get('partner_email') # nie może być puste
            dotpay_values['api_version'] = 'dev'
            dotpay_values['id'] = self.dotpay_pos_id
            dotpay_values['amount']=values['amount']
            dotpay_values['currency']='PLN'
            dotpay_values["chk"] = self.compute_chk(dotpay_values)
            dotpay_values['description'] = reference
            dotpay_values['control'] = control
            dotpay_values['firstname'] = values.get('partner_name')
            dotpay_values['lastname'] = values.get('partner_last_name')
            dotpay_values['email'] = values.get('partner_email')
            dotpay_values['type'] = '0'
            dotpay_values['url'] = self.dotpay_url if self.dotpay_url else base_url+'/payment/dotpay/return'
            dotpay_values['urlc'] = self.dotpay_urlc if self.dotpay_urlc else base_url+'/payment/dotpay/result'
# urlc      : id=346801&operation_number=M6856-9235&operation_type=payment&operation_status=completed&operation_am...
#           dotpay_values['buttontext'] = 'wróć do transmem'
# + channel + credit_card_brand + ch_lock + channel_groups + onlinetransfer +
# street + street_n1 +
#street_n2 + state + addr3 + city + postcode + phone + country + code + p_info +
#p_email + n_email + expiration_date + deladdr + recipient_account_number +
#recipient_company + recipient_first_name + recipient_last_name +
#recipient_address_street + recipient_address_building + recipient_address_apartment +
#recipient_address_postcode + recipient_address_city + application +
#application_version + warranty + bylaw + personal_data + credit_card_number +
#credit_card_expiration_date_year + credit_card_expiration_date_month +
#credit_card_security_code + credit_card_store + credit_card_store_security_code +
#credit_card_customer_id + credit_card_id + blik_code + credit_card_registration +
#recurring_frequency + recurring_interval + recurring_start + recurring_count +
#surcharge_amount + surcharge + ignore_last_payment_channel + id1 + amount1 +
#currency1 + description1 + control1 + ... + id(n) + amount(n) + currency(n) +
#description(n) + control(n)
            dotpay_values['chk'] = self.compute_chk(dotpay_values)

        return dotpay_values

    # obowiązkowa funkcja wywoływana przez paynent_acquirer zaraz po dotpay_form_generate_values
    # nazwa: _get_<provider>_get_form_action_url
    # zwraca url providera - wywoływany jako akcja formularza
    # wywolywany też przed wywołaniem providera
    @api.multi
    def dotpay_get_form_action_url(self):
        self.ensure_one()
        self.test=True
        if self.test:
            return 'https://ssl.dotpay.pl/t2/'
        else:
            return 'https://ssl.dotpay.pl/t2/'




class PaymentTransactionDotpay(models.Model):
    _inherit = 'payment.transaction'


   # wywołania z addons/payment/models/payment_acquirer.py ->   form_feedback
   # '_%s_form_get_tx_from_data' % acquirer_name
   # '_%s_form_get_invalid_parameters' % acquirer_name
   # '_%s_form_validate' % acquirer_name

   # id = 346801 & operation_number = M6856 - 9235 & operation_type = payment & operation_status = completed & operation_am

    @api.model
    def _dotpay_form_get_tx_from_data(self, data):
        status = data.get('operation_status')
        control=data.get('control')
        try:
            partner_id=int(control)
        except:
            partner_id=0
        if partner_id>0:
            transaction = self.search([('partner_id', '=', partner_id),('state','=','draft')])
        else:
            transaction = self.search([('reference', '=', control)])
        if not transaction:
#            error_msg = (_('Dotpay: received data for reference %s no order found') % (partner_id))
            return self #raise ValidationError(error_msg)
        elif len(transaction) > 1:
#            error_msg = (_('Dotpay: received data for reference %s multiple orders found') % (partner_id))
            return self #raise ValidationError(error_msg)
        return transaction

    @api.multi
    def _dotpay_form_get_invalid_parameters(self, data):
        invalid_parameters = []
        return invalid_parameters

    @api.multi
    def _dotpay_form_validate(self, data):
        status = data.get('operation_status')
        transaction_status = {
            'completed': {
                'state': 'done',
            },
            'pending': {
                'state': 'pending',
            },
            'failure': {
                'state': 'cancel',
            },
            'error': {
                'state': 'error',
            }
        }
        vals = transaction_status.get(status, False)
        if not vals:
            vals = transaction_status['error']
            _logger.info('_dotpay_form_validate error')
        if self:
            return self.write(vals)
        else:
            return None
