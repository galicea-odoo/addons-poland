# -*- coding: utf-8 -*-

import logging
import pprint
import werkzeug

from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)


class DotpayController(http.Controller):

    @http.route(['/payment/dotpay/result', ], type='http', auth='public', csrf=False)
    def dotpay_urlc(self, **post):
        _logger.info('Dotpay RESULT  %s', pprint.pformat(post))
        if post:
            request.env['payment.transaction'].sudo().form_feedback(post, 'dotpay')
        return werkzeug.wrappers.Response(status=200)

    @http.route(['/payment/dotpay/return', ], type='http', auth="public", website=True, csrf=False)
    def payu_return(self, **post):
        _logger.info('Dotpay RETURN  %s', pprint.pformat(post))
        if post.get('status')=='OK':
            msg=u'Dziękujemy za dokonanie wpłaty'
        else:
            msg=u'Oczekujemy na potwierdzenie wykonania wpłaty'
        return request.render(
            "payment_dotpay.payment_return_dotpay",
            {
              'message': msg,
            }
        )
