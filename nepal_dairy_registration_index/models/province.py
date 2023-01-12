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



