# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductProduct(models.Model):
    _inherit = 'product.product'

    arabic_name = fields.Char(
        compute='_compute_arabic_name',
        string='Arabic Name',
        help='Arabic name of the product fetched from translations'
    )

    @api.depends('name')
    def _compute_arabic_name(self):
        """Fetch Arabic translation for the product name"""
        # Find the first available Arabic language
        arabic_lang = self.env['res.lang'].search([('code', 'ilike', 'ar_')], limit=1)
        lang_code = arabic_lang.code if arabic_lang else 'ar_001'
        
        for product in self:
            # Get the name in the Arabic context
            product.arabic_name = product.with_context(lang=lang_code).display_name or ''
