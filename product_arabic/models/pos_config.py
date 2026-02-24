# -*- coding: utf-8 -*-

from odoo import models, fields


class PosConfig(models.Model):
    _inherit = 'pos.config'

    show_arabic_product_names = fields.Boolean(
        string='Show Arabic Product Names in POS',
        default=True,
        help='Enable to show Arabic product names in POS interface and receipts'
    )
