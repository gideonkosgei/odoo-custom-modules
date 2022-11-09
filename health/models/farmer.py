# -*- coding: utf-8 -*-
from odoo import fields, models


class HealthFarmer(models.Model):
    _name = "health.farmer"
    _description = "Farmer"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "id"
    _rec_name = "farmer_name"

    visiting_date = fields.Date('Date Of Visit', required=True, tracking=True)
    visiting_doctor_name = fields.Char('Doctor Name', tracking=True,
                                       required=True)
    farmer_name = fields.Char('Farmer Name', required=True, tracking=True)
    farmer_phone_number = fields.Char('Contact Number', tracking=True)
    country_id = fields.Many2one(comodel_name='health.country', string='Country', tracking=True)

    # animal_ids = fields.One2many('health.animal', 'client_id', string='Animal')
