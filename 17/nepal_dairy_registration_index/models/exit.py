# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class NepalDairyIndexMovement(models.Model):
    _name = "nepal.dairy.index.exit"
    _description = "Exit"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "id"
    _rec_name = "animal_id"

    animal_id = fields.Many2one(comodel_name='nepal.dairy.index.animal', string='Animal ID')
    exit_date = fields.Date('Exit Date', tracking=True)
    exit_reason = fields.Many2one(comodel_name='nepal.dairy.index.list.item', string='Exit/Cull Reason',
                                  tracking=True, required=True, domain="[('list_id', '=',5)]")
    remarks = fields.Text('Remarks', tracking=True)

    _sql_constraints = [('animal_id_unique', 'unique (animal_id)', 'A Record Exists With The Same Animal ID')]
