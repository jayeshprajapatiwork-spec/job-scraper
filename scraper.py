import requests
import csv

COMPANIES = [
    "cloudflare",
    "datadog",
    "stripe",
    "canva",
    "hashicorp",
    "snowflake",
    "duolingo",
    "airbnb",
    "robinhood",
    "coinbase"
]

ROLE_KEYWORDS = [
    "intern",
    "internship",
    "software",
    "software engineer",
    "backend",
    "full stack",
    "developer",
    "sde",
    "engineering",
    "new grad"
]

LOCATION_KEYWORDS = [
    "india",
    "bangalore",
    "bengaluru",
    "hyderabad",
    "pune",
    "mumbai",
    "remote"
]

jobs = []

for company in COMPANIES:

    try:
        url = f"https://boards-api.greenhouse.io/v1/boards/{company}/jobs"

        response = requests.get(url, timeout=20)

        if response.status_code != 200:
            continue

        data = response.json()

        for job in data["jobs"]:

            title = job.get("title", "").lower()

            location = (
                job.get("location", {})
                .get("name", "")
                .lower()
            )

            role_match = any(
                keyword in title
                for keyword in ROLE_KEYWORDS
            )

            location_match = any(
                keyword in location
                for keyword in LOCATION_KEYWORDS
            )

            if role_match:

                jobs.append([
                    company,
                    job.get("title", ""),
                    job.get("location", {})
                       .get("name", ""),
                    job.get("absolute_url", "")
                ])

    except Exception:
        pass

with open(
    "internships.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "Company",
        "Title",
        "Location",
        "Link"
    ])

    writer.writerows(jobs)

print(f"Found {len(jobs)} internships")
