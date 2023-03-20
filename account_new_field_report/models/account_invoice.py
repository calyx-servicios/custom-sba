from odoo import models, fields, api, _
from odoo.exceptions import UserError


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    @api.model
    def invoice_line_move_line_get(self):
        res = []
        for line in self.invoice_line_ids:
            if line.quantity == 0:
                continue
            tax_ids = []
            for tax in line.invoice_line_tax_ids:
                tax_ids.append((4, tax.id, None))
                for child in tax.children_tax_ids:
                    if child.type_tax_use != "none":
                        tax_ids.append((4, child.id, None))
            analytic_tag_ids = [
                (4, analytic_tag.id, None) for analytic_tag in line.analytic_tag_ids
            ]
            move_line_dict = {
                "invl_id": line.id,
                "type": "src",
                "name": line.name.split("\n")[0][:64],
                "new_description": line.new_description,
                "price_unit": line.price_unit,
                "quantity": line.quantity,
                "price": line.price_subtotal,
                "account_id": line.account_id.id,
                "product_id": line.product_id.id,
                "uom_id": line.uom_id.id,
                "account_analytic_id": line.account_analytic_id.id,
                "tax_ids": tax_ids,
                "invoice_id": self.id,
                "analytic_tag_ids": analytic_tag_ids,
            }
            res.append(move_line_dict)
        return res
