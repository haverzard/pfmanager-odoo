# -*- coding: utf-8 -*-
{
    'name': "PFManager",

    'summary': """
        ODOO Module for Pertamina Foundation""",

    'description': """
        ODOO Module for Pertamina Foundation
    """,

    'author': "haverzard",
    'website': "http://www.haverzard.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security-group.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'qweb': [
        'static/src/img/*',
        'static/src/css/*',
    ],
    'installable': True,
    'application': True,
}
