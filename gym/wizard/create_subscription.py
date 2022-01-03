# -*- coding: utf-8 -*-
from odoo import fields, models


class CreateSubscriptionWizard(models.TransientModel):
    _name = "create.subscription.wizard"
    _description = "Create Subscription Wizard"

    name = fields.Char('Name', required=True)

    def action_create_subscription(self):
        print('button is clicked')
