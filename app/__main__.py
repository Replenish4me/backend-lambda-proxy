from .handler import lambda_handler

event = {
    "resource": "/{proxy+}",
    "path": "/cart",
    "httpMethod": "POST",
    "headers": {
        'Authorization': '14aafb20-88e5-4db9-98dc-9d91d58f77fc'
    },
    "multiValueHeaders": None,
    "queryStringParameters": None,
    "multiValueQueryStringParameters": None,
    "pathParameters": {
        "proxy": "create-user"
    },
    "body": {
        "email": "user@domain.com",
        "senha": "caio1234"
    },
    "stageVariables": None
}

context = {}
response = lambda_handler(event, context)
print(f'Status code: {response.get("statusCode")}')
print(f'Body: {response.get("body")}')
print(f'Headers: {response.get("headers")}')
