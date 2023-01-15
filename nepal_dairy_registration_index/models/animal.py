# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class NepalDairyIndexAnimal(models.Model):
    _name = "nepal.dairy.index.animal"
    _description = "Animal"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "id desc"
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
    province = fields.Char('Province', related='farmer_id.province', tracking=True)
    province_code = fields.Char('Province Code', related='farmer_id.province_code', tracking=True)
    district = fields.Char('District', related='farmer_id.district', tracking=True)
    district_code = fields.Char('District Code', related='farmer_id.district_code', tracking=True)
    municipality = fields.Char('Municipality', related='farmer_id.municipality', tracking=True)
    municipality_code = fields.Char('Municipality Code', related='farmer_id.municipality_code', tracking=True)
    ward = fields.Char('Ward', related='farmer_id.ward', tracking=True)
    ward_code = fields.Char('Ward Code', related='farmer_id.ward_code', tracking=True)
    herd_id = fields.Char('Herd ID', tracking=True, required=True)
    serial_number = fields.Integer('Serial No', tracking=True, required=True)
    _sql_constraints = [('reg_number_unique', 'unique (reg_number)', 'A Record Exists With The Same Animal ID')]

    @api.model
    def create(self, vals):
        farm_id = vals.get('farmer_id')
        farm_rec = self.env['nepal.dairy.index.farmer'].search([("id", "=", farm_id)])

        if farm_rec:
            province_code = farm_rec.province_code
            district_code = farm_rec.district_code.zfill(2)
            municipality_code = farm_rec.municipality_code.zfill(2)
            ward_code = farm_rec.ward_code.zfill(2)
            herd_id = province_code + district_code + municipality_code + ward_code

            # Generate new serial number -> get the last serial number & increment by 1
            animal_rec = self.env['nepal.dairy.index.animal'].search([("herd_id", "=", herd_id)])
            if animal_rec:
                last_serial = max(d.serial_number for d in animal_rec)
                serial = last_serial + 1
            else:
                serial = 1

        else:
            raise ValidationError("Error In Generating Registration Number. Cannot Retrieve Administrative Codes")

        if vals.get('reg_number', _('New')) == _('New'):
            vals['reg_number'] = herd_id + str(serial).zfill(4)
            vals['herd_id'] = herd_id
            vals['serial_number'] = serial
        res = super(NepalDairyIndexAnimal, self).create(vals)
        return res
