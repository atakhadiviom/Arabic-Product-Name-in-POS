# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductProduct(models.Model):
    _inherit = 'product.product'

    arabic_name = fields.Char(
        string='Arabic Name',
        store=True,
        compute='_compute_arabic_name',
        inverse='_inverse_arabic_name',
        help='Arabic name of the product. Auto-filled from the Arabic '
             'translation when empty; editing it updates the translation.'
    )

    @api.depends('name')
    def _compute_arabic_name(self):
        """Default the Arabic name from the product's Arabic translation."""
        arabic_lang = self.env['res.lang'].search([('code', 'ilike', 'ar_')], limit=1)
        lang_code = arabic_lang.code if arabic_lang else 'ar_001'

        for product in self:
            if not product.arabic_name:
                # Get the name in the Arabic context
                product.arabic_name = product.with_context(lang=lang_code).display_name or ''

    def _inverse_arabic_name(self):
        """Write an edited Arabic name back to the Arabic translation."""
        arabic_lang = self.env['res.lang'].search([('code', 'ilike', 'ar_')], limit=1)
        lang_code = arabic_lang.code if arabic_lang else 'ar_001'

        for product in self:
            if product.arabic_name:
                product.with_context(lang=lang_code).name = product.arabic_name
