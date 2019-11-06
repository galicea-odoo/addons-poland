# -*- coding: utf-8 -*-
{
    'name': "Galicea - Jednolity Plik Kontrolny",

    'summary': """
        Jednolity Plik Kontrolny""",

    'description': """
        Jednolity Plik Kontrolny
    """,

    'author': "Galicea",
    'maintainer': "Galicea",
    'website': "http://www.galicea.org",

    'category': 'Accounting',
    'version': '12.0.0.0',

    'depends': ['web', 'galicea_environment_checkup', 'gal_jpk_data', 'account_gal'],

    'external_dependencies': {
        'python': ['xsd2xml']
    },

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/wizard.xml',
        'views/vat.xml',
        'views/data.xml',
    ],
    'application': True,

    'system_checkup': {
        'dependencies': {
            'python': [
                {
                    'name': 'xsd2xml',
                    'install': 'pip install -U $GALICEA_DIR/python-packages/pycodegen $GALICEA_DIR/python-packages/xsd2xml',
                    'min_version': '0.0.2'
                }
            ]
        }
    },
}
