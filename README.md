Here's your updated `README.md` with your **LinkedIn** and **GitHub** links added correctly:

---

```markdown
# 💼 Job Listing Web App – Full-Stack Project

This is a full-stack Job Board Web Application. It features a Flask REST API,  database, a React frontend, and a Selenium-based scraper that pulls live job data from [ActuaryList.com](https://www.actuarylist.com).

> 🚀 **Live Frontend:** [https://vercel.com/kanzagulzars-projects/job-listing-app](#)  
> 🖥️ **Backend:** Runs locally via Flask  
> 📹 **Demo Video:** [https://drive.google.com/file/d/1-e_I28oAEFNebnzamGkQ8pveC19ntXkA/view?usp=sharing](#)

---

## 📁 Project Structure

```

job\_app/
│
├── backend/
│   ├── app.py               # Main Flask app
│   ├── models.py            # SQLAlchemy models
│   ├── routes.py            # REST API endpoints
│   ├── scraper.py           # Selenium scraper for actuarylist.com
│   ├── requirements.txt     # Python dependencies
│   ├── .env.example         # Environment variable sample
│   └── config.py            # DB & Flask config
│
├── frontend/
│   ├── src/
│   │   ├── components/      # JobCard, JobForm, FilterBar, etc.
│   │   ├── App.js           # Main React app
│   │   └── api.js           # API interaction logic
│   ├── package.json
│   └── public/
│
└── README.md

🔧 Setup Instructions

1. Backend – Flask API

✅ Requirements

- Python 3.9+
- SQLite (default, can be changed)
- Chrome + ChromeDriver (for scraper)

 ✅ Installation
bash
cd backend
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

pip install -r requirements.txt

#### ✅ Environment Variables

Create a `.env` file using `.env.example` as a template:

env
DATABASE_URL=sqlite:///jobs.db
FLASK_ENV=development

✅ Run the Flask Server

bash
python app.py

If using Alembic for migrations:

bash
flask db init

### 2. Frontend – React

#### ✅ Requirements

* Node.js 16+

#### ✅ Installation

```bash
cd frontend
npm install
```

#### ✅ Run the React App

```bash
npm start
```

Make sure the API base URL in `src/api.js` matches your backend (e.g., `http://localhost:5000`).

---

### 3. Selenium Scraper

#### ✅ Installation

Already handled in `backend/requirements.txt`.

#### ✅ Run the Scraper

```bash
cd backend
python scraper.py
```

This script:

* Navigates to **ActuaryList.com**
* Extracts title, company, location, posting date, and tags
* Inserts data into your database
* Prevents duplicate entries

---

## ⚙️ Features Overview

### 🔹 Backend (Flask + SQLAlchemy)

* REST API: `GET`, `POST`, `PUT`, `DELETE` endpoints at `/jobs`
* Filter jobs by type, location, or tags using query parameters

  * Example: `/jobs?job_type=Full-time&location=Remote`
* Sort by posting date

  * Example: `/jobs?sort=posting_date_desc`
* Input validation with appropriate HTTP status codes (400, 404)

### 🔹 Frontend (React)

* Responsive job board interface
* CRUD operations: Add, Edit, Delete job listings
* Dynamic filtering by:

  * Job Type
  * Tags
  * Location
  * Keywords (title/company)
* Sorting (Newest/Oldest first)
* Form validation and API error feedback

### 🔹 Scraper (Selenium)

* Scrapes real-time job data from [ActuaryList.com](https://www.actuarylist.com)
* Handles dynamic content
* Inserts scraped jobs into the database without duplication

---

## 🎥 Demo Video

The demo covers:

* Full application walkthrough
* Backend API testing (CRUD + filters)
* React frontend interaction
* Live data scraping demo
* Challenges, architecture, and trade-offs

## 🧠 Assumptions & Notes

* All scraped jobs are assumed **Full-time** unless otherwise noted
* Tags are stored as a **comma-separated string**
* Backend is **not deployed** (runs locally)
* Scraper currently fetches **first 50 jobs** for demo

## 📌 Tech Stack

| Layer    | Technologies Used                      |
| -------- | -------------------------------------- |
| Frontend | React, CSS Modules                     |
| Backend  | Flask, SQLAlchemy, Marshmallow         |
| Database | SQLite (easily switchable to Postgres) |
| Scraper  | Python, Selenium, ChromeDriver         |
| Tools    | Vercel, Postman, VS Code               |

---

## 🙋‍♀️ Author

**Kanza-tul-Islam**
[LinkedIn](https://www.linkedin.com/in/kanza-tul-islam) • [GitHub](https://github.com/Kanzagulzar)


