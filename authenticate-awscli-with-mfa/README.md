# Authenticate awscli w/ mfa

## scripts folder

create the iam groups and policies via the scripts

```sh
sh 01-create-mfa-policies.sh
sh 02-create-iam-users-groups.sh
sh 03-attach-mfa-policies-to-mfa-group.sh
sh 04-attach-users-policies-to-default-group.sh
sh 05-create-demo-user.sh
sh 06-add-user-demo-to-mfa-and-default-groups.sh
```

## awscli-auth script

use the script to authenticate w/ mfa

```sh
. ./awscli-auth-with-mfa.sh
```

## switch aws profiles

use the script to switch aws profiles

```sh
. ./awscli-switch-aws-profile.sh
```

## awscli authentication requirements using linux

**required packages**

```bash
awscli
jq
```

## tests

those scripts tested on debian
