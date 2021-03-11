# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models


class StockPickingBatch(models.Model):
    _inherit = "stock.picking.batch"

    def action_print_group(self):
        self.ensure_one()
        return self.env.ref(
            "stock_picking_batch_report.action_report_picking_batch_turboserver"
        ).report_action(self)
