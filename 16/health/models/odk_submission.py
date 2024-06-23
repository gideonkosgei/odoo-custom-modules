# -*- coding: utf-8 -*-
from odoo import fields, models


class HealthOdkSubmission(models.Model):
    _name = "health.odk.submission"
    _description = "ODK Submission"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "id"

    odk_submitted_object = fields.Text('Submission Object', required=True, tracking=True)
    submission_uuid = fields.Text('submission UUID', tracking=True)
    _id = fields.Integer('_id', tracking=True)
    start_time = fields.Datetime('Start Time', tracking=True)
    end_time = fields.Datetime('End Time', tracking=True)
    form_id = fields.Integer('Form ID', tracking=True)
    form_name = fields.Char('Form Name', tracking=True)
    instance_name = fields.Char('Instance Name', tracking=True)
    submitted_by = fields.Char('Submitted By', tracking=True)
    instance_id = fields.Char('Instance ID', tracking=True)
    geo_location = fields.Char('Geo Location', tracking=True)
    form_edited = fields.Boolean('Form Edited', tracking=True)
    version = fields.Integer('Version', tracking=True)
    duration = fields.Float('Duration', tracking=True)
    gps_location_lon = fields.Float('GPS Longitude', tracking=True)
    gps_location_lat = fields.Float('GPS Latitude', tracking=True)
    odk_user_id = fields.Integer('User Account', tracking=True)
    is_processed = fields.Boolean('Is Processed', required=True, tracking=True, default=False)
