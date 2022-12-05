#!/bin/sh

source ./unset-key.sh

res=$(aws sts assume-role --output text \
    --role-arn $ROLE_ARN \
    --role-session-name $ROLE_SESS_NAME \
    --duration-seconds 900 \
		--query 'Credentials')

AccessKeyId=$(echo $res | cut -f 1 )
SecretAccessKey=$(echo $res | cut -f 3)
SessionToken=$(echo $res | cut -f 4)

echo "AWS ACCESS KEY ID:" $AccessKeyId
echo "AWS SECRET ACCESS KEY: " $SecretAccessKey
echo "AWS SESSION TOKEN: " $SessionToken

export AWS_ACCESS_KEY_ID=$AccessKeyId
export AWS_SECRET_ACCESS_KEY=$SecretAccessKey
export AWS_SESSION_TOKEN=$SessionToken
