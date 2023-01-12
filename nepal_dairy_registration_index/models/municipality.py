# -*- coding: utf-8 -*-
from odoo import fields, models


class NepalDairyIndexMunicipality(models.Model):
    _name = "nepal.dairy.index.municipality"
    _description = "Municipality"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "id"
    _rec_name = "municipality_name"

    province_id = fields.Many2one(comodel_name='nepal.dairy.index.province', string='Province', required=True,
                                  tracking=True)
    district_id = fields.Many2one(comodel_name='nepal.dairy.index.district', string='District', required=True,
                                  tracking=True, domain="[('province_id', '=', province_id)]")
    municipality_code = fields.Char('Municipality Code', required=True, tracking=True)
    municipality_name = fields.Char('Municipality Name', required=True, tracking=True)
    ward_count = fields.Integer('Word Count', compute='_compute_ward_count')

    def _compute_ward_count(self):
        for rec in self:
            ward_count = self.env['nepal.dairy.index.ward'].search_count([('municipality_id', '=', rec.id)])
            rec.ward_count = ward_count

    def action_open_wards_from_municipality(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Wards',
            'res_model': 'nepal.dairy.index.ward',
            'domain': [("municipality_id", "=", self.id)],
            # 'context': {"default_member_id": self.id},
            'view_mode': 'tree,form',
            'target': 'current'
        }

