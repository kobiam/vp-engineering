''' lambda function PING '''
import json

def lambda_handler(event, context):
    ''' main lambda function '''
    http_method = event.get('httpMethod')

    if http_method == 'GET':
        return {
            'statusCode': 200,
            'body': json.dumps('PING OK')
        }
    else:
        response = {
            'statusCode': 405,
            'body': json.dumps({'message': 'Method Not Allowed'}),
            'headers': {'Content-Type': 'application/json'}
        }

    return response
