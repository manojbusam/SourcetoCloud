from google.cloud import storage

def upload_to_gcp(local_file_path, bucket_name, gcp_file_name):
    # Authenticate using service account credentials
    client = storage.Client.from_service_account_json('path_to_service_account_key.json')

    try:
        bucket = client.get_bucket(bucket_name)
        blob = bucket.blob(gcp_file_name)
        blob.upload_from_filename(local_file_path)
        print(f"File uploaded successfully to gs://{bucket_name}/{gcp_file_name}")
    except Exception as e:
        print(f"Error uploading file: {e}")

# Replace these values with your own
local_file_path = 'path_to_local_file/data.csv'
bucket_name = 'your_gcp_bucket_name'
gcp_file_name = 'data.csv'  # The name with which the file will be saved in GCP bucket

upload_to_gcp(local_file_path, bucket_name, gcp_file_name)
