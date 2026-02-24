# -*- coding: utf-8 -*-
{
    'name': 'Arabic Product Name in POS',
    'version': '19.0.1.0.0',
    'category': 'Point Of Sale',
    'summary': 'Display Arabic product names in POS Product Card, Order Line and Receipt',
    'author': 'Your Name',
    'website': 'https://your-website.com',
    'depends': [
        'point_of_sale',
    ],
    'data': [
        'views/pos_views.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'arabic_product_pos/static/src/js/pos_arabic_name.js',
            'arabic_product_pos/static/src/css/pos_arabic.css',
            'arabic_product_pos/static/src/xml/pos_arabic_templates.xml',
        ],
    },
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'application': False,
}
