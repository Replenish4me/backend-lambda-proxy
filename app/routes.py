import os

from . import mocked

routes = {
    '/create-user': {
        'function_name': f'create-user-{os.environ.get("ENVIRONMENT", "dev")}',
        'requires_auth': False,
    },
    '/login': {
        'function_name': f'login-{os.environ.get("ENVIRONMENT", "dev")}',
        'requires_auth': False,
    },
    '/retrieve-password': {
        'function_name': f'retrieve-password-{os.environ.get("ENVIRONMENT", "dev")}',
        'requires_auth': False,
    },
    '/update-user': {
        'function_name': f'update-user-{os.environ.get("ENVIRONMENT", "dev")}',
        'requires_auth': True,
    },
    '/get-user-details': {
        'function_name': f'get-user-details-{os.environ.get("ENVIRONMENT", "dev")}',
        'requires_auth': True,
    },
    '/get-products': {
        'function_name': f'get-products-{os.environ.get("ENVIRONMENT", "dev")}',
        'requires_auth': True,
    },
    '/add-to-cart': {
        'function_name': f'add-to-cart-{os.environ.get("ENVIRONMENT", "dev")}',
        'requires_auth': True,
    },
    '/get-cart': {
        'function_name': f'get-cart-{os.environ.get("ENVIRONMENT", "dev")}',
        'requires_auth': True,
    },
    '/remove-from-cart': {
        'function_name': f'remove-from-cart-{os.environ.get("ENVIRONMENT", "dev")}',
        'requires_auth': True,
    },
    '/remove-one-unity': {
        'function_name': f'remove-one-unity-{os.environ.get("ENVIRONMENT", "dev")}',
        'requires_auth': True,
    },
    '/add-one-unity': {
        'function_name': f'add-one-unity-{os.environ.get("ENVIRONMENT", "dev")}',
        'requires_auth': True,
    },
    '/get-history': {
        'function_name': f'get-history-{os.environ.get("ENVIRONMENT", "dev")}',
        'requires_auth': True,
    },
    '/get-old-purchase': {
        'function_name': f'get-old-purchase-{os.environ.get("ENVIRONMENT", "dev")}',
        'requires_auth': True,
    },
    '/checkout': {
        'function_name': f'checkout-{os.environ.get("ENVIRONMENT", "dev")}',
        'requires_auth': True,
    },
    '/set-delivery-preferences': {
        'function_name': f'set-delivery-preferences-{os.environ.get("ENVIRONMENT", "dev")}',
        'requires_auth': True,
    },
    '/get-delivery-preferences': {
        'function_name': f'get-delivery-preferences-{os.environ.get("ENVIRONMENT", "dev")}',
        'requires_auth': True,
    },
    '/add-credit-card': {
        'function_name': f'add-credit-card-{os.environ.get("ENVIRONMENT", "dev")}',
        'requires_auth': True,
    },
    '/remove-credit-card': {
        'function_name': f'remove-credit-card-{os.environ.get("ENVIRONMENT", "dev")}',
        'requires_auth': True,
    },
    '/get-credit-cards': {
        'function_name': f'get-credit-cards-{os.environ.get("ENVIRONMENT", "dev")}',
        'requires_auth': True,
    },
}