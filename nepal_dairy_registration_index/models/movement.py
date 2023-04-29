# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class NepalDairyIndexMovement(models.Model):
    _name = "nepal.dairy.index.movement"
    _description = "Movement/Transfer"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "id"
    _rec_name = "animal_id"

    origin_herd_id = fields.Many2one(comodel_name='nepal.dairy.index.farmer', string=' Herd(from)', tracking=True,
                                     required=True)
    origin_herd_code = fields.Char('Herd ID(from)', related='origin_herd_id.herd_id')
    destination_herd_id = fields.Many2one(comodel_name='nepal.dairy.index.farmer', string='Herd(to)',
                                          tracking=True, required=True)
    destination_herd_code = fields.Char('Herd ID (to)', related='destination_herd_id.herd_id')
    animal_id = fields.Many2one(comodel_name='nepal.dairy.index.animal', string='Animal ID')
    tag_id = fields.Char('Tag ID', related='animal_id.tag_id')
    species = fields.Char('Species', related='animal_id.species')
    sex = fields.Char('Sex', related='animal_id.sex')
    breed = fields.Char('Breed', related='animal_id.breed')
    animal_dob = fields.Date('Birth Date', related='animal_id.animal_dob')

    origin_province = fields.Char('Province(from)', related='origin_herd_id.province')
    origin_district = fields.Char('District(from)', related='origin_herd_id.district')
    origin_municipality = fields.Char('Municipality(from)', related='origin_herd_id.municipality')
    origin_ward = fields.Char('Ward(from)', related='origin_herd_id.ward')

    destination_province = fields.Char('Province(to)', related='destination_herd_id.province')
    destination_district = fields.Char('District(to)', related='destination_herd_id.district')
    destination_municipality = fields.Char('Municipality(to)', related='destination_herd_id.municipality')
    destination_ward = fields.Char('Ward(to)', related='destination_herd_id.ward')

