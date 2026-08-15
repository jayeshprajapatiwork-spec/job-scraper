import requests

url = "https://boards-api.greenhouse.io/v1/boards/notion/jobs"

response = requests.get(url, timeout=30)

print("Status Code:", response.status_code)
print(response.text[:500])
