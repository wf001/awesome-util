## Enable to switch role with CLI
Set AWS Credentails in environment variable, enable to switch role
### Usage
1. Configure local credentials file as following format
```
[default]
aws_access_key_id = XXXXXXXXXXXXXXXXXXXXXXXXX
aws_secret_access_key = XXXXXXXXXXXXXXXXXXXX
```

2. Create and setup switch role
	- See [docs](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-console.html)
3. Set following environment variables locally
	- `ROLE_ARN`
		- `arn:aws:iam:xxxxxxxxxxx:role/yyyyyyyyy`
	- `ROLE_SESS_NAME`
		- indicate role session name. This script use the role session name to uniquely identify a session when the same role is assumed by different principals or for different reasons. Any formats are available. 

4. Run script as following
```
source get-key.sh
```

5. (Optional) Back to the state before script running
```
source unset-key.sh
```
