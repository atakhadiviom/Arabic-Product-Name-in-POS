# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is an Odoo 19 POS module that adds Arabic product name display to the Point of Sale interface. It extends the standard POS to show Arabic names alongside product names in three locations: product cards, order lines, and receipts.

## Architecture

The module follows standard Odoo addon structure with three extension points:

1. **Backend Model Extension** (`models/pos_config.py`): Adds `show_arabic_product_names` boolean field to `pos.config` for per-POS enable/disable control.

2. **Frontend JavaScript** (`static/src/js/pos_arabic_name.js`): Uses Odoo's POS extension pattern with `Registries.Model.extend()` to patch:
   - `PosGlobalState` - ensures `arabic_name` is loaded for products
   - `Orderline` - overrides `getDisplayName()` to return Arabic name when enabled
   - `ProductItem` component via `patch()` - adds `arabicName` computed property

3. **XML Templates** (`static/src/xml/pos_arabic_templates.xml`): Uses XPath inheritance to inject Arabic name elements into existing POS templates (`ProductItem`, `Orderline`, `ReceiptLine`).

4. **CSS** (`static/src/css/pos_arabic.css`): Arabic-specific styling with RTL direction (`direction: rtl`) and appropriate fonts for Arabic text rendering.

## Key Implementation Notes

- Products must have an `arabic_name` field defined on the product model (this module assumes the field exists but does not define it)
- The `env.pos.config.show_arabic_product_names` flag controls visibility throughout the POS UI
- All Arabic text uses `direction: rtl` for proper rendering
- Template inheritance uses `hasclass()` selectors for more robust XPath targeting

## Odoo Development

- Module uses `assets` in `__manifest__.py` to inject JS/CSS into `point_of_sale.assets` and templates into `point_of_sale.assets_templates`
- View inheritance via `ir.ui.view` with `inherit_id` referencing standard POS views
- All files use `# -*- coding: utf-8 -*-` for Arabic character support
