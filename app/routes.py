import os

from . import mocked

routes = {
    '/create-user': {
        'function_name': f'create-user-{os.environ.get("ENVIRONMENT", "dev")}',
        'requires_auth': False,
        'mocked': mocked.create_user,
    },
    '/login': {
        'function_name': f'login-{os.environ.get("ENVIRONMENT", "dev")}',
        'requires_auth': False,
        'mocked': mocked.login,
    },
    '/retrieve-password': {
        'function_name': f'retrieve-password-{os.environ.get("ENVIRONMENT", "dev")}',
        'requires_auth': False,
        'mocked': mocked.retrieve_password,
    },
    '/update-user': {
        'function_name': f'update-user-{os.environ.get("ENVIRONMENT", "dev")}',
        'requires_auth': True,
        'mocked': mocked.update_user,
    },
    '/get-user-details': {
        'function_name': f'get-user-details-{os.environ.get("ENVIRONMENT", "dev")}',
        'requires_auth': True,
        'mocked': mocked.get_user_details,
    },
    '/get-products': {
        'function_name': f'get-products-{os.environ.get("ENVIRONMENT", "dev")}',
        'requires_auth': True,
        'mocked': mocked.get_products,
    },
    '/add-to-cart': {
        'function_name': f'add-to-cart-{os.environ.get("ENVIRONMENT", "dev")}',
        'requires_auth': True,
        'mocked': mocked.add_to_cart,
    },
    '/get-cart': {
        'function_name': f'get-cart-{os.environ.get("ENVIRONMENT", "dev")}',
        'requires_auth': True,
        'mocked': mocked.get_cart,
    },
    '/remove-from-cart': {
        'function_name': f'remove-from-cart-{os.environ.get("ENVIRONMENT", "dev")}',
        'requires_auth': True,
        'mocked': mocked.remove_from_cart,
    },
    '/remove-one-unity': {
        'function_name': f'remove-one-unity-{os.environ.get("ENVIRONMENT", "dev")}',
        'requires_auth': True,
        'mocked': mocked.remove_one_unity,
    },
    '/add-one-unity': {
        'function_name': f'add-one-unity-{os.environ.get("ENVIRONMENT", "dev")}',
        'requires_auth': True,
        'mocked': mocked.add_one_unity,
    },
    '/get-history': {
        'function_name': f'get-history-{os.environ.get("ENVIRONMENT", "dev")}',
        'requires_auth': True,
        'mocked': mocked.get_history,
    },
    '/get-old-purchase': {
        'function_name': f'get-old-purchase-{os.environ.get("ENVIRONMENT", "dev")}',
        'requires_auth': True,
        'mocked': mocked.get_old_purchase,
    },
    '/checkout': {
        'function_name': f'checkout-{os.environ.get("ENVIRONMENT", "dev")}',
        'requires_auth': True,
        'mocked': mocked.checkout,
    },
    '/set-delivery-preferences': {
        'function_name': f'set-delivery-preferences-{os.environ.get("ENVIRONMENT", "dev")}',
        'requires_auth': True,
        'mocked': mocked.set_delivery_preferences,
    },
    '/get-delivery-preferences': {
        'function_name': f'get-delivery-preferences-{os.environ.get("ENVIRONMENT", "dev")}',
        'requires_auth': True,
        'mocked': mocked.get_delivery_preferences,
    },
    '/add-credit-card': {
        'function_name': f'add-credit-card-{os.environ.get("ENVIRONMENT", "dev")}',
        'requires_auth': True,
        'mocked': mocked.add_credit_card,
    },
    '/remove-credit-card': {
        'function_name': f'remove-credit-card-{os.environ.get("ENVIRONMENT", "dev")}',
        'requires_auth': True,
        'mocked': mocked.remove_credit_card,
    },
    '/get-credit-cards': {
        'function_name': f'get-credit-cards-{os.environ.get("ENVIRONMENT", "dev")}',
        'requires_auth': True,
        'mocked': mocked.get_credit_cards,
    },
}