# -*- coding: utf-8 -*-
try:
    import qrcode
except ImportError:
    qrcode = None
try:
    import base64
except ImportError:
    base64 = None

from io import BytesIO
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError


class NepalDairyIndexAnimal(models.Model):
    _name = "nepal.dairy.index.animal"
    _description = "Animal"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "id desc"
    _rec_name = "animal_id"

    farmer_id = fields.Many2one(comodel_name='nepal.dairy.index.farmer', string='Herd', tracking=True, required=True)
    herd_name = fields.Char('Herd', related='farmer_id.farmer_name')

    species_id = fields.Many2one(comodel_name='nepal.dairy.index.list.item', string='Species', tracking=True,
                                 required=True, domain="[('list_id', '=',2)]")
    species = fields.Char('Species', related='species_id.item_name')

    sex_id = fields.Many2one(comodel_name='nepal.dairy.index.list.item', string='Sex', tracking=True,
                             required=True, domain="[('list_id', '=',1)]")
    sex = fields.Char('Sex', related='sex_id.item_name')

    breed_id = fields.Many2one(comodel_name='nepal.dairy.index.breed', string='Breed',
                               tracking=True, domain="[('species_id', '=', species_id)]")
    breed = fields.Char('Breed', related='breed_id.breed_name')

    animal_dob = fields.Date('Birth Date', tracking=True)

    province = fields.Char('Province', related='farmer_id.province')
    province_code = fields.Char('Province Code', related='farmer_id.province_code')

    district = fields.Char('District', related='farmer_id.district')
    district_code = fields.Char('District Code', related='farmer_id.district_code')

    municipality = fields.Char('Municipality', related='farmer_id.municipality')
    municipality_code = fields.Char('Municipality Code', related='farmer_id.municipality_code')

    ward = fields.Char('Ward', related='farmer_id.ward')
    ward_code = fields.Char('Ward Code', related='farmer_id.ward_code')

    herd_id = fields.Char('Herd ID', related='farmer_id.herd_id', tracking=True)
    serial_number = fields.Integer('Serial No', tracking=True, required=True)
    tag_id = fields.Char('Tag ID', tracking=True, required=True, readonly=True,
                         default=lambda self: _('New'))
    animal_id = fields.Char('Animal ID', required=True, tracking=True, readonly=True,
                            default=lambda self: _('New'))
    qr_code = fields.Binary('QRcode', compute="_generate_qr")

    movement_ids = fields.One2many('nepal.dairy.index.movement', 'animal_id', string='Movement')
    exit_ids = fields.One2many('nepal.dairy.index.exit', 'animal_id', string='Exit')

    _sql_constraints = [('animal_id_unique', 'unique (animal_id)', 'A Record Exists With The Same Animal ID')]

    @api.model
    def create(self, vals):
        farm_id = vals.get('farmer_id')
        farm_rec = self.env['nepal.dairy.index.farmer'].search([("id", "=", farm_id)])

        if farm_rec:
            province_code = farm_rec.province_code
            herd_id = farm_rec.herd_id
            # Generate new serial number -> get the last serial number & increment by 1
            animal_rec = self.env['nepal.dairy.index.animal'].search([("province_code", "=", province_code)])
            if animal_rec:
                last_serial = max(d.serial_number for d in animal_rec)
                serial = last_serial + 1
            else:
                serial = 1

        else:
            raise ValidationError("Error In Generating Registration Number. Cannot Retrieve Administrative Codes")

        if vals.get('animal_id', _('New')) == _('New'):
            padded_serial = str(serial).zfill(5)
            tag_id = province_code + padded_serial
            vals['animal_id'] = herd_id + tag_id
            vals['tag_id'] = tag_id
            vals['serial_number'] = serial
        res = super(NepalDairyIndexAnimal, self).create(vals)
        return res

    @api.onchange('species_id')
    def onchange_species_id(self):
        if self.species_id:
            self.breed_id = None

    @api.onchange('farmer_id')
    def onchange_farmer_id(self):
        if self.herd_id and self._origin.farmer_id.id != self.farmer_id.id:
            vals = {
                'origin_herd_id': self._origin.farmer_id.id,
                'destination_herd_id': self.farmer_id.id,
                'animal_id': self._origin.id
            }

            self.env['nepal.dairy.index.movement'].create(vals)

    def _generate_qr(self):
        "method to generate QR code"
        for rec in self:
            if qrcode and base64:
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=3,
                    border=4,
                )
                qr.add_data("Herd: ")
                qr.add_data(rec.herd_name)

                qr.add_data(", Herd ID: ")
                qr.add_data(rec.herd_id)

                qr.add_data(", Animal ID: ")
                qr.add_data(rec.animal_id)

                qr.add_data(", Tag ID: ")
                qr.add_data(rec.tag_id)

                qr.add_data(", DOB: ")
                qr.add_data(rec.animal_dob)

                qr.add_data(", Species: ")
                qr.add_data(rec.species)

                qr.add_data(", Sex: ")
                qr.add_data(rec.sex)

                qr.add_data(", Breed: ")
                qr.add_data(rec.breed)

                qr.add_data(", Province: ")
                qr.add_data(rec.province)

                qr.add_data(", District: ")
                qr.add_data(rec.district)

                qr.add_data(", Municipality: ")
                qr.add_data(rec.municipality)

                qr.add_data(", Ward: ")
                qr.add_data(rec.ward)

                qr.make(fit=True)
                img = qr.make_image()
                temp = BytesIO()
                img.save(temp, format="PNG")
                qr_image = base64.b64encode(temp.getvalue())
                rec.update({'qr_code': qr_image})
            else:
                raise UserError(_('Necessary Requirements To Run This Operation Is Not Satisfied'))
