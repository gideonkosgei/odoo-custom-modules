{
    'name': 'Animal Health ',
    'version': '1.O.0',
    'summary': 'Animal Health Module',
    'sequence': 10,
    'description': """Animal & Human Health Module""",
    'category': 'Productivity',
    'website': '',
    'license': 'LGPL-3',
    'depends': [
        'mail'
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/security_access.xml',
        'data/config_catalogue_data.xml',
        'data/config_catalogue_item_data.xml',
        'data/health.country.csv',
        # 'data/health.admin.unit.level.one.csv',
        # 'data/health.admin.unit.level.two.csv',
        # 'data/health.admin.unit.level.three.csv',
        # 'data/health.admin.unit.level.four.csv',
        'data/health.breed.csv',
        'views/config_catalogue.xml',
        'views/config_catalogue_item.xml',
        'views/animal.xml',
        'views/farmer.xml',
        'views/country.xml',
        'views/breed.xml',
        'views/admin_unit_level_one.xml',
        'views/admin_unit_level_two.xml',
        'views/admin_unit_level_three.xml',
        'views/admin_unit_level_four.xml',
        'views/odk_submission.xml',
        'views/odk_user.xml',
        'views/menu.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False

}
