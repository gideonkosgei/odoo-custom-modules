# -*- coding: utf-8 -*-
from odoo import fields, models


class NepalDairyIndexWard(models.Model):
    _name = "nepal.dairy.index.ward"
    _description = "Ward"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "id"
    _rec_name = "ward_name"

    province_id = fields.Many2one(comodel_name='nepal.dairy.index.province', string='Province', required=True,
                                  tracking=True)
    district_id = fields.Many2one(comodel_name='nepal.dairy.index.district', string='District', required=True,
                                  tracking=True, domain="[('province_id', '=', province_id)]")
    municipality_id = fields.Many2one(comodel_name='nepal.dairy.index.municipality', string='Municipality',
                                      required=True, tracking=True, domain="[('district_id', '=', district_id)]")
    ward_code = fields.Char('Ward Code', required=True, tracking=True)
    ward_name = fields.Char('Ward Name', required=True, tracking=True)




