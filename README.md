# Arabic Product Name in POS

An Odoo 19 module that displays Arabic product names in the Point of Sale (POS) interface.

## Features

- Display Arabic product names in the POS Product Card
- Show Arabic names in Order Lines
- Print Arabic names on POS receipts
- Configurable setting to enable/disable Arabic names per POS configuration
- Adds `arabic_name` field to products

## Requirements

- Odoo 19.0
- `point_of_sale` module

## Installation

1. Clone or download this repository
2. **Important:** Rename the folder to `arabic_product_pos`
3. Copy the renamed `arabic_product_pos` folder to your Odoo addons directory
4. Restart Odoo server
5. Update the module list in Odoo Apps
6. Search for "Arabic Product Name in POS"
7. Click Install

## Configuration

After installation:

1. Go to **Point of Sale > Configuration > Point of Sale**
2. Open a POS configuration
3. In the "Arabic Product Names" section, enable **Show Arabic Product Names in POS**
4. Save the configuration

## Usage

1. Open any product and fill in the **Arabic Name** field
2. Open POS and the Arabic names will display in:
   - Product cards in the POS interface
   - Order lines in the current order
   - Printed receipts

## Module Structure

```
arabic_product_pos/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── pos_config.py       # POS config extension for Arabic name setting
│   ├── product.py          # Product model extension (adds arabic_name field)
│   └── pos_order.py        # POS field loading for arabic_name
├── views/
│   └── pos_views.xml       # POS config form view extension
└── static/
    ├── src/
    │   ├── js/
    │   │   └── pos_arabic_name.js          # Frontend logic
    │   ├── xml/
    │   │   └── pos_arabic_templates.xml    # POS template overrides
    │   └── css/
    │       └── pos_arabic.css              # RTL Arabic styles
    └── description/
        ├── icon.png
        └── index.html
```

## License

LGPL-3

## Author

Your Name
