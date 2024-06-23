# -*- coding: utf-8 -*-
from odoo import fields, models


class HealthFarmer(models.Model):
    _name = "health.odk.user"
    _description = "User"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "id"
    _rec_name = "username"

    full_name = fields.Char('Name', tracking=True, required=True)
    username = fields.Char('Username', required=True, tracking=True)
    password = fields.Char('password', tracking=True, required=True)
    role = fields.Many2one(comodel_name='health.config.catalogue.item', string='Role', tracking=True,
                           domain="[('catalogue_id', '=', 23)]")
    country_id = fields.Many2one(comodel_name='health.country', string='Country', required=True, tracking=True)
    legacy_code = fields.Char('legacy Code', tracking=True)
    is_active = fields.Boolean('Is Active?', required=True, tracking=True, default=True)


