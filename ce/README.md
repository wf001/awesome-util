## Send cost report
Query for aggegated data such as total daily usage and email it via AWS SNS. Runs on Lambda.
### Usage
1. Copy and paste send-report.py on Lambda editor and deploy it.
2. Create SNS Topic
3. Set following enviroment variable at lambda configuration
	- `BILLING_TOPIC_ARN`
		- SNS Topic ARN (arn:aws:sns:xxx:yyyy:zzzz)
4. Set up event-driven service, such as EventBridge for Lambda.
