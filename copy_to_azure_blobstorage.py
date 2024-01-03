# Demonstrates uploading a local file to Azure Blob Storage using the 'azure-storage-blob' library.
# Ensure proper authentication and replace placeholders for custom usage.

from azure.storage.blob import BlobServiceClient  # Importing necessary libraries

def upload_to_azure(local_file_path, container_name, azure_file_name, connection_string):
    try:
        # Authenticate using connection string and get a blob client
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=azure_file_name)
        
        # Open the local file and upload its contents to Azure Blob Storage
        with open(local_file_path, "rb") as data:
            blob_client.upload_blob(data)
        
        print(f"File uploaded successfully to '{container_name}' container in Azure Blob Storage")
    except Exception as e:
        # Handling exceptions, if any, during the file upload process
        print(f"Error uploading file: {e}")

# Replace these values with your own
local_file_path = 'path_to_local_file/data.csv'  # Local file path
container_name = 'your_azure_container_name'  # Azure Blob Storage container name
azure_file_name = 'data.csv'  # The name with which the file will be saved in Azure Blob Storage
connection_string = 'your_connection_string'  # Connection string for Azure Blob Storage

upload_to_azure(local_file_path, container_name, azure_file_name, connection_string)  # Calling the function with specified file paths and connection details
