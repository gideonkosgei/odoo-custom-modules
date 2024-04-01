# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class NepalDairyIndexListItem(models.Model):
    _name = "nepal.dairy.index.list.item"
    _description = "List Item"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "id"
    _rec_name = "item_name"

    list_id = fields.Many2one(comodel_name='nepal.dairy.index.list', string='List', required=True,
                              tracking=True)
    item_name = fields.Char('Item Name', required=True, tracking=True)
    item_is_active = fields.Boolean('Is Item Active?', required=True, tracking=True, default=True)
    item_description = fields.Text('Item Description', tracking=True)
