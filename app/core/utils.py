from tokenize import String
import boto3
from fastapi import File, HTTPException
from app.core.settings import settings

ACCESS_KEY_ID=settings.AWS_ACCESS_KEY
ACCESS_SECRET_KEY=settings.AWS_SECRET_KEY
S3_BUCKET_NAME=settings.S3_BUCKET_NAME

def upload_file_obj(file: File, path: str):
    upload_path = '{}/{}'.format(path, file.filename)

    try:
        s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY_ID, aws_secret_access_key=ACCESS_SECRET_KEY)
        res = s3.upload_fileobj(file.file, S3_BUCKET_NAME, upload_path)
        return res
    except Exception as e:
        print(f"Another error => {e}")
        raise HTTPException(status_code=500)