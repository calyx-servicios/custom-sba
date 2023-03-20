from odoo import models, _


class GeneralLedgerXslx(models.AbstractModel):
    _inherit = "report.a_f_r.report_general_ledger_xlsx"

    def _get_report_columns(self, report):

        res = {
            0: {"header": _("Date"), "field": "date", "width": 11},
            1: {"header": _("Entry"), "field": "entry", "width": 18},
            2: {"header": _("Journal"), "field": "journal", "width": 8},
            3: {"header": _("Account"), "field": "account", "width": 9},
            4: {
                "header": _("Account Name"),
                "field": "account_name",
                "field_initial_balance": "name",
                "width": 9,
            },
            5: {"header": _("Display Name"), "field": "entry_name", "width": 9},
            6: {"header": _("Taxes"), "field": "taxes_description", "width": 15},
            7: {"header": _("Partner"), "field": "partner", "width": 25},
            8: {"header": _("Ref - Label"), "field": "label", "width": 40},
            9: {"header": _("IN"), "field": "new_description", "width": 40},
            10: {"header": _("Cost center"), "field": "center_name", "width": 15},
            11: {"header": _("Tags"), "field": "tags", "width": 10},
            12: {"header": _("Rec."), "field": "matching_number", "width": 5},
            13: {
                "header": _("Debit"),
                "field": "debit",
                "field_initial_balance": "initial_debit",
                "field_final_balance": "final_debit",
                "type": "amount",
                "width": 14,
            },
            14: {
                "header": _("Credit"),
                "field": "credit",
                "field_initial_balance": "initial_credit",
                "field_final_balance": "final_credit",
                "type": "amount",
                "width": 14,
            },
            15: {
                "header": _("Cumul. Bal."),
                "field": "cumul_balance",
                "field_initial_balance": "initial_balance",
                "field_final_balance": "final_balance",
                "type": "amount",
                "width": 14,
            },
        }
        if report.foreign_currency:
            foreign_currency = {
                16: {
                    "header": _("Cur."),
                    "field": "currency_id",
                    "field_currency_balance": "currency_id",
                    "type": "many2one",
                    "width": 7,
                },
                17: {
                    "header": _("Amount cur."),
                    "field": "amount_currency",
                    "field_initial_balance": "initial_balance_foreign_currency",
                    "field_final_balance": "final_balance_foreign_currency",
                    "type": "amount_currency",
                    "width": 14,
                },
            }
            res = {**res, **foreign_currency}
        return res
