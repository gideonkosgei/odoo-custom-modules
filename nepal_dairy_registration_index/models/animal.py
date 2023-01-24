# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class NepalDairyIndexAnimal(models.Model):
    _name = "nepal.dairy.index.animal"
    _description = "Animal"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "id desc"
    _rec_name = "animal_id"

    farmer_id = fields.Many2one(comodel_name='nepal.dairy.index.farmer', string='Herd', tracking=True, required=True)
    species_id = fields.Many2one(comodel_name='nepal.dairy.index.list.item', string='Species', tracking=True,
                                 required=True, domain="[('list_id', '=',2)]")
    sex_id = fields.Many2one(comodel_name='nepal.dairy.index.list.item', string='Sex', tracking=True,
                             required=True, domain="[('list_id', '=',1)]")
    breed_id = fields.Many2one(comodel_name='nepal.dairy.index.breed', string='Breed',
                               tracking=True, domain="[('species_id', '=', species_id)]")
    animal_dob = fields.Date('Birth Date', tracking=True)
    province = fields.Char('Province', related='farmer_id.province', tracking=True)
    province_code = fields.Char('Province Code', related='farmer_id.province_code', tracking=True)
    district = fields.Char('District', related='farmer_id.district', tracking=True)
    district_code = fields.Char('District Code', related='farmer_id.district_code', tracking=True)
    municipality = fields.Char('Municipality', related='farmer_id.municipality', tracking=True)
    municipality_code = fields.Char('Municipality Code', related='farmer_id.municipality_code', tracking=True)
    ward = fields.Char('Ward', related='farmer_id.ward', tracking=True)
    ward_code = fields.Char('Ward Code', related='farmer_id.ward_code', tracking=True)

    herd_id = fields.Char('Herd ID', related='farmer_id.herd_id', tracking=True)
    serial_number = fields.Integer('Serial No', tracking=True, required=True)
    tag_id = fields.Char('Tag ID', tracking=True, required=True, readonly=True,
                         default=lambda self: _('New'))
    animal_id = fields.Char('Animal ID', required=True, tracking=True, readonly=True,
                            default=lambda self: _('New'))

    _sql_constraints = [('animal_id_unique', 'unique (animal_id)', 'A Record Exists With The Same Animal ID')]

    @api.model
    def create(self, vals):
        farm_id = vals.get('farmer_id')
        farm_rec = self.env['nepal.dairy.index.farmer'].search([("id", "=", farm_id)])

        if farm_rec:
            herd_id = farm_rec.herd_id
            # Generate new serial number -> get the last serial number & increment by 1
            animal_rec = self.env['nepal.dairy.index.animal'].search([("herd_id", "=", herd_id)])
            if animal_rec:
                last_serial = max(d.serial_number for d in animal_rec)
                serial = last_serial + 1
            else:
                serial = 1

        else:
            raise ValidationError("Error In Generating Registration Number. Cannot Retrieve Administrative Codes")

        if vals.get('animal_id', _('New')) == _('New'):
            tag_id = str(serial).zfill(5)
            vals['animal_id'] = herd_id + tag_id
            vals['tag_id'] = tag_id
            vals['serial_number'] = serial
        res = super(NepalDairyIndexAnimal, self).create(vals)
        return res
