from odoo import models, fields, api


class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    new_description = fields.Text()

    @api.onchange("new_description")
    def _onchange_new_description(self):
        for rec in self:
            account_moves = self.env["account.move"].search(
                [("name", "=", rec.invoice_id.move_name)]
            )
            if len(account_moves) == 0:
                exit
            for am in account_moves:
                for aml in am.line_ids:
                    if (
                        rec.account_id == aml.account_id
                        and aml.product_id == rec.product_id
                    ):
                        aml.write({"new_description": rec.new_description})
