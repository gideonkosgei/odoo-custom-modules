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
        'views/staff.xml',
        'views/menu.xml',
        'report/evoucher_card.xml',
        'report/evoucher_cards.xml',
        'report/report.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False
}
