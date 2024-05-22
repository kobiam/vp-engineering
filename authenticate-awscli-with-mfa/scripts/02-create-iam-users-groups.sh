#!/bin/bash


# create group users-default
aws iam create-group --group-name users-default

# create group users-mfa
aws iam create-group --group-name users-mfa
