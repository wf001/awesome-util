import os
import boto3
import datetime

_env = {
    "S3_DEST_KEY_PREFIX": os.getenv("S3_DEST_KEY_PREFIX"),
}


def move_s3_file(bucket: str, original_key: str, renamed_key: str) -> None:
    """
    Move s3 file from `original_key` to `renamed_key` on `bucket`
    """
    original = {"Bucket": bucket, "Key": original_key}
    s3 = boto3.resource("s3")
    s3.meta.client.copy(original, bucket, renamed_key)
    s3.meta.client.delete_object(Bucket=bucket, Key=original_key)


def lambda_handler(event, context):
    bucket = event["Records"][0]["s3"]["bucket"]["name"]

    original_key = event["Records"][0]["s3"]["object"]["key"]

    dest_key_prefix = _env["S3_DEST_KEY_PREFIX"]
    renamed_key = f"{dest_key_prefix}{int(datetime.datetime.now())}.txt.gz"

    move_s3_file(bucket, original_key, renamed_key)
    print(f"{original_key} renamed to {renamed_key}")


if __name__ == "__main__":
    lambda_handler({}, {})
