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
    "coinbase",
    "razorpay",
    "phonepe",
    "groww",
    "zerodha",
    "cred",
    "meesho",
    "swiggy",
    "zomato",
    "zepto",
    "flipkart",
    "paytm",
    "ola",
    "olaelectric",
    "rapido",
    "delhivery",
    "browserstack",
    "postman",
    "freshworks",
    "chargebee",
    "darwinbox",
    "juspay",
    "coinDCX",
    "coinswitch",
    "unacademy",
    "urbancompany",
    "inmobi",
    "jumbotail",
    "netradyne",
    "ofbusiness",
    "lenskart"
]

ROLE_KEYWORDS = [
    "software engineer",
    "software engineering",
    "software developer",
    "backend",
    "frontend",
    "full stack",
    "full-stack",
    "java",
    "python",
    "developer",
    "web developer",
    "swe",
    "sde",
    "engineering intern",
    "software engineer intern",
    "backend engineer",
    "full stack engineer",
    "platform engineer",
    "cloud engineer",
    "machine learning",
    "ai engineer",
    "data engineer"
]

EXCLUDED = [
    "marketing",
    "sales",
    "finance",
    "audit",
    "accounting",
    "tax",
    "legal",
    "recruiting",
    "hr",
    "human resources",
    "customer support",
    "operations",
    "business analyst",
    "product manager",
    "designer",
    "content",
    "campaign",
    "merchant",
    "regulatory",
    "compliance"
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
                loc in location
                for loc in LOCATION_KEYWORDS
            )
            
            excluded_match = any(
                keyword in title
                for keyword in EXCLUDED
            )

            if role_match and location_match and not excluded_match:
            
                jobs.append([
                    company,
                    job.get("title", ""),
                    job.get("location", {}).get("name", ""),
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

    jobs.sort(key=lambda x: x[0])
    writer.writerows(jobs)

print(f"Found {len(jobs)} internships")
