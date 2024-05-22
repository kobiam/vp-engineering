# Get data from G-suite API

## Create virtualenv

`virtualenv env`

## Install Packages

`pip install google-auth google_auth_oauthlib`

## Create quickstart project at the developers console

### Create Credentials

Credentials > OAuth client ID > choose Web application > Add Authorized redirect URIs > `http://localhost:8080` > Download JSON > save it as client_secret.json > put it in the same directory as your code

### Enable Admin SDK

make sure to enable admin SDK
`https://console.developers.google.com/apis/api/admin.googleapis.com`

### Allow G Suite admin - unrestricted

`https://admin.google.com/ac/owl/list?tab=services`

#### Running this API call will open a web browser to login
