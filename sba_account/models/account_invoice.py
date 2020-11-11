##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    code_sls = fields.Char(string="SLS", required=False)

    @api.multi
    def action_invoice_open(self):
        if self.type in ['in_refund', 'out_refund'] and not self.origin:
            raise ValidationError(_("Debe completar el campo Documento de origen"))
        return super(AccountInvoice, self).action_invoice_open()
