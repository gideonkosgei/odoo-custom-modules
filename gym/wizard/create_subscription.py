# -*- coding: utf-8 -*-
from odoo import fields, models, _


class CreateSubscriptionWizard(models.TransientModel):
    _name = "create.subscription.wizard"
    _description = "Create Subscription Wizard"

    member_id = fields.Many2one(comodel_name='gym.member.information', string='Member', required=True)
    start_date = fields.Date('Start Date', required=True)

    preferred_session = fields.Selection([('morning', 'Morning'), ('noon', 'Noon'), ('evening', 'Evening'),
                                          ('other', 'Other')], required=True, default='other')

    notes = fields.Char('Notes')
    mobile = fields.Char('Mobile Number', related='member_id.mobile')
    email = fields.Char('Email', related='member_id.email')
    physical_address = fields.Char('Physical Address', related='member_id.physical_address')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], related='member_id.gender')

    def action_create_subscription(self):
        values = {
            'member_id': self.member_id.id,
            'start_date': self.start_date,
            'preferred_session': self.preferred_session,
            'notes': self.notes,
            'mobile': self.mobile,
            'email': self.email,
            'physical_address': self.physical_address,
            'gender': self.gender
        }

        subscription_rec = self.env["gym.subscription"].create(values)

        return {
            'name': _('Subscriptions'),
            'view_mode': 'form',
            'res_model': 'gym.subscription',
            'res_id': subscription_rec.id,
            'type': 'ir.actions.act_window',
            'target': 'new'
        }

    def action_view_subscriptions(self):
        action = self.env.ref('gym.action_subscriptions').read()[0]
        action['domain'] = [('member_id', '=', self.member_id.id)]

        # below code also works. same as above
        # action = self.env["ir.actions.actions"]._for_xml_id('gym.action_subscriptions')
        # action['domain'] = [('member_id', '=', self.member_id.id)]

        return action
