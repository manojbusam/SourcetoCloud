import boto3

def upload_to_s3(local_file_path, bucket_name, s3_file_name):
    # AWS credentials are required for this operation
    s3 = boto3.client('s3')
    
    try:
        s3.upload_file(local_file_path, bucket_name, s3_file_name)
        print(f"File uploaded successfully to {bucket_name}/{s3_file_name}")
    except Exception as e:
        print(f"Error uploading file: {e}")

# Replace these values with your own
local_file_path = 'path_to_local_file/data.csv'
bucket_name = 'your_s3_bucket_name'
s3_file_name = 'data.csv'  # The name with which the file will be saved in S3

upload_to_s3(local_file_path, bucket_name, s3_file_name)