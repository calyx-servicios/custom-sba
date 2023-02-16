from odoo import models, fields


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    new_description = fields.Text(compute="_get_new_description")

    def _get_new_description(self):
        for rec in self:
            account_line = self.env["account.invoice.line"].search(
                [("invoice_id", "=", rec.invoice_id.id)]
            )
            if len(account_line) == 0:
                return True
            for account in account_line:
                if (
                    rec.account_id == account.account_id
                    and account.product_id == rec.product_id
                ):
                    rec.update({"new_description": account.new_description})
