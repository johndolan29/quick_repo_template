import os
import requests

# Get the repository details from environment variables
repo_owner = os.getenv("GITHUB_REPOSITORY_OWNER")
repo_name = os.getenv("GITHUB_REPOSITORY").split("/")[1]

# Get the GitHub token from environment variables
token = os.getenv("GITHUB_TOKEN")

# Set up the headers for authentication
headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json",
}

# Define the API endpoint to get issues
url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"

# Make the request to get all issues
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    issues = response.json()
    print("All issues in the repository:")
    for issue in issues:
        print(f"#{issue['number']} - {issue['title']}")
else:
    print(f"Failed to retrieve issues: {response.status_code}")
    print(response.text)
