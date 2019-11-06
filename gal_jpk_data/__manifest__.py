# -*- coding: utf-8 -*-
{
    'name': "Gaicea - JPK - zbieranie danych",

    'summary': """
        Gromadzenie danych do JPK
    """,

    'description': """
        Dane do JPK
    """,

    'author': "Jerzy Wawro, Galicea",
    'website': "http://www.galicea.org",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base', 'account', 'account_gal'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
#        'wizard/creator.xml',
    ],

}