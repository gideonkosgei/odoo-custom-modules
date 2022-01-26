# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class GymSubscription(models.Model):
    _name = "gym.subscription"
    _description = "Gym  Subscription"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _rec_name = "subscription_number"

    member_id = fields.Many2one(comodel_name='gym.member.information', string='Member', tracking=True)
    subscription_number = fields.Char('Subscription Number', required=True, copy=False, readonly=True,
                                      default=lambda self: _('New'))
    start_date = fields.Datetime('Start date', required=True, tracking=True)
    preferred_session = fields.Selection(
        [('morning', 'Morning'), ('noon', 'Noon'), ('evening', 'Evening'),
         ('other', 'Other')], required=True, default='other', tracking=True)
    notes = fields.Char('Notes', tracking=True)
    state = fields.Selection(
        [('draft', 'Draft'), ('confirmed', 'Confirmed'), ('done', 'Done'), ('cancelled', 'Cancelled')], default='draft',
        string='Status', tracking=True)

    mobile = fields.Char('Mobile Number', related='member_id.mobile', tracking=True)
    email = fields.Char('Email', related='member_id.email', tracking=True)
    physical_address = fields.Char('Physical Address', related='member_id.physical_address', tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], required=True
                              , tracking=True)

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirmed'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancelled(self):
        for rec in self:
            rec.state = 'cancelled'

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_url(self):
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': 'https://app.asana.com/0/home/1165647132098783'
        }

    # Override default create method
    @api.model
    def create(self, vals):
        if vals.get('subscription_number', _('New')) == _('New'):
            vals['subscription_number'] = self.env['ir.sequence'].next_by_code('gym.subscription') or _('New')
        res = super(GymSubscription, self).create(vals)
        return res

    @api.onchange('member_id')
    def onchange_member_id(self):
        if self.member_id:
            if self.member_id.gender:
                self.gender = self.member_id.gender
            else:
                self.gender = ''

    def unlink(self):
        print('----------------------deleting--------------------')
        if self.state == "done":
            raise ValidationError("You cannot delete %s as it is in done state" % self.subscription_number)
        return super(GymSubscription, self).unlink()
