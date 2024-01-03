# Demonstrates uploading a local file to an AWS S3 bucket using 'boto3'.
# Ensure correct AWS credentials and replace placeholders for custom usage.

import boto3  # Importing the boto3 library

def upload_to_s3(local_file_path, bucket_name, s3_file_name):
    s3 = boto3.client('s3')  # Creating an S3 client object using boto3
    
    try:
        # Uploading the local file to the specified S3 bucket
        s3.upload_file(local_file_path, bucket_name, s3_file_name)
        print(f"File uploaded successfully to {bucket_name}/{s3_file_name}")
    except Exception as e:
        # Handling exceptions, if any, during the file upload process
        print(f"Error uploading file: {e}")

# Replace these values with your own
local_file_path = 'path_to_local_file/data.csv'  # Local file path
bucket_name = 'your_s3_bucket_name'  # S3 bucket name
s3_file_name = 'data.csv'  # The name with which the file will be saved in S3

upload_to_s3(local_file_path, bucket_name, s3_file_name)  # Calling the upload function with specified file paths and bucket details
