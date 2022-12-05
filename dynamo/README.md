## Create Item on DynamoDB
Create Item on DynamoDB. Runs on local Python.
### Usage
1. Set up Python
2. Set following enviroment variable locally
	- `DDB_TABLE_NAME`
	- `DDB_CONFIG_FILE`
		- Location of configuration file which defines DynamoDB key schema.
3. Install dependencies
```
git clone git@github.com:wf001/awesomw-util
pip install -r requirement.txt
cd dynamo
```
4. Run script as following
```
python seed_ddb.py
```
