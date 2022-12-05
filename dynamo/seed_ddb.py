import boto3
import yaml
import json
import os
from functools import cache
import time
import random
import string

DDB_DELETE_INTERVAL = 5
DDB_CREATE_INTERVAL = 10

_env = {
    "DDB_TABLE_NAME": os.getenv("DDB_TABLE_NAME"),
    "DDB_CONFIG_FILE": os.getenv("DDB_CONFIG_FILE"),
}

dynamo = boto3.client("dynamodb")


def create_table():
    ddb_def_yaml = _env["DDB_CONFIG_FILE"]
    with open(ddb_def_yaml, "r", encoding="utf-8") as fp:
        table_config = yaml.safe_load(fp)["Table"]

    dynamo.create_table(
        TableName=_env["DDB_TABLE_NAME"],
        AttributeDefinitions=table_config["AttributeDefinitions"],
        KeySchema=table_config["KeySchema"],
        ProvisionedThroughput=table_config["ProvisionedThroughput"],
    )
    print(f"created {_env['DDB_TABLE_NAME']} table")


def delete_table():
    dynamo.delete_table(TableName=_env["DDB_TABLE_NAME"])
    print(f"deleted {_env['DDB_TABLE_NAME']} table")


def seed():
    with open("data.json") as fp:
        s = json.load(fp)

    # Seed Pattern1; put data from JSON
    for si in s["data"]:
        dynamo.put_item(TableName=_env["DDB_TABLE_NAME"], Item=si)
        print(f"Item {si} created")

    # Seed Pattern2; put data randomly
    for _ in range(2):
        d = {}
        d["type"] = {"S": f"type{random.randint(1, 3)}"}
        d["created_at"] = {"N": str(random.randint(1, 10))}
        d["user"] = {"S": _rand_str(10)}
        dynamo.put_item(TableName=_env["DDB_TABLE_NAME"], Item=d)
        print(f"Item {d} created")


def exists_ddb_table():
    res = _list_table()
    return _env["DDB_TABLE_NAME"] in res["TableNames"]


def _rand_str(digit):
    return "".join(random.choice(string.ascii_letters) for i in range(digit))


@cache
def _list_table():
    res = dynamo.list_tables()
    return res


def main(recreate=False):
    """
    1. Table exists, reacreate flag is True
        - Drop current table, then create new table and put items.
    2. Table exists, reacreate flag is False
        - Without creating new table, put items on current table.
    3. Table not exists, reacreate flag is True
        - Creating new table, then put items on new table.
    4. Table not exists, reacreate flag is False
        - Creating new table, then put items on new table.
    """
    # Recreate table
    if exists_ddb_table() and recreate:
        print(f"{_env['DDB_TABLE_NAME']} already exists")
        delete_table()
        time.sleep(DDB_DELETE_INTERVAL)
        create_table()
        time.sleep(DDB_CREATE_INTERVAL)

    # Create table
    elif not exists_ddb_table():
        print(f"{_env['DDB_TABLE_NAME']} not exists")
        create_table()
        time.sleep(DDB_CREATE_INTERVAL)

    seed()


if __name__ == "__main__":
    main(recreate=False)
