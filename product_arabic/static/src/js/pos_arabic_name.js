// -*- coding: utf-8 -*-
odoo.define('product_arabic.pos_arabic_name', function (require) {
    "use strict";

    const { PosGlobalState, Orderline, Product } = require('point_of_sale.models');
    const Registries = require('point_of_sale.Registries');

    /**
     * Extend Product model to support Arabic names
     */
    const PosArabicProduct = (Product) => class PosArabicProduct extends Product {
        /**
         * Export data for POS - include Arabic name
         */
        export_as_JSON() {
            const json = super.export_as_JSON(...arguments);
            json.arabic_name = this.arabic_name || '';
            return json;
        }

        /**
         * Initialize from JSON
         */
        init_from_JSON(json) {
            super.init_from_JSON(...arguments);
            this.arabic_name = json.arabic_name || '';
        }
    };

    /**
     * Extend PosGlobalState to load Arabic names
     */
    const PosArabicGlobalState = (PosGlobalState) => class PosArabicGlobalState extends PosGlobalState {
        async _processPosProduct(product) {
            await super._processPosProduct(...arguments);
            product.arabic_name = product.arabic_name || '';
        }
    };

    /**
     * Extend Orderline to display Arabic names
     */
    const PosArabicOrderline = (Orderline) => class PosArabicOrderline extends Orderline {
        /**
         * Get the display name for the order line
         */
        get_display_name() {
            const product = this.get_product();
            if (this.pos.config.show_arabic_product_names && product && product.arabic_name) {
                return product.arabic_name;
            }
            return super.get_display_name(...arguments);
        }
    };

    // Register the extended models
    Registries.Model.extend(Product, PosArabicProduct);
    Registries.Model.extend(PosGlobalState, PosArabicGlobalState);
    Registries.Model.extend(Orderline, PosArabicOrderline);

    return {
        PosArabicProduct: PosArabicProduct,
        PosArabicGlobalState: PosArabicGlobalState,
        PosArabicOrderline: PosArabicOrderline,
    };
});
