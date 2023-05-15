import os

routes = {
    '/signup': {
        'function_name': f'create-user-{os.environ.get("env", "dev")}',
        'requires_auth': False,
        'required_params': ['email', 'senha', 'endereco', 'nome', 'telefone'],
    },
    '/login': {
        'function_name': f'login-{os.environ.get("env", "dev")}',
        'requires_auth': False,
        'required_params': ['email', 'senha'],
    },
}