# -*- coding: utf-8 -*-

import base64
import io

from odoo import models


class MemberDetailsXlsx(models.AbstractModel):
    _name = 'report.gym.report_gym_member_details_xls'
    _inherit = 'report.report_xlsx.abstract'

    # data in different sheets
    # def generate_xlsx_report(self, workbook, data, members):
    #     for obj in members:
    #         report_name = obj.first_name
    #         # One sheet by partner
    #         sheet = workbook.add_worksheet(report_name[:31])
    #         bold = workbook.add_format({'bold': True})
    #         sheet.write(0, 0, obj.first_name, bold)

    # data in one sheet
    def generate_xlsx_report(self, workbook, data, members):
        sheet = workbook.add_worksheet("Members")
        bold = workbook.add_format({'bold': True})
        format_1 = workbook.add_format({'bold': True, 'align': 'center', 'bg_color': 'yellow'})
        row = 0
        col = 0

        # Increase column width - many
        # sheet.set_column('A:B', 30)

        # Increase column width - one
        sheet.set_column('A:A', 30)

        for obj in members:
            row += 1
            sheet.merge_range(row, col, row, col + 1, 'Member Details ', format_1)  # merge columns

            if obj.image:
                member_image = io.BytesIO(base64.b64decode(obj.image))
                sheet.insert_image(row, col, "image.png", {'image_data': member_image, 'x_scale': 0.5, 'y_scale': 0.5})
                row += 6

            row += 1
            sheet.write(row, col, 'First Name', bold)
            sheet.write(row, col + 1, obj.first_name)

            row += 1
            sheet.write(row, col, 'Last Name', bold)
            sheet.write(row, col + 1, obj.last_name)

            row += 2  # create a 2 row gap
