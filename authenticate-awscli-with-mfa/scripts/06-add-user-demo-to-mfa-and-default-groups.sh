#!/bin/bash


# add user to group
aws iam add-user-to-group --user-name demo-user --group-name users-default

# add user to group
aws iam add-user-to-group --user-name demo-user --group-name users-mfa
