import requests
import datetime

base_url = "https://your-artifactory-url.com/artifactory"
repository = "your-repository-name"
username = "your-username"
password = "your-password"
cutoff_date = datetime.datetime.now() - datetime.timedelta(days=90)


def delete_files():
    url = f"{base_url}/{repository}?list&deep=1"
    auth = (username, password)
    response = requests.get(url, auth=auth).json()

    for result in response["files"]:
        created_date = datetime.datetime.fromtimestamp(result["created"] / 1000)
        if created_date < cutoff_date:
            file_name = result["uri"]
            delete_url = f"{base_url}/{repository}/{file_name}"
            requests.delete(delete_url, auth=auth)
            print(f"Deleted file: {file_name}")


delete_files()
