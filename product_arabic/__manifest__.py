# -*- coding: utf-8 -*-
{
    'name': 'Arabic Product Name in POS',
    'version': '19.0.1.0.0',
    'category': 'Point Of Sale',
    'summary': 'Adds Arabic product names in POS product screen and receipt',
    'author': 'Your Name',
    'website': 'https://your-website.com',
    'depends': [
        'point_of_sale',
        'product',
        'base',
    ],
    'data': [
        'views/product_views.xml',
        'views/pos_views.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'product_arabic/static/src/js/pos_arabic_name.js',
            'product_arabic/static/src/css/pos_arabic.css',
        ],
        'point_of_sale.assets_templates': [
            'product_arabic/static/src/xml/pos_arabic_templates.xml',
        ],
    },
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'external_dependencies': {
        'python': [],
    },
    'application': False,
}
