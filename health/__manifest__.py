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
        'views/config_catalogue.xml',
        'views/config_catalogue_item.xml',
        'views/menu.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False

}
