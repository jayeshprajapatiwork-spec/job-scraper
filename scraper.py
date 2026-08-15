import requests

url = "https://boards-api.greenhouse.io/v1/boards/cloudflare/jobs"

response = requests.get(url, timeout=30)

print("Status Code:", response.status_code)

data = response.json()

print("Keys:", data.keys())
print("Total Jobs:", len(data["jobs"]))
