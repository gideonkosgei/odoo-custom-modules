# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class NepalDairyIndexFarmer(models.Model):
    _name = "nepal.dairy.index.farmer"
    _description = "Herd"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "id desc"
    _rec_name = "farmer_name"

    farmer_name = fields.Char('Herd Name', required=True, tracking=True)
    image = fields.Binary(string='farmer Photo')
    farmer_type = fields.Many2one(comodel_name='nepal.dairy.index.list.item', string='Category', tracking=True,
                                  required=True, domain="[('list_id', '=',3)]")
    mobile = fields.Char('Mobile', required=True, tracking=True)
    herd_prefix = fields.Char('Herd Prefix', required=False, tracking=True)
    herd_id = fields.Char('Herd ID', required=True, tracking=True, readonly=True,
                          default=lambda self: _('New'))
    serial_number = fields.Integer('Serial No', tracking=True, required=True)
    province_id = fields.Many2one(comodel_name='nepal.dairy.index.province', string='Province', required=True,
                                  tracking=True)
    district_id = fields.Many2one(comodel_name='nepal.dairy.index.district', string='District', required=True,
                                  tracking=True, domain="[('province_id', '=', province_id)]")
    municipality_id = fields.Many2one(comodel_name='nepal.dairy.index.municipality', string='Municipality',
                                      required=True, tracking=True, domain="[('district_id', '=', district_id)]")
    ward_id = fields.Many2one(comodel_name='nepal.dairy.index.ward', string='Ward',
                              required=True, tracking=True, domain="[('district_id', '=', district_id)]")
    animal_count = fields.Integer('Animal Count', compute='_compute_animal_count')
    animal_ids = fields.One2many('nepal.dairy.index.animal', 'farmer_id', string='Farmer')

    province = fields.Char('Province', related='province_id.province_name', tracking=True)
    province_code = fields.Char('Province Code', related='province_id.province_code', tracking=True)
    province_abbreviation = fields.Char('Province Abbreviation', related='province_id.province_abbreviation',
                                        tracking=True)

    district = fields.Char('District', related='district_id.district_name', tracking=True)
    district_code = fields.Char('District Code', related='district_id.district_code', tracking=True)

    municipality = fields.Char('Municipality', related='municipality_id.municipality_name', tracking=True)
    municipality_code = fields.Char('Municipality Code', related='municipality_id.municipality_code', tracking=True)

    ward = fields.Char('Ward', related='ward_id.ward_name', tracking=True)
    ward_code = fields.Char('Ward Code', related='ward_id.ward_code', tracking=True)
    tole = fields.Char('Tole', tracking=True)
    longitude = fields.Float('Longitude', digits=(8, 5), tracking=True)
    latitude = fields.Float('Latitude', digits=(8, 5), tracking=True)

    destination_herd_ids = fields.One2many('nepal.dairy.index.movement', 'destination_herd_id',
                                           string='Destination Herd')
    origin_herd_ids = fields.One2many('nepal.dairy.index.movement', 'origin_herd_id',
                                      string='Origin Herd')

    _sql_constraints = [('herd_id_unique', 'unique (herd_id)', 'Herd ID Already Exists')]

    @api.model
    def create(self, vals):
        province_id = vals.get('province_id')
        if province_id:
            province_code = self.env['nepal.dairy.index.province'].search([("id", "=", province_id)]).province_code
        else:
            raise ValidationError("Error Fetching Province Code")

        district_id = vals.get('district_id')
        if district_id:
            district_code = self.env['nepal.dairy.index.district'].search(
                [("id", "=", district_id)]).district_code.zfill(2)
        else:
            raise ValidationError("Error Fetching District Code")

        municipality_id = vals.get('municipality_id')
        if municipality_id:
            municipality_code = self.env['nepal.dairy.index.municipality'].search(
                [("id", "=", municipality_id)]).municipality_code.zfill(2)
        else:
            raise ValidationError("Error Fetching Municipality Code")

        ward_id = vals.get('ward_id')
        if ward_id:
            ward_code = self.env['nepal.dairy.index.ward'].search([("id", "=", ward_id)]).ward_code.zfill(2)
        else:
            raise ValidationError("Error Fetching Ward Code")

        # Generate new serial number -> get the last serial number & increment by 1
        herd_prefix = province_code + district_code + municipality_code + ward_code
        herd_recs = self.env['nepal.dairy.index.farmer'].search([("herd_prefix", "=", herd_prefix)])

        if herd_recs:
            last_serial = max(d.serial_number for d in herd_recs)
            serial = last_serial + 1
        else:
            serial = 1

        if vals.get('herd_id', _('New')) == _('New'):
            vals['herd_prefix'] = herd_prefix
            vals['serial_number'] = serial

            vals['herd_id'] = herd_prefix + str(serial).zfill(3)
        res = super(NepalDairyIndexFarmer, self).create(vals)
        return res

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

    @api.constrains('longitude')
    def _check_longitude(self):
        for record in self:
            if not (-180 <= record.longitude <= 180):
                raise ValidationError(_("Longitude must be between -180 and 180."))

    @api.constrains('latitude')
    def _check_latitude(self):
        for record in self:
            if not (-90 <= record.latitude <= 90):
                raise ValidationError(_("Latitude must be between -90 and 90."))
