# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class NepalDairyIndexFarmer(models.Model):
    _name = "nepal.dairy.index.farmer"
    _description = "Farmer"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "id"
    _rec_name = "farmer_name"

    farmer_name = fields.Char('Farmer|Farm Name', required=True, tracking=True)
    image = fields.Binary(string='farmer Photo')
    farmer_type = fields.Many2one(comodel_name='nepal.dairy.index.list.item', string='Category', tracking=True,
                                  required=True, domain="[('list_id', '=',3)]")

    entity_type = fields.Many2one(comodel_name='nepal.dairy.index.list.item', string='Entity Type', tracking=True,
                                  required=True, default=8, domain="[('list_id', '=',4)]")

    street = fields.Char('Street', required=False, tracking=True)
    house_number = fields.Char('House Number', required=False, tracking=True)
    mobile = fields.Char('Mobile', required=False, tracking=True)
    national_identification_card_number = fields.Char('ID|Reg Number', tracking=True)

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
    province = fields.Char('Province', related='province_id.province_name', tracking=True)
    province_code = fields.Char('Province Code', related='province_id.province_code', tracking=True)
    district = fields.Char('District', related='district_id.district_name', tracking=True)
    district_code = fields.Char('District Code', related='district_id.district_code', tracking=True)
    municipality = fields.Char('Municipality', related='municipality_id.municipality_name', tracking=True)
    municipality_code = fields.Char('Municipality Code', related='municipality_id.municipality_code', tracking=True)
    ward = fields.Char('Ward', related='ward_id.ward_name', tracking=True)
    ward_code = fields.Char('Ward Code', related='ward_id.ward_code', tracking=True)

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

    @api.onchange('province_id')
    def onchange_province_id(self):
        if self.province_id:
            self.district_id = None
            self.municipality_id = None
            self.ward_id = None

    @api.onchange('district_id')
    def onchange_district_id(self):
        if self.district_id:
            self.municipality_id = None
            self.ward_id = None

    @api.onchange('municipality_id')
    def onchange_municipality_id(self):
        if self.municipality_id:
            self.ward_id = None





