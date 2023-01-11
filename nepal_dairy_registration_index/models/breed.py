# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class NepalDairyIndexBreed(models.Model):
    _name = "nepal.dairy.index.breed"
    _description = "Breed"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "id"
    _rec_name = "breed_name"
    species_id = fields.Many2one(comodel_name='nepal.dairy.index.list.item', string='Species', required=True,
                                 tracking=True, domain="[('list_id', '=', 2)]")
    breed_name = fields.Char('Breed Name', required=True, tracking=True)
    breed_is_active = fields.Boolean('Is Breed Active?', required=True, tracking=True, default=True)






