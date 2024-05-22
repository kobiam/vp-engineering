#!/bin/bash


# attach policy to users-mfa
aws iam attach-group-policy --policy-arn arn:aws:iam::aws:policy/IAMReadOnlyAccess --group-name users-default

# attach policy to users-mfa
aws iam attach-group-policy --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess --group-name users-default

# attach policy to users-mfa
aws iam attach-group-policy --policy-arn arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess --group-name users-default
