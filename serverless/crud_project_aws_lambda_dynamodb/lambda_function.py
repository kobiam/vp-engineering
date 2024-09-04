''' lambda function with api gateway and dynamodb '''
import json
import boto3
from botocore.exceptions import ClientError


dynamodb = boto3.resource('dynamodb')
client = boto3.client('dynamodb')
table = dynamodb.Table('inventory')


def lambda_handler(event, context):
    ''' main lambda func '''
    http_method = event.get('httpMethod')
    path_parameters = event.get('queryStringParameters', {})
    body = event.get('body', '{}')
    response = {}

    if http_method == 'GET':
        response = handle_get(path_parameters)
    elif http_method == 'DELETE':
        response = handle_delete(path_parameters)
    elif http_method == 'POST':
        response = handle_post(body)
    else:
        response = {
            'statusCode': 405,
            'body': json.dumps({'message': 'Method Not Allowed'}),
            'headers': {'Content-Type': 'application/json'}
        }

    return response


def handle_get(path_parameters):
    ''' GET '''
    item_id = path_parameters.get('itemId')
    if not item_id:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'ID is required'}),
            'headers': {'Content-Type': 'application/json'}
        }

    try:
        response = table.get_item(Key={'itemId': item_id})
        item = response.get('Item')
        if item:
            return {
                'statusCode': 200,
                'body': json.dumps(item),
                'headers': {'Content-Type': 'application/json'}
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps({'message': 'Item not found'}),
                'headers': {'Content-Type': 'application/json'}
            }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Error retrieving item', 'error': str(e)}),
            'headers': {'Content-Type': 'application/json'}
        }


def handle_delete(path_parameters):
    ''' DELETE '''
    item_id = path_parameters.get('itemId')
    if not item_id:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'ID is required'}),
            'headers': {'Content-Type': 'application/json'}
        }

    try:
        table.delete_item(Key={'itemId': item_id})
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Item deleted successfully'}),
            'headers': {'Content-Type': 'application/json'}
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Error deleting item', 'error': str(e)}),
            'headers': {'Content-Type': 'application/json'}
        }


def handle_post(body):
    ''' POST '''
    data = json.loads(body)
    item_id = data.get('itemId')
    if not item_id:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'ID is required'}),
            'headers': {'Content-Type': 'application/json'}
        }

    try:
        table.put_item(Item=data)
        return {
            'statusCode': 201,
            'body': json.dumps({'message': 'Item created successfully'}),
            'headers': {'Content-Type': 'application/json'}
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Error creating item', 'error': str(e)}),
            'headers': {'Content-Type': 'application/json'}
        }
