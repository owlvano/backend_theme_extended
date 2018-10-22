# -*- coding: utf-8 -*-
{
    'name': "Web_Responsive (Custom Extension)",

    'summary': "Custom Extension of web_responsive",

    'description': """
        Backend theme extension, but for web_responsive module. It tries.
    """,

    'author': "Ivan Sova",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Themes/Backend',
    'license': 'LGPL-3',
    'version': '10.0.2.0.1',
    'installable': True,
    # any module necessary for this one to work correctly
    'depends': ['web_responsive'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/assets.xml',
    ],
    # only loaded in demonstration mode
}