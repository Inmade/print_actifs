from odoo import api, fields, models


class VATReport(models.TransientModel):
    _name = "reports_vat_report"

    company_id = fields.Many2one(comodel_name='res.company')
    date_at = fields.Date(required=True,
                          default=fields.Date.context_today)
