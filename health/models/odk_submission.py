# -*- coding: utf-8 -*-
from odoo import fields, models


class HealthOdkSubmission(models.Model):
    _name = "health.odk.submission"
    _description = "ODK Submission"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "id"

    odk_submitted_object = fields.Text('Submission Object', required=True, tracking=True)
    is_processed = fields.Boolean('Is Processed', required=True, tracking=True, default=False)
    submission_uuid = fields.Text('submission UUID', tracking=True)



