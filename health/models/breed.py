# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class HealthBreed(models.Model):
    _name = "health.breed"
    _description = "Breed"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "id"
    _rec_name = "breed_name"

    country_id = fields.Many2one(comodel_name='health.country', string='Country', required=True,
                                 tracking=True)
    species_id = fields.Many2one(comodel_name='health.config.catalogue.item', string='Species', required=True,
                                 tracking=True, domain="[('catalogue_id', '=', 21)]")
    breed_code = fields.Char('Breed Code', required=True, tracking=True)
    breed_name = fields.Char('Breed Name', required=True, tracking=True)
    breed_is_active = fields.Boolean('Is Breed Active?', required=True, tracking=True, default=True)






