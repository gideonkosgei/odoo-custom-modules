# -*- coding: utf-8 -*-
from odoo import fields, models


class HealthClient(models.Model):
    _name = "health.client"
    _description = "Client"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "id"
    _rec_name = "client_name"

    client_name = fields.Char('Name', required=True, tracking=True)
    client_address = fields.Char('Address', tracking=True)
    client_contact_number = fields.Char('Contact Number', tracking=True)
    client_place = fields.Char('Place', tracking=True)
    animal_ids = fields.One2many('health.animal', 'client_id', string='Animal')
