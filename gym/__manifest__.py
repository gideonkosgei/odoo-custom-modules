{
    'name': 'Gym ',
    'version': '1.O',
    'summary': 'Gym',
    'sequence': 10,
    'description': """Gym System""",
    'category': 'Productivity',
    'website': '',
    'license': 'LGPL-3',
    'depends': [
        'mail',
        'report_xlsx'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'wizard/create_subscription_view.xml',
        'views/members.xml',
        'views/junior_members.xml',
        'views/gender_view_members.xml',
        'views/subscriptions.xml',
        'report/member_details.xml',
        'report/report.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False

}
