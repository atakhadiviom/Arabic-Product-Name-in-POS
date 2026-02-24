# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductProduct(models.Model):
    _inherit = 'product.product'

    arabic_name = fields.Char(
        string='Arabic Name',
        related='product_tmpl_id.arabic_name',
        readonly=False,
        store=True,
        translate=True,
        help='Arabic name of the product for POS display and receipts'
    )

    def _get_pos_product_properties(self, price, uom):
        """
        Override to include Arabic name in POS product data
        """
        res = super()._get_pos_product_properties(price, uom)
        res['arabic_name'] = self.arabic_name or ''
        return res

    def get_arabic_display_name(self):
        """
        Get the Arabic display name for the product.
        Falls back to the regular display name if Arabic name is not set.
        """
        self.ensure_one()
        return self.arabic_name if self.arabic_name else self.display_name
