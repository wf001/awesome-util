## Export logs to S3
Export logs in CloudWatch logs to S3 based on parameters. Runs on Lambda.
### Usage
1. Copy and paste rename.py on Lambda editor and deploy it.
2. Set following enviroment variable at Lambda configuration
	- `LOGS_LOG_STREAM_NAME_PREFIX`
	- `LOGS_LOG_GROUP_NAME`
	- `LOGS_DESTINATION`
		- S3 bucket name to locate exported logs
	- `LOGS_DESTINATION_PREFIX`
		- S3 prefix to locate exported logs
3. Set up event-driven service, such as EventBridge for Lambda.
