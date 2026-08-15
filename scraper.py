import requests
import csv

GREENHOUSE_COMPANIES = [
    "cloudflare",
    "datadog",
    "stripe"
]

KEYWORDS = [
    "intern",
    "internship",
    "software engineer intern",
    "swe intern",
    "summer intern",
    "student",
    "new grad"
]

jobs = []

for company in GREENHOUSE_COMPANIES:
    try:
        url = f"https://boards-api.greenhouse.io/v1/boards/{company}/jobs"

        data = requests.get(url, timeout=20).json()

        for job in data["jobs"]:

            title = job["title"]

            if any(k in title.lower() for k in KEYWORDS):

                jobs.append([
                    company,
                    title,
                    job.get("location", {}).get("name", ""),
                    job["absolute_url"]
                ])

    except Exception as e:
        print(company, e)

with open("internships.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    writer.writerow([
        "Company",
        "Title",
        "Location",
        "Link"
    ])

    writer.writerows(jobs)

print("Found", len(jobs), "internships")
