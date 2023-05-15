import os
from typing import Dict, Any
from .routes import routes
from .caller import call_lambda

def lambda_handler(event: Dict[str, Dict[str, Any]], context: Dict[str, Any]):
    req_body = event.get('body') or {}
    query_params = event.get('queryStringParameters') or {}
    req_headers = event.get('headers') or {}
    path = event.get('path') or '/'

    function_name : str = routes.get(path, {}).get('function_name')
    requires_auth : bool = routes.get(path, {}).get('requires_auth')

    if requires_auth:
        response = call_lambda(
            f'validate-session-{os.environ.get("env", "dev")}',
            {'token': req_headers.get('Authorization', '')}
        )
        if response.get('statusCode') != 200:
            return response
    
    print(f'Event: {event}')
    print(f'Request body: {req_body}')
    print(f'Query params: {query_params}')
    print(f'Request headers: {req_headers}')

    # Invoca a função lambda com os dados em um json não aninhado
    response = call_lambda(
        function_name,
        {**req_body, **query_params, **req_headers}
    )

    # Acidiona os headers de resposta caso não existam
    if response.get('headers') is None:
        response['headers'] = {}


    # Adiciona o header de CORS
    response['headers']['Access-Control-Allow-Origin'] = '*'
    response['headers']['Content-Type'] = 'application/json'
    
    return response