import requests

companies = [
    "cloudflare",
    "stripe",
    "datadog",
    "airbnb",
    "notion",
    "coinbase",
    "scaleai",
    "rippling"
]

for company in companies:
    try:
        url = f"https://boards-api.greenhouse.io/v1/boards/{company}/jobs"

        data = requests.get(url, timeout=20).json()

        print(f"\n=== {company.upper()} ===")

        for job in data["jobs"]:
            if "intern" in job["title"].lower():
                print(job["title"])
                print(job["absolute_url"])

    except:
        pass
