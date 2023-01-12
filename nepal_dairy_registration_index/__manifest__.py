{
    'name': 'Nepal Dairy Registration Index',
    'version': '1.O.0',
    'summary': 'Nepal Dairy Registration Index',
    'sequence': 10,
    'description': """Nepal Dairy Registration Index""",
    'category': 'Productivity',
    'website': '',
    'license': 'LGPL-3',
    'depends': [
        'mail'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/nepal.dairy.index.list.csv',
        'data/nepal.dairy.index.list.item.csv',
        'data/nepal.dairy.index.breed.csv',
        'data/nepal.dairy.index.province.csv',
        'data/nepal.dairy.index.district.csv',
        'data/nepal.dairy.index.municipality.csv',
        'data/nepal.dairy.index.ward.csv',
        'views/list.xml',
        'views/list_item.xml',
        'views/breed.xml',
        'views/province.xml',
        'views/district.xml',
        'views/municipality.xml',
        'views/ward.xml',
        'views/menu.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False
}
