# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Stock picking batch report",
    "category": "Inventory/Inventory",
    "depends": ["stock"],
    "author": "Tecnativa",
    "authors": ["Cristian Monja", "Erick Delgado"],
    "version": "14.0.0.0.1",
    "data": [
        "views/stock_picking_batch_views.xml",
        "report/stock_picking_batch_report_views.xml",
        "report/report_picking_batch.xml",
    ],
    "installable": True,
    "license": "LGPL-3",
}
