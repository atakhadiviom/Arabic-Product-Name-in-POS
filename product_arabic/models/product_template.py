# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    arabic_name = fields.Char(
        string='Arabic Name',
        translate=True,
        help='Arabic name of the product for POS display and receipts'
    )
