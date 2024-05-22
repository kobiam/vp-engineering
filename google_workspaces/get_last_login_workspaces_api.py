'''get_last_login_workspaces_api module'''
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build


# scope is readonly
flow = InstalledAppFlow.from_client_secrets_file(
            'client_secret.json', 
            scopes=['https://www.googleapis.com/auth/admin.directory.user.readonly']
        )

flow.run_local_server(port=8080, prompt='consent', authorization_prompt_message='')

credentials = flow.credentials

admin = build('admin' , 'directory_v1', credentials=credentials)

# update the email address
USER_KEY = 'email@your-domain.com'

request = admin.users().get(
    USER_KEY=USER_KEY,
    customFieldMask=None,
    projection=None,
    viewType=None)

response = request.execute()

# uncomment if you want to print it to the console
# print(json.dumps(response['lastLoginTime'], sort_keys=True, indent=4))


# writing response to data.json
with open('data.json', 'w') as outfile:
    json.dump(response, outfile, sort_keys=True, indent=4)


with open('data.json') as json_file:
    data = json.load(json_file)
print(data['lastLoginTime'])
