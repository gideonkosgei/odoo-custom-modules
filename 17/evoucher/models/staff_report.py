from io import BytesIO
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError
class StaffReport(models.AbstractModel):
    _name = 'report.evoucher.report_evoucher_template'

    @api.model
    def _get_report_values(self, docids, data=None):

        vouchers = self.env['evoucher.staff'].browse(docids) if docids else self.env['evoucher.staff'].search([])

        return {
            'docs': vouchers
        }

