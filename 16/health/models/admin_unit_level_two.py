# -*- coding: utf-8 -*-
from odoo import fields, models


class HealthAdminUnitLevelTwo(models.Model):
    _name = "health.admin.unit.level.two"
    _description = "Admin Unit Level Two"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "id"
    _rec_name = "level_name"

    country_id = fields.Many2one(comodel_name='health.country', string='Country', required=True,
                                 tracking=True)
    level_one_id = fields.Many2one(comodel_name='health.admin.unit.level.one', string='Level One', required=True,
                                   tracking=True, domain="[('country_id', '=', country_id)]")
    level_code = fields.Char('Level Code', required=True, tracking=True)
    level_name = fields.Char('Level Name', required=True, tracking=True)
