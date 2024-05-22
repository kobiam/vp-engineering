#!/bin/bash


# create policy-allow-users-manage-keys
aws iam create-policy --policy-name policy-allow-users-manage-keys --policy-document file://policy-allow-users-manage-keys.json

# create policy-users-mfa
aws iam create-policy --policy-name policy-users-mfa --policy-document file://policy-users-mfa.json
