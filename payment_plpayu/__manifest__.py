# -*- coding: utf-8 -*-
# 

{
    'name': 'Payu Poland Payment Acquirer',
    'category': 'Payment Acquirer',
    'summary': 'Payment Acquirer : Implementation for  Payu Poland',
    'description': """
    Payment Acquirer : Implementation for  Payu Poland.
    Author: Jurek Wawro
    Copyright: Galicea
    License: ALGPL-3.0
    """,
    'depends': ['payment'],
    'data': [
        'views/payment_views.xml',
        'views/payment_plpayu_templates.xml',
        'data/payment_acquirer_data.xml',
    ],
    'license': 'OEEL-1',
}
