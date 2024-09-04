''' lambda function crud with dynamodb '''
import boto3

client = boto3.client('dynamodb')
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("items-inventory")

def lambda_handler(event, context):
    ''' crud operations '''

    # put item
    table.put_item(Item= {'items': 'Banana'})
    # get item
    table.get_item(Key={'items': 'Banana'})
    # delete item
    table.delete_item(Key={'items': 'Banana'})
    # get item
    res_get_items = table.get_item(Key={'items': 'Banana'})

    return res_get_items
