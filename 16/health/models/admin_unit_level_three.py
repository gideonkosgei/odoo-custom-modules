# -*- coding: utf-8 -*-
from odoo import fields, models


class HealthAdminUnitLevelThree(models.Model):
    _name = "health.admin.unit.level.three"
    _description = "Admin Unit Level Three"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "id"
    _rec_name = "level_name"

    country_id = fields.Many2one(comodel_name='health.country', string='Country', required=True,
                                 tracking=True)
    level_one_id = fields.Many2one(comodel_name='health.admin.unit.level.one', string='Level One', required=True,
                                   tracking=True, domain="[('country_id', '=', country_id)]")
    level_two_id = fields.Many2one(comodel_name='health.admin.unit.level.two', string='Level Two', required=True,
                                   tracking=True, domain="[('level_one_id', '=', level_one_id)]")
    level_code = fields.Char('Level Code', required=True, tracking=True)
    level_name = fields.Char('Level Name', required=True, tracking=True)




