{
    'name': 'Evouchers',
    'version': '1.O.0',
    'summary': 'Evouchers',
    'sequence': 13,
    'description': """Evouchers""",
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
        'views/menu.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False
}
