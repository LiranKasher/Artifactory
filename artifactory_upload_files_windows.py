import os
import requests

base_url = "https://your-artifactory-url.com/artifactory"
repository = "your-repository-name"
username = "your-username"
password = "your-password"
source_dir = "C:\\Upload"


def upload_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, directory)
            windows_destination_path = os.path.join(repository, relative_path)
            destination_path = windows_destination_path.replace("\\", "/")
            url = f"{base_url}/{destination_path}"
            auth = (username, password)

            with open(file_path, "rb") as f:
                file_content = f.read()
            response = requests.put(url, auth=auth, data=file_content)

            if response.status_code == 201:
                print(f"Uploaded file: {file_path}")
            else:
                print(f"Failed to upload file: {file_path}")
                print(response.text)


upload_files(source_dir)