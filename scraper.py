import requests

print("GitHub Actions is running Python successfully")

response = requests.get(
    "https://boards-api.greenhouse.io/v1/boards/notion/jobs",
    timeout=30
)

print("Status Code:", response.status_code)

data = response.json()

print("Total Jobs:", len(data["jobs"]))
