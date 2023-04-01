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
        """TODO: Implement authentication"""
    
    response = call_lambda(function_name, event)
    
    return response