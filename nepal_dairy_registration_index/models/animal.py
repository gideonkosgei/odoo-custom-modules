# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class NepalDairyIndexAnimal(models.Model):
    _name = "nepal.dairy.index.animal"
    _description = "Animal"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "id"
    _rec_name = "reg_number"

    farmer_id = fields.Many2one(comodel_name='nepal.dairy.index.farmer', string='Farmer', tracking=True, required=True)
    species_id = fields.Many2one(comodel_name='nepal.dairy.index.list.item', string='Species', tracking=True,
                                 required=True, domain="[('list_id', '=',2)]")
    sex_id = fields.Many2one(comodel_name='nepal.dairy.index.list.item', string='Sex', tracking=True,
                             required=True, domain="[('list_id', '=',1)]")
    breed_id = fields.Many2one(comodel_name='nepal.dairy.index.breed', string='Breed',
                               tracking=True, domain="[('species_id', '=', species_id)]")
    animal_dob = fields.Date('Birth Date', tracking=True)
    reg_number = fields.Char('Animal ID', required=True, tracking=True, readonly=True,
                             default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('reg_number', _('New')) == _('New'):
            vals['reg_number'] = self.env['ir.sequence'].next_by_code('nepal.dairy.index.animal') or _('New')

        res = super(NepalDairyIndexAnimal, self).create(vals)
        return res
