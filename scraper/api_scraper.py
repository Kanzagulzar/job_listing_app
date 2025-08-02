import os
import sys
import requests
from datetime import datetime

sys.path.append(os.path.abspath("backend"))
from models import db, Job
from app import app

def already_exists(title, company):
    return Job.query.filter_by(title=title, company=company).first() is not None

def run_api_scraper():
    url = "https://www.actuarylist.com/api/jobs"
    headers = {
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0"
    }

    print("📡 Fetching job listings from API...")
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"❌ Failed to fetch jobs. Status code: {response.status_code}")
        return

    jobs_data = response.json()
    print(f"🔍 Retrieved {len(jobs_data)} job records")

    with app.app_context():
        new_count = 0
        for job in jobs_data:
            title = job.get("title", "").strip()
            company = job.get("company", "").strip()
            location = job.get("location", "").strip()
            job_type = job.get("type", "Full-time")
            tags = job.get("tags", [])
            posting_date = datetime.strptime(job["created_at"], "%Y-%m-%dT%H:%M:%S.%fZ") if "created_at" in job else datetime.now()

            if not already_exists(title, company):
                job_record = Job(
                    title=title,
                    company=company,
                    location=location,
                    job_type=job_type,
                    posting_date=posting_date,
                    tags=",".join(tags)
                )
                db.session.add(job_record)
                new_count += 1
                print(f"📌 {title} @ {company} ✔ inserted")

        db.session.commit()
        print(f"✅ {new_count} new jobs inserted into the database.")

if __name__ == "__main__":
    run_api_scraper()
