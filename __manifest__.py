{
    'name': 'Vendor Self Service Portal',
    'version': '1.0',
    'category': 'services',
    'description': "Vendor Self-Service Portal for Fatmug Designs and focusing on essential functionalities",
    'depends': ['mail','product','sale'],
    'data': [
        'views/request_submission.xml',
        'views/forecast.xml',
        'security/vendor_self_service_portal_security.xml',
        'views/order_adjustment_request_submission_email.xml',
        'security/ir.model.access.csv',
    ],

    'installable': True,
}