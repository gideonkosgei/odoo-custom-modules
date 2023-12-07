# -*- coding: utf-8 -*-
from odoo import fields, models


class HealthAdminUnitLevelFour(models.Model):
    _name = "health.admin.unit.level.four"
    _description = "Admin Unit Level Four"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "id"
    _rec_name = "level_name"

    country_id = fields.Many2one(comodel_name='health.country', string='Country', required=True,
                                 tracking=True)
    level_one_id = fields.Many2one(comodel_name='health.admin.unit.level.one', string='Level One', required=True,
                                   tracking=True)
    level_two_id = fields.Many2one(comodel_name='health.admin.unit.level.two', string='Level Two', required=True,
                                   tracking=True, domain="[('level_one_id', '=', level_one_id)]")
    level_three_id = fields.Many2one(comodel_name='health.admin.unit.level.three', string='Level Three', required=True,
                                     tracking=True, domain="[('level_two_id', '=', level_two_id)]")
    level_code = fields.Char('Level Code', required=True, tracking=True)
    level_name = fields.Char('Level Name', required=True, tracking=True)
