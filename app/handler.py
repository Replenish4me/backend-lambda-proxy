import os
import json
import logging
from typing import Dict, Any
from .routes import routes
from .caller import call_lambda

def lambda_handler(event: Dict[str, Dict[str, Any]], context: Dict[str, Any]):
    req_body = event.get('body') or {}
    query_params = event.get('queryStringParameters') or {}
    req_headers = event.get('headers') or {}
    path = event.get('path') or '/'
    
    logging.info(f'Path: {path}')

    if isinstance(req_body, str):
        req_body = json.loads(req_body)

    function_name : str = routes.get(path, {})['function_name']
    requires_auth : bool = routes.get(path, {})['requires_auth']
    required_params : list = routes.get(path, {})['required_params']

    # Verifica se todos os parâmetros obrigatórios estão presentes
    for param in required_params:
        if req_body.get(param) is None:
            return {
                'statusCode': 400,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Content-Type': 'application/json',
                },
                'body': {
                    'message': f'Parameter {param} is required',
                },
            }

    if requires_auth:
        response = call_lambda(
            f'validate-session-{os.environ.get("env", "dev")}',
            {'token': req_headers.get('Authorization', '')}
        )

        if response.get('headers') is None:
            response['headers'] = {}
        
        response['headers']['Access-Control-Allow-Origin'] = '*'
        response['headers']['Content-Type'] = 'application/json'

        if response.get('statusCode') != 200:
            return response

    # Invoca a função lambda com os dados em um json não aninhado
    response = call_lambda(
        function_name,
        {**req_body, **query_params, **req_headers}
    )

    if 'statusCode' not in response:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json',
            },
            'body': {
                'message': 'Internal server error',
            },
        }

    # Acidiona os headers de resposta caso não existam
    if response.get('headers') is None:
        response['headers'] = {}


    # Adiciona o header de CORS
    response['headers']['Access-Control-Allow-Origin'] = '*'
    response['headers']['Access-Control-Allow-Methods'] = '*'
    response['headers']['Access-Control-Allow-Headers'] = '*'
    response['headers']['Content-Type'] = 'application/json'
    return response