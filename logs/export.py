import boto3
import datetime
import os
from typing import Tuple

_env = {
    "logStreamNamePrefix": os.getenv("LOGS_LOG_STREAM_NAME_PREFIX"),
    "logGroupName": os.getenv("LOGS_LOG_GROUP_NAME"),
    "destination": os.getenv("LOGS_DESTINATION"),
    "destinationPrefix": os.getenv("LOGS_DESTINATION_PREFIX"),
}


def get_ut_range(tdelta_from: int = 1, tdelta_to: int = 1) -> Tuple[int, int]:
    """
    Return unix time(millisecond) range.

    `tdelta_from`: indicate from which point in time the log is to be exported
    `tdelta_to`: indicate to which point in time the log is to be exported

    By default, the log between current time 2 days ago and current time of the previous day is to be exported.

    """
    cur_sec = int(datetime.datetime.now().timestamp())
    one_day_msec = 3600 * 24 * 1000
    _to = cur_sec * 1000 - one_day_msec * tdelta_to
    _from = _to - one_day_msec * tdelta_from
    return _from, _to


def lambda_handler(event, context):
    _from, _to = get_ut_range()
    print(_from, _to)

    logs_client = boto3.client("logs")
    res = logs_client.create_export_task(
        taskName="daily-export-task01",
        logGroupName=_env["logGroupName"],
        logStreamNamePrefix=_env["logStreamNamePrefix"],
        fromTime=_from,
        to=_to,
        destination=_env["destination"],
        destinationPrefix=_env["destinationPrefix"],
    )
    print(res)


if __name__ == "__main__":
    lambda_handler({}, {})
