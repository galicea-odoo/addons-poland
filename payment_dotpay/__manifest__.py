# -*- coding: utf-8 -*-
# 

{
    'name': 'Dotpay Payment Acquirer',
    'category': 'Payment Acquirer',
    'summary': 'Payment Acquirer : Dotpay, Poland',
    'description': """
    Payment Acquirer : Dotpay.
    Author: Jurek Wawro
    Copyright: Galicea
    License: ALGPL-3.0
    """,
    'depends': ['payment'],
    'data': [
        'views/payment_views.xml',
        'views/payment_return.xml',
        'views/payment_dotpay_templates.xml',
        'data/payment_acquirer_data.xml',
    ],
}
