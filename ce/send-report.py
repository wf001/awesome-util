import boto3
from datetime import datetime
import os

_env = {"topic_arn": os.getenv("BILLING_TOPIC_ARN")}
MAIL_SUBJECT = "AWS Cost"
# cost rounded by specific number
COST_DIGIT = 3
SNS_REGION = "ap-northeast-1"


def lambda_handler(event, context):
    topic_arn = _env["topic_arn"]

    ce = boto3.client("ce", region_name="us-east-1")
    sns = boto3.resource("sns", region_name=SNS_REGION)

    cur = datetime.now()
    year = cur.year
    month = cur.strftime("%m")
    today = cur.strftime("%d")
    start = f"{year}-{month}-01"
    end = f"{year}-{month}-{today}"

    response = ce.get_cost_and_usage(
        TimePeriod={
            "Start": start,
            "End": end,
        },
        Granularity="MONTHLY",
        Metrics=["UnblendedCost"],
    )
    print(response)
    cost = round(
        float(response["ResultsByTime"][0]["Total"]["UnblendedCost"]["Amount"]),
        COST_DIGIT,
    )
    msg = f"{cost} USD \n[{start} - {end}]"

    response = sns.Topic(topic_arn).publish(Message=msg, Subject=MAIL_SUBJECT)
    print(response)


if __name__ == "__main__":
    lambda_handler({}, {})
