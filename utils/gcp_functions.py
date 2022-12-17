from google.cloud import storage
from google.oauth2 import service_account
from django.conf import settings
import json

credentials = service_account.Credentials.from_service_account_info(json.loads(settings.GCP_JSON))


def download_blob(bucket_name, source_blob_name):
    storage_client = storage.Client(credentials=credentials)
    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(source_blob_name)
    blob = blob.download_as_bytes()

    return blob


def upload_blob_from_memory(bucket_name, contents, destination_blob_name):
    storage_client = storage.Client(credentials=credentials)
    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(destination_blob_name)

    blob.upload_from_string(contents)
