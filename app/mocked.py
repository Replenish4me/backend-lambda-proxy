# Cria funções mockadas para validação da api

def create_user(event, context):
    req_body = event.get('body') or {}

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*.replenish4.me',
        },
        'body': {
            'message': 'User created successfully',
            'user': {
                'id': 1,
                'username': req_body.get('username'),
                'email': req_body.get('email'),
            }
        }
    }


def login(event, context):
    req_body = event.get('body') or {}

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*.replenish4.me',
        },
        'body': {
            'message': 'Logged in successfully',
            'user': {
                'id': 1,
                'username': req_body.get('username'),
                'email': req_body.get('email'),
            },
            'token': 'token',
        }
    }


def add_to_cart(event, context):
    req_body = event.get('body') or {}

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*.replenish4.me',
        },
        'body': {
            'message': 'Product added to cart successfully',
            'product': {
                'id': 1,
                'name': req_body.get('name'),
                'price': req_body.get('price'),
                'quantity': req_body.get('quantity'),
            }
        }
    }

def get_cart(event, context):
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*.replenish4.me',
        },
        'body': {
            'message': 'Cart retrieved successfully',
            'cart': [
                {
                    'id': 1,
                    'name': 'Product 1',
                    'price': 10,
                    'quantity': 1,
                },
                {
                    'id': 2,
                    'name': 'Product 2',
                    'price': 20,
                    'quantity': 2,
                },
                {
                    'id': 3,
                    'name': 'Product 3',
                    'price': 30,
                    'quantity': 3,
                },
            ]
        }
    }

def remove_from_cart(event, context):
    req_body = event.get('body') or {}

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*.replenish4.me',
        },
        'body': {
            'message': 'Product removed from cart successfully',
            'product': {
                'id': req_body.get('id'),
            }
        }
    }

def remove_one_unity(event, context):
    req_body = event.get('body') or {}

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*.replenish4.me',
        },
        'body': {
            'message': 'Product removed one unity from cart successfully',
            'product': {
                'id': req_body.get('id'),
            }
        }
    }

def add_one_unity(event, context):
    req_body = event.get('body') or {}

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*.replenish4.me',
        },
        'body': {
            'message': 'Product added one unity from cart successfully',
            'product': {
                'id': req_body.get('id'),
            }
        }
    }

def get_history(event, context):
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*.replenish4.me',
        },
        'body': {
            'message': 'History retrieved successfully',
            'history': [
                {
                    'purchaseId': 1,
                },
                {
                    'purchaseId': 2,
                }
            ]
        }
    }


def get_old_purchase(event, context):
    query_params = event.get('queryStringParameters') or {}

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*.replenish4.me',
        },
        'body': {
            'message': 'Old purchase retrieved successfully',
            'purchase': {
                'id': query_params.get('id'),
                'products': [
                    {
                        'id': 1,
                        'name': 'Product 1',
                        'price': 10,
                        'quantity': 1,
                    },
                    {
                        'id': 2,
                        'name': 'Product 2',
                        'price': 20,
                        'quantity': 2,
                    },
                    {
                        'id': 3,
                        'name': 'Product 3',
                        'price': 30,
                        'quantity': 3,
                    },
                ]
            }
        }
    }

def checkout(event, context):
    req_body = event.get('body') or {}

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*.replenish4.me',
        },
        'body': {
            'message': 'Checkout successfully',
            'purchase': {
                'id': 1,
                'products': [
                    {
                        'id': 1,
                        'name': 'Product 1',
                        'price': 10,
                        'quantity': 1,
                    },
                    {
                        'id': 2,
                        'name': 'Product 2',
                        'price': 20,
                        'quantity': 2,
                    },
                    {
                        'id': 3,
                        'name': 'Product 3',
                        'price': 30,
                        'quantity': 3,
                    },
                ],
                'payment_method': req_body.get('payment_method'),
            }
        }
    }

def get_products(event, context):
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*.replenish4.me',
        },
        'body': {
            'message': 'Products retrieved successfully',
            'products': [
                {
                    'id': 1,
                    'name': 'Product 1',
                    'price': 10,
                    'quantity': 1,
                },
                {
                    'id': 2,
                    'name': 'Product 2',
                    'price': 20,
                    'quantity': 2,
                },
                {
                    'id': 3,
                    'name': 'Product 3',
                    'price': 30,
                    'quantity': 3,
                },
            ]
        }
    }

def set_delivery_preferences(event, context):
    req_body = event.get('body') or {}

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*.replenish4.me',
        },
        'body': {
            'message': 'Delivery preferences set successfully',
            'delivery_preferences': {
                'delivery_frequence': req_body.get('delivery_frequence'),
                'delivery_day': req_body.get('delivery_day'),
                'auto_approve': req_body.get('auto_approve'),
            }
        }
    }

def get_delivery_preferences(event, context):
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*.replenish4.me',
        },
        'body': {
            'message': 'Delivery preferences retrieved successfully',
            'delivery_preferences': {
                'delivery_frequence': 'weekly',
                'delivery_day': 'monday',
                'auto_approve': True,
            }
        }
    }

def add_credit_card(event, context):
    req_body = event.get('body') or {}

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*.replenish4.me',
        },
        'body': {
            'message': 'Credit card added successfully',
            'credit_card': {
                'id': 1,
                'number': req_body.get('number'),
                'name': req_body.get('name'),
                'expiration_date': req_body.get('expiration_date'),
                'cvv': req_body.get('cvv'),
            }
        }
    }

def get_credit_cards(event, context):
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*.replenish4.me',
        },
        'body': {
            'message': 'Credit cards retrieved successfully',
            'credit_cards': [
                {
                    'id': 1,
                    'number': '1234 5678 9012 3456',
                    'name': 'John Doe',
                    'expiration_date': '01/2020',
                    'cvv': '123',
                },
                {
                    'id': 2,
                    'number': '1234 5678 9012 3456',
                    'name': 'John Doe',
                    'expiration_date': '01/2020',
                    'cvv': '123',
                },
            ]
        }
    }

def remove_credit_card(event, context):
    query_params = event.get('queryStringParameters') or {}

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*.replenish4.me',
        },
        'body': {
            'message': 'Credit card removed successfully',
            'credit_card': {
                'id': query_params.get('id'),
            }
        }
    }

def get_user_details(event, context):
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*.replenish4.me',
        },
        'body': {
            'message': 'User details retrieved successfully',
            'user': {
                'id': 1,
                'name': 'John Doe',
                'email': 'example@example.com',
            }
        }
    }

def retrieve_password(event, context):
    req_body = event.get('body') or {}

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*.replenish4.me',
        },
        'body': {
            'message': 'Password retrieve email sent',
            'user': {
                'id': 1,
                'name': 'John Doe',
                'email': 'example@example.com',
            }
        }
    }

def update_user(event, context):
    req_body = event.get('body') or {}

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*.replenish4.me',
        },
        'body': {
            'message': 'User updated successfully',
            'user': {
                'id': 1,
                'name': req_body.get('name'),
                'email': req_body.get('email'),
            }
        }
    }


import flask
from app import routes

app = flask.Flask(__name__)

# Create a wildcard route to handle all requests
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api_gw(path):
    func = routes.routes.get('/'+ path).get('mocked')
    response = func({}, None)
    
    return response

if __name__ == '__main__':
    app.run(port='3000')