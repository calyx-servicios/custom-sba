# pylint: disable=missing-module-docstring,pointless-statement
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Account New Field Report",
    "summary": """
        This module add a new field to the account form views and reports
    """,
    "author": "Calyx Servicios S.A.",
    "maintainers": ["lucianobaleani"],
    "website": "https://odoo.calyx-cloud.com.ar/",
    "license": "AGPL-3",
    "category": "Account",
    "version": "11.0.1.0.0",
    "development_status": "Production/Stable",
    "application": False,
    "installable": True,
    "depends": [
        "account",
        "l10n_ar_account",
        "sba_account",
        "account_general_ledger_customization",
    ],
    "data": [
        "views/account_invoice_line_inherited_views.xml",
        "views/account_move_line_inherited_views.xml",
        "report/account_invoice_line_report_inherited_views.xml",
        "report/templates/general_ledger.xml",
    ],
}
