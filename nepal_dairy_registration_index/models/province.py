# -*- coding: utf-8 -*-
from odoo import fields, models


class NepalDairyIndexProvince(models.Model):
    _name = "nepal.dairy.index.province"
    _description = "Province"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "id"
    _rec_name = "province_name"

    province_code = fields.Char('Province Code', required=True, tracking=True)
    province_name = fields.Char('Province Name', required=True, tracking=True)
    province_abbreviation = fields.Char('Abbreviation', tracking=True)
    district_count = fields.Integer('District Count', compute='_compute_district_count')
    municipality_count = fields.Integer('Municipality Count', compute='_compute_municipality_count')
    ward_count = fields.Integer('Word Count', compute='_compute_ward_count')

    def _compute_district_count(self):
        for rec in self:
            district_count = self.env['nepal.dairy.index.district'].search_count([('province_id', '=', rec.id)])
            rec.district_count = district_count

    def _compute_municipality_count(self):
        for rec in self:
            municipality_count = self.env['nepal.dairy.index.municipality'].search_count([('province_id', '=', rec.id)])
            rec.municipality_count = municipality_count

    def _compute_ward_count(self):
        for rec in self:
            ward_count = self.env['nepal.dairy.index.ward'].search_count([('province_id', '=', rec.id)])
            rec.ward_count = ward_count

    def action_open_districts_from_province(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Districts',
            'res_model': 'nepal.dairy.index.district',
            'domain': [("province_id", "=", self.id)],
            # 'context': {"default_member_id": self.id},
            'view_mode': 'tree,form',
            'target': 'current'
        }

    def action_open_municipalities_from_province(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Municipalities',
            'res_model': 'nepal.dairy.index.municipality',
            'domain': [("province_id", "=", self.id)],
            # 'context': {"default_member_id": self.id},
            'view_mode': 'tree,form',
            'target': 'current'
        }

    def action_open_wards_from_province(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Wards',
            'res_model': 'nepal.dairy.index.ward',
            'domain': [("province_id", "=", self.id)],
            # 'context': {"default_member_id": self.id},
            'view_mode': 'tree,form',
            'target': 'current'
        }
