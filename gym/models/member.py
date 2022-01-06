# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class GymMemberInformation(models.Model):
    _name = "gym.member.information"
    _description = "Gym Member Information"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _rec_name = 'first_name'

    title = fields.Selection(
        [('mr', 'Mr'), ('ms', 'Ms'), ('mrs', 'Mrs'), ('dr', 'Dr'), ('prof', 'Prof'), ('rev', 'Rev'),
         ('other', 'Other')], required=True, default='other', tracking=True)
    first_name = fields.Char('First Name', required=True, tracking=True)
    middle_name = fields.Char('Middle Name', tracking=True)
    last_name = fields.Char('Last Name', required=True, tracking=True)
    member_number = fields.Char('Member Number', required=True, copy=False, readonly=True,
                                default=lambda self: _('New'))
    date_of_birth = fields.Date('Date Of Birth', required=True, tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], required=True,
                              default='other', tracking=True)
    marital_status = fields.Selection(
        [('married', 'Married'), ('divorced', 'Divorced'), ('single', 'Single'), ('separated', 'separated'),
         ('other', 'Other')], required=True, default='other', tracking=True)
    mobile = fields.Char('Mobile Number', required=True, tracking=True)
    email = fields.Char('Email', required=True, tracking=True)
    physical_address = fields.Char('Physical Address', tracking=True)
    postal_address = fields.Char('Postal Address', tracking=True)
    postal_code = fields.Char('Postal Code', tracking=True)
    city = fields.Char('City', tracking=True)
    country = fields.Selection(
        [('ke', 'Kenya'), ('ug', 'Uganda'), ('tz', 'Tanzania'), ('et', 'Ethiopia'), ('rw', 'Rwanda'),
         ('other', 'Other')], default='other', tracking=True)
    education_level = fields.Selection(
        [('bachelors', 'Bachelors'), ('masters', 'Masters'), ('doctorate', 'Doctorate'), ('A level', 'A level'),
         ('o level', 'O level'), ('other', 'Other')], default='other', tracking=True)
    profession = fields.Char('profession', tracking=True)
    state = fields.Selection(
        [('draft', 'Draft'), ('confirmed', 'Confirmed'), ('done', 'Done'), ('cancelled', 'Cancelled')], default='draft',
        string='Status', tracking=True)
    sponsor_id = fields.Many2one(comodel_name='res.partner', string='Sponsor', tracking=True)
    subscription_count = fields.Integer('Subscription Count', compute='_compute_subscription_count')

    # handles singleton error on tree view
    def _compute_subscription_count(self):
        for rec in self:
            subscription_count = self.env['gym.subscription'].search_count([('member_id', '=', rec.id)])
            rec.subscription_count = subscription_count

    def action_confirm(self):
        self.state = 'confirmed'

    def action_done(self):
        self.state = 'done'

    def action_cancelled(self):
        self.state = 'cancelled'

    def action_draft(self):
        self.state = 'draft'

    # Override default create method
    @api.model
    def create(self, vals):
        # if the profession form value is not set, pass unemployed as the value
        if not vals.get('profession'):
            vals['profession'] = 'Unemployed'

        if vals.get('member_number', _('New')) == _('New'):
            vals['member_number'] = self.env['ir.sequence'].next_by_code('gym.member.information') or _('New')

        res = super(GymMemberInformation, self).create(vals)
        return res

    # override default values
    @api.model
    def default_get(self, fields):
        res = super(GymMemberInformation, self).default_get(fields)
        res['marital_status'] = 'single'
        return res
