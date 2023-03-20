from odoo import models, fields


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    new_description = fields.Text()
