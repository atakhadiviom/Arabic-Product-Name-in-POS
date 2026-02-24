# Arabic Product Name in POS

An Odoo 19 module that displays Arabic product names in the Point of Sale (POS) interface.

## Features

- Display Arabic product names in the POS Product Card
- Show Arabic names in Order Lines
- Print Arabic names on POS receipts
- Configurable setting to enable/disable Arabic names per POS configuration

## Requirements

- Odoo 19.0
- `point_of_sale` module

## Installation

1. Copy the `product_arabic` folder to your Odoo addons directory
2. Restart Odoo server
3. Update the module list in Odoo Apps
4. Search for "Arabic Product Name in POS"
5. Click Install

## Configuration

After installation:

1. Go to **Point of Sale > Configuration > Point of Sale**
2. Open a POS configuration
3. In the "Arabic Product Names" section, enable **Show Arabic Product Names in POS**
4. Save the configuration

## Usage

Once enabled, the module will display Arabic product names in:
- Product cards in the POS interface
- Order lines in the current order
- Printed receipts

Note: Products must have an `arabic_name` field defined in the product model for Arabic names to display.

## Module Structure

```
product_arabic/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── pos_config.py       # POS config extension for Arabic name setting
├── views/
│   └── pos_views.xml       # POS config form view extension
└── static/
    ├── src/
    │   ├── js/
    │   │   └── pos_arabic_name.js    # Frontend logic
    │   ├── xml/
    │   │   └── pos_arabic_templates.xml
    │   └── css/
    │       └── pos_arabic.css
    └── description/
        ├── icon.png
        └── index.html
```

## License

LGPL-3

## Author

Your Name
