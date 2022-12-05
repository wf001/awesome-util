# awesome-util
awsome-util is useful toolkit for aws. 

This contains:

- [Send cost report](https://github.com/wf001/awesome-util/tree/main/ce#send-cost-report)
	- Query for aggegated data such as total daily usage and email it via AWS SNS. Runs on Lambda.
- [Export logs to S3](https://github.com/wf001/awesome-util/tree/main/logs#export-logs-to-s3)
	-	Export logs in CloudWatch logs to S3 based on parameters. Runs on Lambda.
- [Move newly created S3 object](https://github.com/wf001/awesome-util/tree/main/s3#move-newly-created-s3-object)
	- Move newly created object in S3 to specified location. Notified by S3, runs on Lambda.
- [Create Item on DynamoDB](https://github.com/wf001/awesome-util/tree/main/dynamo#create-item-on-dynamodb)
	- Create Item on DynamoDB. Runs on local Python.
- [Enable to switch role with CLI](https://github.com/wf001/awesome-util/tree/main/ssm#enable-to-switch-role-with-cli)
	- Set AWS Credentails in environment variable, enable to switch role
