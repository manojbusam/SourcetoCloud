from azure.storage.blob import BlobServiceClient

def upload_to_azure(local_file_path, container_name, azure_file_name, connection_string):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=azure_file_name)
        with open(local_file_path, "rb") as data:
            blob_client.upload_blob(data)
        print(f"File uploaded successfully to '{container_name}' container in Azure Blob Storage")
    except Exception as e:
        print(f"Error uploading file: {e}")

# Replace these values with your own
local_file_path = 'path_to_local_file/data.csv'
container_name = 'your_azure_container_name'
azure_file_name = 'data.csv'  # The name with which the file will be saved in Azure Blob Storage
connection_string = 'your_connection_string'

upload_to_azure(local_file_path, container_name, azure_file_name, connection_string)
