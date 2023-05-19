import os

routes = {
    '/signup': {
        'versions': {
            'v1': {
                'function_name': f'create-user-{os.environ.get("env", "dev")}',
            }
        },
        'requires_auth': False,
        'required_params': ['email', 'senha', 'endereco', 'nome', 'telefone'],
    },
    '/login': {
        'versions': {
            'v1': {
                'function_name': f'login-{os.environ.get("env", "dev")}',
            }
        },
        'requires_auth': False,
        'required_params': ['email', 'senha'],
    },
    '/cart': {
        'versions': {
            'v1': {
                'function_name': f'get-cart-{os.environ.get("env", "dev")}',
            }
        },
        'requires_auth': True,
        'required_params': [],
    }
}