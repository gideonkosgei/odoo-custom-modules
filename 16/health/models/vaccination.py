# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class HealthVaccination(models.Model):
    _name = "health.vaccination"
    _description = "Vaccination"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "id"

    animal_id = fields.Many2one(comodel_name='health.animal', string='Animal',
                                tracking=True)
    vaccine_id = fields.Many2one(comodel_name='health.config.catalogue.item', string='Vaccine',
                                 tracking=True, domain="[('catalogue_id', '=', 22)]")
    vaccination_date = fields.Date('Date', tracking=True)
    odk_user_id = fields.Many2one(comodel_name='health.odk.user', string='ODK User', tracking=True)
    submission_uuid = fields.Text('submission UUID', tracking=True)
