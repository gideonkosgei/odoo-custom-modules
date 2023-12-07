# -*- coding: utf-8 -*-
try:
    import qrcode
except ImportError:
    qrcode = None
try:
    import base64
except ImportError:
    base64 = None

from io import BytesIO
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError


class Evoucher(models.Model):
    _name = "evoucher.staff"
    _description = "staff"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "id"
    _rec_name = "staff_name"

    staff_name = fields.Char('Staff Name', tracking=True, required=True, readonly=True)
    department = fields.Selection(
        [("1", "Operation:Supply chain, Engineering, Security, Hospitality"), ("2", "Finance"), ("3", "Biosciences"),
         ("4", "People & Organizational Development"),
         ("5", "Institutional Planning & Partnerships"), ("6", "Policies, Institutions and Livelihoods"),
         ("7", "Animal and Human Health"),
         ("7", "Sustainable Livestock Systems"), ("8", "Director Generals Office"), ("9", "ICT"),
         ("10", "Communications and Knowledge Management"),
         ("11", "Gender Platform"), ("12", "Livestock Genetics"), ("13", "DDG - Biosciences Office"),
         ("14", "Sustainable Livestock Systems"),
         ("15", "Data and Research Methods Unit"), ("16", "Capacity Development"), ("17", "Internal Audit"),
         ("18", "Feed and Forage  Development"),
         ("19", "Legal"), ("20", "Program  Management"), ("21", "Hosted Institutions"), ("22", "Integrated  Science")],
        string='Program/Department', tracking=True, readonly=True)
    diet = fields.Selection([("1", "Vegetarian"), ("2", "Non-vegetarian"), ("3", "Other")], string='Dietary Preference',
                            tracking=True, readonly=True)
    beverage = fields.Selection([('1', 'Beer'), ('2', 'Wine'), ('3', 'Juice/Beer')], string='Beverage', tracking=True,
                                readonly=True)

    qr_code = fields.Binary('QRcode', compute="_generate_qr")

    token_food = fields.Boolean('Food', tracking=True)
    token_drink = fields.Boolean('Drinks', tracking=True)
    state = fields.Selection([('Open', 'Open'), ('Closed', 'Closed')], string='state', default='Open',
                              compute='_compute_state')

    def _generate_qr(self):
        "method to generate QR code"
        for rec in self:
            if qrcode and base64:
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=5,
                    border=6,
                )

                base_url = self.env['ir.config_parameter'].get_param('web.base.url')
                # if not 'localhost' in base_url:
                #     if 'http://' in base_url:
                #         base_url = base_url.replace('http://', 'https://')
                base_url = base_url + '/web#id=' + str(self.id) + '&model=evoucher.staff&view_type=form&cids='
                qr.add_data(base_url)

                qr.make(fit=True)
                img = qr.make_image()
                temp = BytesIO()
                img.save(temp, format="PNG")
                qr_image = base64.b64encode(temp.getvalue())
                rec.update({'qr_code': qr_image})

            else:
                raise UserError(_('Necessary Requirements To Run This Operation Is Not Satisfied'))

    @api.depends('token_food', 'token_drink')
    def _compute_state(self):
        for rec in self:
            if all([rec.token_food, rec.token_drink]):
                rec.state = 'Closed'
            else:
                rec.state = 'Open'
