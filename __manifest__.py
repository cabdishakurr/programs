{
    'name': 'Contact Promotional Program',
    'version': '1.0',
    'category': 'Sales/CRM',
    'summary': 'Manage promotional balances for contacts',
    'description': """
        This module adds promotional program management to contacts with the following features:
        - Track promotional balance for each contact
        - Restricted access based on user roles
        - Admin overview of all promotional balances
    """,
    'depends': ['base', 'contacts'],
    'data': [
        'security/promotional_security.xml',
        'security/ir.model.access.csv',
        'views/promotional_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
} 