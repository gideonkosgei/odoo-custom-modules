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
    _rec_name = "id"

    staff_name = fields.Char('Staff Name', tracking=True, required=True, readonly=True)
    department = fields.Selection(
        [
            ("department", "department"),
            ("Legal", "Legal"),
            ("Finance", "Finance"),
            ("Sustainable Livestock Systems", "Sustainable Livestock Systems"),
            ("People & Organizational Development", "People & Organizational Development"),
            ("Animal and Human Health", "Animal and Human Health"),
            ("Policies, Institutions and Livelihoods", "Policies, Institutions and Livelihoods"),
            ("ILRI Ugadanda", "ILRI Ugadanda"),
            ("Biosciences", "Biosciences"),
            ("Operations-Kenya (Supply chain, Security, Hospitality)",
             "Operations-Kenya (Supply chain, Security, Hospitality)"),
            ("Communications and Knowledge Management", "Communications and Knowledge Management"),
            ("Director Generals Office", "Director Generals Office"),
            ("Internal Audit", "Internal Audit"),
            ("Feed and Forage Development", "Feed and Forage Development"),
            ("ICT", "ICT"),
            ("Hosted Institutions", "Hosted Institutions"),
            ("GENDER Platform", "GENDER Platform"),
            ("Livestock Genetics", "Livestock Genetics"),
            ("Program Management", "Program Management"),
            ("Capacity Development", "Capacity Development"),
            ("Institutional Planning & Partnerships", "Institutional Planning & Partnerships"),
            ("Data and Research Methods Unit", "Data and Research Methods Unit"),
            ("Integrated Science", "Integrated Science"),
            ("Operations-Kenya (Supply chain, Engineering ,Security, Hospitality)",
             "Operations-Kenya (Supply chain, Engineering ,Security, Hospitality)")
        ],
        string='Program/Department', tracking=True, readonly=True)
    diet = fields.Selection([("1", "Vegetarian"), ("2", "Non-Vegetarian")], string='Dietary Preference',
                            tracking=True, readonly=True)
    beverage = fields.Selection([('1', 'Beer'), ('2', 'Wine'), ('3', 'Juice/Soda')], string='Beverage', tracking=True,
                                readonly=True)

    qr_code = fields.Binary('QRcode', compute="_generate_qr")

    token_food = fields.Boolean('Food', tracking=True)
    token_drink = fields.Boolean('Drinks', tracking=True)
    state = fields.Selection([('Open', 'Open'), ('Closed', 'Closed')], string='state', default='Open',
                             compute='_compute_state')

    def _generate_qr(self):
        for rec in self:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=5,
                border=6,
            )

            # base_url = self.env['ir.config_parameter'].get_param('web.base.url')
            base_url= 'http://109.74.196.59:8069'
            qr_data = f'{base_url}/web#id={rec.id}&model=evoucher.staff&view_type=form&cids='
            qr.add_data(qr_data)
            qr.make(fit=True)
            img = qr.make_image()

            # Save QR code image to BytesIO and encode it to base64
            temp = BytesIO()
            img.save(temp, format="PNG")
            qr_image = base64.b64encode(temp.getvalue())
            rec.qr_code = qr_image

    @api.depends('token_food', 'token_drink')
    def _compute_state(self):
        for rec in self:
            if all([rec.token_food, rec.token_drink]):
                rec.state = 'Closed'
            else:
                rec.state = 'Open'
