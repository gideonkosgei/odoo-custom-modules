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
