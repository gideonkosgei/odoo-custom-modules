# -*- coding: utf-8 -*-
from odoo import fields, models


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

        self.env["gym.subscription"].create(values)
