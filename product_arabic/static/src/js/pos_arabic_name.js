// -*- coding: utf-8 -*-
odoo.define('product_arabic.pos_arabic_name', function (require) {
    "use strict";

    const { PosGlobalState, Orderline } = require('point_of_sale.models');
    const Registries = require('point_of_sale.Registries');
    const { useState } = owl;

    /**
     * Extend PosGlobalState to load Arabic names for products
     */
    const PosArabicGlobalState = (PosGlobalState) => class PosArabicGlobalState extends PosGlobalState {
        async _processPosProduct(product) {
            await super._processPosProduct(...arguments);
            // Ensure arabic_name is loaded from the server
            product.arabic_name = product.arabic_name || '';
        }
    };

    /**
     * Extend Orderline to display Arabic names
     */
    const PosArabicOrderline = (Orderline) => class PosArabicOrderline extends Orderline {
        getDisplayName() {
            const product = this.get_product();
            if (this.pos.config.show_arabic_product_names && product && product.arabic_name) {
                return product.arabic_name;
            }
            return super.getDisplayName(...arguments);
        }
    };

    // Register the extended models
    Registries.Model.extend(PosGlobalState, PosArabicGlobalState);
    Registries.Model.extend(Orderline, PosArabicOrderline);

    // Also patch the ProductItem component to show Arabic name
    patch('point_of_sale.ProductItem', 'product_arabic.ProductItem', (T) => {
        class ProductItemExtension extends T {
            get arabicName() {
                return this.props.product.arabic_name || '';
            }
        }
        return ProductItemExtension;
    });

    return {
        PosArabicGlobalState: PosArabicGlobalState,
        PosArabicOrderline: PosArabicOrderline,
    };
});
