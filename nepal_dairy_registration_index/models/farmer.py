# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class NepalDairyIndexFarmer(models.Model):
    _name = "nepal.dairy.index.farmer"
    _description = "Farmer"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "id"
    _rec_name = "farmer_name"

    farmer_name = fields.Char('Farmer Name', required=True, tracking=True)
    image = fields.Binary(string='farmer Photo')
    farmer_type = fields.Many2one(comodel_name='nepal.dairy.index.list.item', string='Category', tracking=True,
                                  required=True, domain="[('list_id', '=',3)]")
    gender = fields.Many2one(comodel_name='nepal.dairy.index.list.item', string='Gender', tracking=True,
                             required=True, domain="[('list_id', '=',1)]")
    street = fields.Char('Street', required=False, tracking=True)
    house_number = fields.Char('House Number', required=False, tracking=True)
    mobile = fields.Char('Mobile', required=False, tracking=True)
    national_identification_card_number = fields.Char('NID Number', required=True, tracking=True)

    email = fields.Char('Email')
    province_id = fields.Many2one(comodel_name='nepal.dairy.index.province', string='Province', required=True,
                                  tracking=True)
    district_id = fields.Many2one(comodel_name='nepal.dairy.index.district', string='District', required=True,
                                  tracking=True, domain="[('province_id', '=', province_id)]")
    municipality_id = fields.Many2one(comodel_name='nepal.dairy.index.municipality', string='Municipality',
                                      required=True, tracking=True, domain="[('district_id', '=', district_id)]")
    ward_id = fields.Many2one(comodel_name='nepal.dairy.index.ward', string='Municipality',
                              required=True, tracking=True, domain="[('district_id', '=', district_id)]")
    animal_count = fields.Integer('Animal Count', compute='_compute_animal_count')
    animal_ids = fields.One2many('nepal.dairy.index.animal', 'farmer_id', string='Farmer')

    def _compute_animal_count(self):
        for rec in self:
            animal_count = self.env['nepal.dairy.index.animal'].search_count([('farmer_id', '=', rec.id)])
            rec.animal_count = animal_count

    def action_open_animal(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Animals',
            'res_model': 'nepal.dairy.index.animal',
            'domain': [("farmer_id", "=", self.id)],
            'view_mode': 'tree,form',
            'target': 'current'
        }


