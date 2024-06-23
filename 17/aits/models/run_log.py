# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
import re


class AitsRunLog(models.Model):
    _name = "aits.run.log"
    _description = "Batch"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "id"
    _rec_name = "batch_serial"

    batch_serial = fields.Char(string="Batch Serial", required=True, copy=False, readonly=True, index=True,
                               default=lambda self: _("New Batch"))
    species_id = fields.Many2one(comodel_name='nepal.dairy.index.list.item', string='Species', tracking=True,
                                 required=True, domain="[('list_id', '=',1),('item_is_active', '=',True)]")
    province_id = fields.Many2one(comodel_name='nepal.dairy.index.province', string='Province', required=True,
                                  tracking=True)
    quantity = fields.Integer('Quantity', tracking=True, required=True)
    is_saved = fields.Boolean(string='Is Saved', compute='_compute_is_saved')
    state = fields.Selection(
        [('draft', 'Draft'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled'), ('not_printed', 'Unprinted'),
         ('printed', 'Printed')],
        default='draft',
        string='Status', tracking=True)

    province_code = fields.Integer('Province Code', related='province_id.province_code', tracking=True)
    province = fields.Char('Province', related='province_id.province_name')
    species_code = fields.Integer('Species Code', related='species_id.item_code', tracking=True)
    species = fields.Char('Species', related='species_id.item_name', tracking=True)
    run_ids = fields.One2many('aits.run.output', 'run_id', string='Output')
    create_uid = fields.Many2one('res.users', string='Created By', readonly=True)
    creator_name = fields.Char(string='Creator', compute='_compute_creator_name', store=True)
    order_by = fields.Char('Order By', tracking=True, required=True)
    order_date = fields.Date('Order Date', tracking=True, required=True)
    email = fields.Char('Email', tracking=True, required=False)
    phone_number = fields.Char('Phone Number', tracking=True, required=True)
    letter_of_order = fields.Binary(string="Letter Of Order", required=True)
    letter_of_order_name = fields.Char(string="Document Name")

    @api.constrains('quantity')
    def _check_quantity(self):
        for record in self:
            if record.quantity < 1:
                raise ValidationError("Quantity must be at least 1.")

    @api.constrains('phone_number')
    def _check_phone_number(self):
        pattern = re.compile(r'^(?:\+977[- ]?)?(98\d{8})$')
        for record in self:
            if not pattern.match(record.phone_number):
                raise ValidationError("Phone number must be a valid Nepal phone number (e.g., +977-98XXXXXXXX).")

    @api.constrains('email')
    def _check_email_format(self):
        for record in self:
            if record.email:
                if not re.match(r"[^@]+@[^@]+\.[^@]+", record.email):
                    raise ValidationError("Invalid email address: %s" % record.email)

    @api.constrains('order_date')
    def _check_future_date(self):
        for record in self:
            if record.order_date and record.order_date > fields.Date.today():
                raise ValidationError("Future dates are not allowed!")

    @api.constrains('letter_of_order')
    def _check_file_extension(self):
        allowed_extensions = ['pdf', 'docx', 'doc']
        for record in self:
            if record.letter_of_order:
                file_extension = record.letter_of_order_name.split('.')[-1]
                if file_extension not in allowed_extensions:
                    raise ValidationError("Only PDF and Word documents are allowed.")

    @api.model
    def create(self, vals):
        # Create the log
        vals['state'] = 'not_printed'

        if vals.get('batch_serial', _('New Batch')) == _('New Batch'):
            vals['batch_serial'] = self.env['ir.sequence'].next_by_code('aits.run.log.sequence') or _('New Patient')

        res = super(AitsRunLog, self).create(vals)

        species = res.species_code
        province = res.province_code

        # Generate IDs based on quantity
        for i in range(res.quantity):
            # Create the run output record
            idx = self.env['ir.sequence'].next_by_code('aits.run.output')
            padded_idx = idx.zfill(9)

            idx_1 = int(padded_idx[0])
            idx_2 = int(padded_idx[1])
            idx_3 = int(padded_idx[2])
            idx_4 = int(padded_idx[3])
            idx_5 = int(padded_idx[4])
            idx_6 = int(padded_idx[5])
            idx_7 = int(padded_idx[6])
            idx_8 = int(padded_idx[7])
            idx_9 = int(padded_idx[8])

            a = ((species * 11) + (province * 10) + (idx_1 * 9) + (idx_2 * 8) + (idx_3 * 7) + (idx_4 * 6) + (
                        idx_5 * 5) + (idx_6 * 4) + (idx_7 * 3) + (idx_8 * 2) + + (idx_9 * 1)) / 9

            check_digit = "0"

            # Extracting the decimal part
            a_decimal = a - int(a)

            # Converting the decimal part to a string
            decimal_string = str(a_decimal)

            # Remove leading zero if it exists
            if decimal_string.startswith("0"):
                decimal_string = decimal_string[1:]

            # Check if the string has at least 3 characters after the decimal point
            if len(decimal_string) >= 3:
                # Extracting the third digit after the decimal point
                check_digit = decimal_string[2]

            animal_tag_id = str(idx_1) + str(idx_2) + str(idx_3) + str(idx_4) + str(idx_5) + str(idx_6) + str(
                idx_7) + str(idx_8) + str(idx_9) + str(check_digit)
            animal_id = str(species) + str(province)  + str(animal_tag_id)

            self.env['aits.run.output'].create({
                'run_id': res.id,
                'index': idx,
                'check_digit': check_digit,
                'animal_tag_id': animal_tag_id,
                'animal_id': animal_id,
            })

        return res

    @api.depends('create_uid')
    def _compute_is_saved(self):
        for record in self:
            record.is_saved = bool(record.create_uid)

    def action_print_batch(self):
        for rec in self:
            rec.state = 'printed'

    def action_unprint_batch(self):
        for rec in self:
            rec.state = 'not_printed'

    def action_cancel_batch(self):
        for rec in self:
            rec.state = 'cancelled'

    def action_restore_batch(self):
        for rec in self:
            rec.state = 'not_printed'

    @api.depends('create_uid')
    def _compute_creator_name(self):
        for record in self:
            if record.create_uid:
                record.creator_name = record.create_uid.name
            else:
                record.creator_name = ''
