import boto3
import os

def list_s3_buckets():
    session = boto3.Session(
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=os.getenv("AWS_REGION", "us-east-1")
    )
    s3 = session.client("s3")
    response = s3.list_buckets()
    return [bucket['Name'] for bucket in response.get('Buckets', [])]
