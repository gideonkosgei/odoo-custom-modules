# -*- coding: utf-8 -*-
from odoo import fields, models


class HealthCountry(models.Model):
    _name = "health.country"
    _description = "Country"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "id"
    _rec_name = "country_name"

    country_code = fields.Integer('Country Code', required=True, tracking=True)
    country_name = fields.Char('Country Name', required=True, tracking=True)
    iso_code = fields.Char('ISO Code', required=True, tracking=True)
    region_text = fields.Char('Region Text', required=True, tracking=True)
    zone_text = fields.Char('Zone Text', required=True, tracking=True)
    ward_text = fields.Char('Ward Text', required=True, tracking=True)
    village_text = fields.Char('Village Text', required=True, tracking=True)
    admin_unit_level_four_ids = fields.One2many('health.admin.unit.level.four', 'country_id', string='Admin Units')




