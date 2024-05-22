#!/bin/bash
### to export the vars start the script like this
### . ./awscli-auth-with-mfa.sh

# check if jq is installed
REQUIRED_PACKAGE="jq"
PACKAGE_OK=$(dpkg -s $REQUIRED_PACKAGE|grep "install ok installed")
echo Checking for $REQUIRED_PACKAGE: $PACKAGE_OK
if [ "" = "$PACKAGE_OK" ]; then
    echo "No $REQUIRED_PACKAGE. Please install jq"
    echo "jq is a tool for processing JSON inputs"
    return
fi


# export the default profile to generate tokens
# if you have multiple users modify it instead of default
export AWS_PROFILE=default


echo "Hi, Please add your AWS account id"
read ACCOUNT_ID

echo "Please add your IAM username"
read MFA_USER

echo "Please add your 6-digit code from your authenticator app"
read MFA_TOKEN

TOKEN=$(aws sts get-session-token --duration-seconds 3600 --serial-number arn:aws:iam::$ACCOUNT_ID:mfa/$MFA_USER --token-code $MFA_TOKEN)

# write output to temp json file
echo $TOKEN > temp-token.json

# assign temp creds to vars
TEMP_ACCESS_ID=$(jq -r '.Credentials | .AccessKeyId' temp-token.json)
TEMP_SECRET=$(jq -r '.Credentials | .SecretAccessKey' temp-token.json)
TEMP_TOKEN=$(jq -r '.Credentials | .SessionToken' temp-token.json)

# set temp creds in aws/credentials
aws configure set aws_access_key_id $TEMP_ACCESS_ID --profile mfa
aws configure set aws_secret_access_key $TEMP_SECRET --profile mfa
aws configure set aws_session_token $TEMP_TOKEN --profile mfa

# cleanup
rm temp-token.json

# export mfa profile
export AWS_PROFILE=mfa

echo "Access token is ready! If you need to switch AWS_PROFILE use the script awscli-switch-aws-profile.sh"
echo "default profile is "$AWS_PROFILE
