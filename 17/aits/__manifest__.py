{
    'name': 'AITS',
    'version': '1.0.0',
    'summary': 'Animal Identification and Traceability System',
    'sequence': 14,
    'description': """Animal Identification and Traceability System""",
    'category': 'Productivity',
    'website': '',
    'license': 'LGPL-3',
    'depends': [
        'mail'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'data/nepal.dairy.index.list.csv',
        'data/nepal.dairy.index.list.item.csv',
        'data/nepal.dairy.index.province.csv',
        'report/report.xml',
        'views/list.xml',
        'views/list_item.xml',
        'views/province.xml',
        'views/run_log.xml',
        'views/run_output.xml',
        'views/cattle_tags.xml',
        'views/buffalo_tags.xml',
        'views/menu.xml',
        'report/tags_batches.xml',
        'report/tags_printer_input.xml'

    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'assets': {
        'web.assets_backend': [
            'aits/static/src/scss/event.scss'
        ],
        'web.report_assets_common': [
            '/aits/static/src/scss/event_badge_report.scss',
            '/aits/static/src/scss/event_full_page_ticket_report.scss',
            '/aits/static/src/scss/event_full_page_ticket_responsive_html_report.scss',
        ],
        'web.report_assets_pdf': [
            '/aits/static/src/scss/event_full_page_ticket_report_pdf.scss',
        ],
    },
    'application': True,
    'auto_install': False
}
