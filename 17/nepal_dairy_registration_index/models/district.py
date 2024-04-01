# -*- coding: utf-8 -*-
from odoo import fields, models


class NepalDairyIndexDistrict(models.Model):
    _name = "nepal.dairy.index.district"
    _description = "District"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "id"
    _rec_name = "district_name"

    province_id = fields.Many2one(comodel_name='nepal.dairy.index.province', string='District', required=True,
                                  tracking=True)
    district_code = fields.Char('District Code', required=True, tracking=True)
    district_name = fields.Char('District Name', required=True, tracking=True)
    municipality_count = fields.Integer('Municipality Count', compute='_compute_municipality_count')
    ward_count = fields.Integer('Word Count', compute='_compute_ward_count')

    def _compute_municipality_count(self):
        for rec in self:
            municipality_count = self.env['nepal.dairy.index.municipality'].search_count([('district_id', '=', rec.id)])
            rec.municipality_count = municipality_count

    def _compute_ward_count(self):
        for rec in self:
            ward_count = self.env['nepal.dairy.index.ward'].search_count([('district_id', '=', rec.id)])
            rec.ward_count = ward_count

    def action_open_municipalities_from_district(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Municipalities',
            'res_model': 'nepal.dairy.index.municipality',
            'domain': [("district_id", "=", self.id)],
            # 'context': {"default_member_id": self.id},
            'view_mode': 'tree,form',
            'target': 'current'
        }

    def action_open_wards_from_district(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Wards',
            'res_model': 'nepal.dairy.index.ward',
            'domain': [("district_id", "=", self.id)],
            # 'context': {"default_member_id": self.id},
            'view_mode': 'tree,form',
            'target': 'current'
        }
