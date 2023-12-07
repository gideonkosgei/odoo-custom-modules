# -*- coding: utf-8 -*-
from odoo import fields, models


class HealthAdminUnitLevelOne(models.Model):
    _name = "health.admin.unit.level.one"
    _description = "Admin Unit Level One"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "id"
    _rec_name = "level_name"

    country_id = fields.Many2one(comodel_name='health.country', string='Country', required=True,
                                 tracking=True)
    level_code = fields.Char('Level Code', required=True, tracking=True)
    level_name = fields.Char('Level Name', required=True, tracking=True)



