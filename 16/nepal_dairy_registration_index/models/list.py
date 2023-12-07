# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class NepalDairyIndexList(models.Model):
    _name = "nepal.dairy.index.list"
    _description = "List"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "id"
    _rec_name = "list_name"

    list_name = fields.Char('List Name', required=True, tracking=True)
    list_description = fields.Text('List Description', tracking=True)
    list_item_ids = fields.One2many('nepal.dairy.index.list.item', 'list_id', string='List Item')











