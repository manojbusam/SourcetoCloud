# Demonstrates uploading a local file to a Google Cloud Storage (GCS) bucket using the 'google-cloud-storage' library.
# Ensure proper authentication and replace placeholders for custom usage.

from google.cloud import storage  # Importing necessary libraries

def upload_to_gcp(local_file_path, bucket_name, gcp_file_name):
    # Authenticate using service account credentials
    client = storage.Client.from_service_account_json('path_to_service_account_key.json')

    try:
        # Accessing the specified GCS bucket and uploading the local file
        bucket = client.get_bucket(bucket_name)
        blob = bucket.blob(gcp_file_name)
        blob.upload_from_filename(local_file_path)
        print(f"File uploaded successfully to gs://{bucket_name}/{gcp_file_name}")
    except Exception as e:
        # Handling exceptions, if any, during the file upload process
        print(f"Error uploading file: {e}")

# Replace these values with your own
local_file_path = 'path_to_local_file/data.csv'  # Local file path
bucket_name = 'your_gcp_bucket_name'  # GCS bucket name
gcp_file_name = 'data.csv'  # The name with which the file will be saved in GCS bucket

upload_to_gcp(local_file_path, bucket_name, gcp_file_name)  # Calling the function with specified file paths and bucket details
