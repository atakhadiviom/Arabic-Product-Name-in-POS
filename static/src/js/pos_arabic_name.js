/** @odoo-module **/

import { Orderline } from "@point_of_sale/app/store/models";
import { patch } from "@web/core/utils/patch";

// We use XML inheritance to display the Arabic name alongside the product name.
// If you want to replace the display name entirely, uncomment the patch below.

/*
patch(Orderline.prototype, {
    getDisplayName() {
        const product = this.get_product();
        if (this.pos.config.show_arabic_product_names && product && product.arabic_name) {
            return product.arabic_name;
        }
        return super.getDisplayName(...arguments);
    },
});
*/
