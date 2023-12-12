{
    'name': 'Evoucher',
    'version': '1.0.0',
    'summary': 'Evouchers',
    'sequence': 13,
    'description': """Evoucher""",
    'category': 'Productivity',
    'website': '',
    'license': 'LGPL-3',
    'depends': [
        'mail'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/evoucher.staff.csv',
        'report/report.xml',
        'views/staff.xml',
        'views/menu.xml',
        'report/evoucher_cards.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'assets': {
        'web.assets_backend': [
            'evoucher/static/src/scss/event.scss'
        ],
        'web.report_assets_common': [
            '/evoucher/static/src/scss/event_badge_report.scss',
            '/evoucher/static/src/scss/event_full_page_ticket_report.scss',
            '/evoucher/static/src/scss/event_full_page_ticket_responsive_html_report.scss',
        ],
        'web.report_assets_pdf': [
            '/evoucher/static/src/scss/event_full_page_ticket_report_pdf.scss',
        ],
    },
    'application': True,
    'auto_install': False
}
