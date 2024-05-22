#!/bin/bash
### to export the vars start the script like this
### . ./awscli-switch-aws-profile.sh

echo "Hi, What aws profile you need?"
read MFA_PROFILE_INPUT

# export mfa as default
export AWS_PROFILE=$MFA_PROFILE_INPUT

echo "The default profile is "$AWS_PROFILE
