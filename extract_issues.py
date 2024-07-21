import pandas as pd
import json

# run gh issue list -s open --json assignees,author,title,body,labels,closedAt,createdAt,projectItems,projectCards > json_test.json

# Load the JSON data
file_path = "./json_test.json"
with open(file_path, "r") as file:
    data = json.load(file)

# Normalize the JSON data
df = pd.json_normalize(data)

# tz aware datetime
df["closedAt"] = pd.to_datetime(df["closedAt"], utc=True)
df["createdAt"] = pd.to_datetime(df["createdAt"], utc=True)

df["time_taken"] = df["closedAt"] - df["createdAt"]

# Extract the required fields
table = pd.DataFrame(
    {
        "assignee_name": df["assignees"].apply(
            lambda x: x[0]["name"] if x else None
        ),
        "title": df["title"],
        "body": df["body"],
        "createdAt": df["createdAt"],
        "closedAt": df["closedAt"],
        "time_taken": df["time_taken"],
        "labels": df["labels"].apply(
            lambda x: "|".join([label["name"] for label in x])
        ),
        "project_items_status": df["projectItems"].apply(
            lambda x: "|".join([item["status"]["name"] for item in x])
        ),
        "author_name": df["author.name"],
    }
)

table.to_csv("issues.csv", index=False)
