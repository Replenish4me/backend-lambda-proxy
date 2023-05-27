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
    },
    '/add-to-cart': {
        'versions': {
            'v1': {
                'function_name': f'add-to-cart-{os.environ.get("env", "dev")}',
            }
        },
        'requires_auth': True,
        'required_params': ['produto_id', 'quantidade'],
    },
    '/remove-one-unity': {
        'versions': {
            'v1': {
                'function_name': f'remove-one-unity-{os.environ.get("env", "dev")}',
            }
        },
        'requires_auth': True,
        'required_params': ['produto_id'],
    },
    '/update-preferences': {
        'versions': {
            'v1': {
                'function_name': f'update-preferences-{os.environ.get("env", "dev")}',
            }
        },
        'requires_auth': True,
        'required_params': ['preferencias'], # aprovar_automaticamente, frequencia, dia_semana
    },
    '/preferences': {
        'versions': {
            'v1': {
                'function_name': f'get-preferences-{os.environ.get("env", "dev")}',
            }
        },
        'requires_auth': True,
        'required_params': [],
    },
    '/remove-reader': {
        'versions': {
            'v1': {
                'function_name': f'remove-reader-{os.environ.get("env", "dev")}',
            }
        },
        'requires_auth': True,
        'required_params': ['leitor_id'],
    },
    '/reders': {
        'versions': {
            'v1': {
                'function_name': f'list-readers-{os.environ.get("env", "dev")}',
            }
        },
        'requires_auth': True,
        'required_params': [],
    },
    '/add-reader': {
        'versions': {
            'v1': {
                'function_name': f'add-reader-{os.environ.get("env", "dev")}',
            }
        },
        'requires_auth': True,
        'required_params': ['leitor_id'],
    },
    '/checkout': {
        'versions': {
            'v1': {
                'function_name': f'confirm-purchase-{os.environ.get("env", "dev")}',
            }
        },
        'requires_auth': True,
        'required_params': [],
    },
    '/remove-from-cart': {
        'versions': {
            'v1': {
                'function_name': f'remove-from-cart-{os.environ.get("env", "dev")}',
            }
        },
        'requires_auth': True,
        'required_params': ['produto_id'],
    },
}