{
    'name': "My pet (+) - minhng.info",
    'summary': """My pet plus""",
    'description': """Managing pet information""",
    'author': "Vinh PL",
    'website': "https://minhng.info",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'mypet',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/my_pet_plus_views.xml',
        'views/product_pet_views.xml',
        'views/my_pet_view.xml',
    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
    'auto-install': False,
}