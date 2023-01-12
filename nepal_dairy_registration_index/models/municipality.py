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
