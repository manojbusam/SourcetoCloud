# Source-to-Cloud Data Transfer

This repository provides Python scripts demonstrating how to copy data from a local source to cloud storage services: AWS S3, Google Cloud Storage (GCS), and Azure Blob Storage.

## Getting Started

### Prerequisites

Make sure you have the following installed:

| Tool                                    | Version/Requirements       |
|-----------------------------------------|----------------------------|
| [![Python](https://img.shields.io/badge/Python-3.6+-blue)](https://www.python.org/downloads/) | - |
| [![boto3](https://img.shields.io/badge/boto3-required-green)](https://pypi.org/project/boto3/) | Required Library |
| [![google-cloud-storage](https://img.shields.io/badge/google--cloud--storage-required-green)](https://pypi.org/project/google-cloud-storage/) | Required Library |
| [![azure-storage-blob](https://img.shields.io/badge/azure--storage--blob-required-green)](https://pypi.org/project/azure-storage-blob/) | Required Library |


## Files

1. **AWS S3 (`copy_to_s3.py`):** This Python script showcases how to upload data from a local source to an AWS S3 bucket using the `boto3` library.

2. **Google Cloud Storage (`copy_to_gcp_bucket.py`):** The Python script `copy_to_gcp_bucket.py` demonstrates the process of transferring data from a local source to Google Cloud Storage using the `google-cloud-storage` library.

3. **Azure Blob Storage (`copy_to_azure_blobstorage.py`):** The `copy_to_azure_blobstorage.py` Python script illustrates copying data from a local source to Azure Blob Storage using the `azure-storage-blob` library.

## Usage

### AWS S3

- **Prerequisites:** Ensure `boto3` is installed (`pip install boto3`) and AWS credentials are configured.

- **Execution:**
    ```bash
    python copy_to_s3.py
    ```
    Replace the `local_file_path`, `bucket_name`, and `s3_file_name` variables within the script with your specific paths and bucket details.

### Google Cloud Storage

- **Prerequisites:** Install the `google-cloud-storage` library (`pip install google-cloud-storage`) and authenticate using GCP service account credentials.

- **Execution:**
    ```bash
    python copy_to_gcp_bucket.py
    ```
    Update the `local_file_path`, `bucket_name`, and `gcp_file_name` variables within the script with your file paths and GCP bucket details.

### Azure Blob Storage

- **Prerequisites:** Install the `azure-storage-blob` library (`pip install azure-storage-blob`) and authenticate using Azure credentials or connection strings.

- **Execution:**
    ```bash
    python copy_to_azure_blobstorage.py
    ```
    Adjust the `local_file_path`, `container_name`, `azure_file_name`, and `connection_string` variables within the script based on your local file and Azure Blob Storage configurations.

## Notes

- Ensure you have proper access and permissions to the respective cloud storage services.
- Update the variables in each script with your own file paths, bucket/container names, and other required details.

