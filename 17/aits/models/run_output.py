# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class AitsRunLog(models.Model):
    _name = "aits.run.output"
    _description = "Animal ID"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "id"
    _rec_name = "animal_id"

    run_id = fields.Many2one(comodel_name='aits.run.log', string='Run', tracking=True, required=True)
    index = fields.Char('Index', tracking=True, required=True)
    check_digit = fields.Char('Check Digit', tracking=True, required=True)
    animal_tag_id = fields.Char('Tag ID', tracking=True, required=True)
    animal_id = fields.Char('Animal ID', tracking=True, required=True)
    animal_id_part_1 = fields.Char('Animal ID Part 1', compute='_compute_animal_id_split', store=True)
    animal_id_part_2 = fields.Char('Animal ID Part 2', compute='_compute_animal_id_split', store=True)
    province = fields.Char('Province', related='run_id.province')
    province_code = fields.Integer('Province Code', related='run_id.province_code')
    species = fields.Char('Species', related='run_id.species',store = True)
    species_code = fields.Integer('Species Code', related='run_id.species_code')
    batch_serial = fields.Char('Batch Serial', related='run_id.batch_serial')
    state = fields.Selection('Status', related='run_id.state', store = True)

    @api.depends('animal_id')
    def _compute_animal_id_split(self):
        for record in self:
            if record.animal_id:
                record.animal_id_part_1 = record.animal_id[:6]
                record.animal_id_part_2 = record.animal_id[-6:]
            else:
                record.animal_id_part_1 = False
                record.animal_id_part_2 = False















