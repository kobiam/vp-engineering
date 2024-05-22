#!/bin/bash
set -e


# Name of the cf stack
STACKNAME=<stack-name>

if [ "$#" -ne 2 ]; then
    echo "please supply one argument create-stack || update-stack"
    echo ""
    echo "example: sh create-cf-main-vpc.sh create-stack"
    exit 1
fi

# Upload CF Template
aws s3 cp $STACKNAME.yaml s3://main-cloudformation-templates/

# Update CF Stack
aws cloudformation "$1" --stack-name "$2" --template-url https://s3.amazonaws.com/main-cloudformation-templates/$STACKNAME.yaml