'''send messages to slack channel module'''
import json
import sys
import random
import requests


if __name__ == '__main__':
    URL = "<slack-channel-url>"
    MESSAGE = ("A Sample Message")
    title = (f"New Incoming Message :zap:")
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
                        "value": MESSAGE,
                        "short": "false",
                    }
                ]
            }
        ]
    }
    BYTE_LENGH = str(sys.getsizeof(slack_data))
    headers = {'Content-Type': "application/json", 'Content-Length': BYTE_LENGH}
    response = requests.post(URL, data=json.dumps(slack_data), headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
