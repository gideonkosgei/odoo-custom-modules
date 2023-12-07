# -*- coding: utf-8 -*-
from odoo import fields, models


class HealthFarmer(models.Model):
    _name = "health.farmer"
    _description = "Farmer"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "id"
    _rec_name = "farmer_name"

    visiting_date = fields.Date('Date Of Visit', required=True, tracking=True)
    farmer_name = fields.Char('Farmer Name', required=True, tracking=True)
    farmer_phone_number = fields.Char('Phone Number', tracking=True, required=True)
    country_id = fields.Many2one(comodel_name='health.country', string='Country', required=True, tracking=True)
    level_one_id = fields.Many2one(comodel_name='health.admin.unit.level.one', required=True, string='Level 1',
                                   tracking=True,
                                   domain="[('country_id', '=', country_id)]")
    level_two_id = fields.Many2one(comodel_name='health.admin.unit.level.two', required=True, string='Level 2',
                                   tracking=True,
                                   domain="[('level_one_id', '=', level_one_id)]")
    level_three_id = fields.Many2one(comodel_name='health.admin.unit.level.three', required=True, string='Level 3',
                                     tracking=True,
                                     domain="[('level_two_id', '=', level_two_id)]")
    level_four_id = fields.Many2one(comodel_name='health.admin.unit.level.four', required=True, string='Level 4',
                                    tracking=True,
                                    domain="[('level_three_id', '=', level_three_id)]")
    nutritional_plan = fields.Many2one(comodel_name='health.config.catalogue.item', string='Feed Type',
                                       tracking=True)

    regular_supply_of_minerals_and_vitamins = fields.Many2one(comodel_name='health.config.catalogue.item',
                                                              string='Minerals & Vitamins',
                                                              tracking=True)
    farm_type = fields.Many2one(comodel_name='health.config.catalogue.item', string='Farm Type', tracking=True,
                                required=True,
                                domain="[('catalogue_id', '=',24)]")
    age_group = fields.Many2one(comodel_name='health.config.catalogue.item', string='Age Group', tracking=True,
                                required=True,
                                domain="[('catalogue_id', '=',25)]")
    gender = fields.Many2one(comodel_name='health.config.catalogue.item', string=' Farmer Gender', required=True,
                             tracking=True,
                             domain="[('catalogue_id', '=',26)]")
    odk_user_id = fields.Many2one(comodel_name='health.odk.user', string='ODK User', tracking=True)
    submission_uuid = fields.Text('submission UUID', tracking=True)
