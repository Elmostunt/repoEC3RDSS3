import boto3
import os
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION")
)

BUCKET = os.getenv("S3_BUCKET")

def listar_archivos():
    response = s3.list_objects_v2(Bucket=BUCKET)

    if "Contents" not in response:
        return []

    return [obj["Key"] for obj in response["Contents"]]