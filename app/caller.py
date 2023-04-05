from typing import Dict, Any
import json

import boto3

def call_lambda(name: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """Call a lambda function and return its response."""
    client = boto3.client('lambda')
    response = client.invoke(
        FunctionName=name,
        InvocationType='RequestResponse',
        Payload=json.dumps(payload).encode('utf-8'),
    )
    return json.loads(response['Payload'].read().decode('utf-8'))