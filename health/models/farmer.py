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
    farmer_phone_number = fields.Char('Farmer Phone Number', tracking=True)
    country_id = fields.Many2one(comodel_name='health.country', string='Country', tracking=True)
    level_one_id = fields.Many2one(comodel_name='health.admin.unit.level.one', string='Level 1', tracking=True)

