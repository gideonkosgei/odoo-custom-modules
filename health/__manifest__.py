{
    'name': 'Health ',
    'version': '1.O.0',
    'summary': 'Animal & Human Health',
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
        'data/config_catalogue_data.xml',
        'data/config_catalogue_item_data.xml',
        'data/health.country.csv',
        'views/config_catalogue.xml',
        'views/config_catalogue_item.xml',
        'views/animal.xml',
        'views/farmer.xml',
        'views/country.xml',
        'views/admin_unit_level_one.xml',
        'views/admin_unit_level_two.xml',
        'views/admin_unit_level_three.xml',
        'views/admin_unit_level_four.xml',
        'views/odk_submission.xml',
        'views/menu.xml'

    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False

}
