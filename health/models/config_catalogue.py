# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class HealthConfigCatalogue(models.Model):
    _name = "health.config.catalogue"
    _description = "Catalogue"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "id"
    _rec_name = "catalogue_name"

    catalogue_name = fields.Char('Catalogue Name', required=True, tracking=True)
    catalogue_description = fields.Text('Catalogue Description', tracking=True)
    catalogue_item_ids = fields.One2many('health.config.catalogue.item', 'catalogue_id', string='Catalog Item')










