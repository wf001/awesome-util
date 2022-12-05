## Move newly created S3 object
Move newly created object in S3 to specified location. Notified by S3, runs on Lambda.
### Usage
1. Copy and paste rename.py on Lambda editor and deploy it.
2. Set following enviroment variable at Lambda configuration
	- `DEST_KEY_PREFIX`
		- S3 bucket name and key (`bucket-name`/`key-prefix-to-locate`)
3. Set up S3 to send an event to Lambda
	- See [docs](https://docs.aws.amazon.com/lambda/latest/dg/with-s3.html)
