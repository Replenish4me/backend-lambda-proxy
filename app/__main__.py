from .handler import lambda_handler

event = {
    'headers': {
        'Content-Type': 'application/json',
    },
    'body': {
        'name': 'John Doe'
    },
    'path': '/create-user',
}

context = {}
response = lambda_handler(event, context)
print(f'Status code: {response["statusCode"]}')
print(f'Body: {response["body"]}')
print(f'Headers: {response["headers"]}')