from odoo import api, fields, models


class MrpBom(models.Model):
    _inherit = "mrp.bom"

    total_qty = fields.Float(
        compute="_compute_total_mo", string="Total qty", store="True"
    )

    @api.depends("bom_line_ids")
    def _compute_total_mo(
        self,
    ):
        for record in self:
            total_qty = 0.0
            for data in record.bom_line_ids:
                total_qty += data.product_qty
            record.total_qty = total_qty
