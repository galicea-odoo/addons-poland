# -*- coding: utf-8 -*-
#

import logging
import pprint
import werkzeug

from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)


class PlPayuController(http.Controller):
    @http.route(['/payment/plpayu/return', ], type='http', auth='public', csrf=False)
    def payu_return(self, **post):
        """ PlPayu."""
        _logger.info(
            'PlPayu RETURN  %s', pprint.pformat(post))
        return_url = '/'
        if post:
            request.env['payment.transaction'].sudo().form_feedback(post, 'plpayu')
            return_url = post.get('udf1')
        return werkzeug.utils.redirect(return_url)

    @http.route(['/payment/plpayu/cancel'], type='http', auth='public', csrf=False)
    def payu_cancel(self, **post):
        """ PlPayu."""
        _logger.info(
            'PlPayu CANCEL %s', pprint.pformat(post))
        return_url = '/'
        if post:
            request.env['payment.transaction'].sudo().form_feedback(post, 'plpayu')
            return_url = post.get('udf1')
        return werkzeug.utils.redirect(return_url)


    @http.route(['/payment/plpayu/error'], type='http', auth='public', csrf=False)
    def payu_error(self, **post):
        """ PlPayu."""
        _logger.info(
            'PlPayu: ERROR %s', pprint.pformat(post))
        return_url = '/'
        if post:
            request.env['payment.transaction'].sudo().form_feedback(post, 'plpayu')
            return_url = post.get('udf1')
        return werkzeug.utils.redirect(return_url)


