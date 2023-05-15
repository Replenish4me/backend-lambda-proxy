import os

routes = {
    '/signup': {
        'function_name': f'create-user-{os.environ.get("env", "dev")}',
        'requires_auth': False,
    },
    '/login': {
        'function_name': f'login-{os.environ.get("env", "dev")}',
        'requires_auth': False,
    },
}