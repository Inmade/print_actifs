# -*- coding: utf-8 -*-

from datetime import timedelta
from odoo import models, fields, api

class print_actifs(models.Model):
    _inherit = "account.asset.asset"



class printActifsWizard(models.TransientModel):
    _name = "print.actif.wizard"

    actifs_date = fields.Date(string="Date")

    def print_timesheet(self, data):
        data = {}
        data['ids'] = self.env.context.get('active_ids', [])
        data['model'] = self.env.context.get('active_model', 'ir.ui.menu')
        data['form'] = self.read(['actifs_date'])[0]
        used_context = self._build_contexts(data)
        data['form']['used_context'] = dict(used_context, lang=self.env.context.get('lang') or 'en_US')
        return self.env.ref('print_actifs.print_journal_items_report').report_action(self, data=data, config=False)

    def _build_contexts(self, data):
        result = {}
        result['actifs_date'] = data['form']['actifs_date'] or False
        return result

