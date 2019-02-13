# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import datetime

class AssetReportWizard(models.TransientModel):
    """Asset report wizard."""

    _name = 'asset.report.wizard'
    _description = 'Asset Report Wizard'
    # _inherit = "account.asset.asset"

    company_id = fields.Many2one(
        comodel_name='res.company',
        default=lambda self: self.env.user.company_id,
        required=False,
        string='Company'
    )
    date_at = fields.Date(string="Date", default=lambda self:datetime.today())
    asset_ids = fields.Many2many("account.asset.asset", "zeguierhuig", string="Asset")

    @api.multi
    def button_export_pdf(self):
        print("1")
        self.ensure_one()
        report_type = 'qweb-pdf'

        actif_ids = self.env['account.asset.asset'].search([('date','<=',self.date_at)])

        self.asset_ids = [(6, 0, [a.id for a in actif_ids])]

        return self._export(report_type)
    @api.multi
    def button_export_xlsx(self):
        self.ensure_one()
        report_type = 'xlsx'
        return self._export(report_type)

    def _export(self, report_type):
        print("2")
        print(self.asset_ids)
        """Default export is PDF."""
        # model = self.env['asset.report.wizard']
        # report = model.create(self._prepare_vat_report())
        return self.print_report(report_type)

    @api.multi
    def print_report(self, report_type='qweb'):
        print("4")
        print("DATE ===== ",self.date_at)
        self.ensure_one()
        report_name = 'print_actifs.project_journal_items_id'
        # report_name = 'print_actifs.project_journal_items_id'
        context = dict(self.env.context)
        action = self.env['ir.actions.report'].search(
            [('report_name', '=', report_name),
             ('report_type', '=', report_type)], limit=1)
        print(context)
        context.update({
            'test': "test2",
        })
        print(context)
        print("---------")
        return action.with_context(context).report_action(self)

    def _prepare_vat_report(self):
        print("3")
        self.ensure_one()
        return {
            'company_id': self.company_id.id,
            'date_at': self.date_at,
        }

