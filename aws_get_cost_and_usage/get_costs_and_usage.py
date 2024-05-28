''' get cost and use module '''
# THIS WILL GET THE CURRENT BILLING FROM AWS FOR THE CURRENT MONTH
# pip3 install boto3
# pip3 install termcolor

import sys
import json
import boto3
import random
import pprint
import requests
from datetime import date
from termcolor import colored


# get today's date
today = date.today()
# get current month
month = today.strftime("%Y-%m-01")
client = boto3.client('ce', region_name='us-east-1')


def cost_usage_amount():
    ''' Get the current billing amount '''
    response = client.get_cost_and_usage(
        TimePeriod={
            'Start': str(month),
            'End': str(today)
        },
        Granularity='MONTHLY',
        Metrics=[
            'NetUnblendedCost',
        ]
    )

    pretty_dict_str = pprint.pformat(response['ResultsByTime'][0]['Total']['NetUnblendedCost']['Amount'])

    global amount_output
    # This removes the ' at the start of the string amount and removes after the float .
    amount_output = pretty_dict_str[1:pretty_dict_str.index('.')]
    return 'The current billing amount for all 4 accounts is: $' + colored(amount_output, 'red')


def send_message_to_channel():
    ''' send message to slack channel '''
    global amount_output
    url = "<slack-channel-url>"
    message = ("The current billing amount for all 4 accounts is: $" + amount_output)
    print(message)
    title = (f"New Billing Update :zap:")
    slack_data = {
        "username": "NotificationBot",
        "icon_emoji": ":satellite:",
        #"channel" : "#somerandomcahnnel",
        "attachments": [
            {
                "color": "#9733EE",
                "fields": [
                    {
                        "title": title,
                        "value": message,
                        "short": "false",
                    }
                ]
            }
        ]
    }
    byte_length = str(sys.getsizeof(slack_data))
    headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
    response = requests.post(url, data=json.dumps(slack_data), headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)


if __name__ == '__main__':    
    cost_usage_amount()
    send_message_to_channel()
