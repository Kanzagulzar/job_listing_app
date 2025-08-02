from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from datetime import datetime
import os
import sys
sys.path.append(os.path.abspath("backend"))

from models import db, Job
from app import app


def extract_job_data(card):
    try:
        title_el = card.find_element(By.CLASS_NAME, "Job_job-card__position__ic1rc")
        company_el = card.find_element(By.CLASS_NAME, "Job_job-card__company__7T9qY")
        location_els = card.find_elements(By.CLASS_NAME, "Job_job-card__location__bq7jX")
        tag_els = card.find_elements(By.CLASS_NAME, "Job_job-card__location__bq7jX")

        title = title_el.text
        company = company_el.text
        locations = ", ".join([el.text for el in location_els])
        tags = ", ".join([el.text for el in tag_els])
        posting_date = datetime.now()
        job_type = "Full-time"

        return {
            "title": title,
            "company": company,
            "location": locations,
            "posting_date": posting_date,
            "job_type": job_type,
            "tags": tags,
        }
    except Exception as e:
        print(f"❌ Failed to extract one job: {e}")
        return None


def already_exists(title, company):
    return Job.query.filter_by(title=title, company=company).first() is not None


def run_scraper():
    options = Options()
    # Comment this line if you want to see the browser
    # options.add_argument("--headless")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get("https://www.actuarylist.com")
        print("🌐 Page loaded...")

        # Scroll to bottom to trigger lazy loading
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print("🌀 Scrolled to bottom... waiting for jobs...")

        # Wait for job cards to appear
        WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "Job_job-page-link__a5I5g"))
        )

        cards = driver.find_elements(By.CLASS_NAME, "Job_job-page-link__a5I5g")
        print(f"🔍 Found {len(cards)} job cards")

        with app.app_context():
            for card in cards[:50]:
                parent = card.find_element(By.XPATH, "./..")
                job_data = extract_job_data(parent)
                if job_data and not already_exists(job_data["title"], job_data["company"]):
                    job = Job(**job_data)
                    db.session.add(job)
                    print(f"📌 {job_data['title']} @ {job_data['company']} ✔ inserted")

            db.session.commit()
            print("✅ Done.")

    finally:
        driver.quit()


if __name__ == "__main__":
    run_scraper()
