# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class HealthConfigCatalogueItem(models.Model):
    _name = "health.config.catalogue.item"
    _description = "Catalogue Item"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "id"
    _rec_name = "item_name"

    catalogue_id = fields.Many2one(comodel_name='health.config.catalogue', string='Catalogue', required=True,
                                   tracking=True)
    item_code = fields.Integer('Item Code', required=True, tracking=True)
    item_name = fields.Char('Item Name', required=True, tracking=True)
    item_is_active = fields.Boolean('Is Item Active?', required=True, tracking=True, default=True)
    item_description = fields.Text('Item Description', tracking=True)





