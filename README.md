Job Listing Application (Flask + React + Selenium)
A full-stack job board application built using Flask (Python) for the backend, React for the frontend, and Selenium for scraping job listings from a target website.
📦 Features

- Add, update, delete, and view job listings
- Filter by keyword, location, and job type
- Sort by date (newest/oldest)
- Web scraping with Selenium
- Database
- Deployed to Render

⚙️ Tech Stack

- Backend: Python, Flask, SQLAlchemy, SQLite
- Frontend: React, Axios
- Scraper: Python, Selenium
- Deployment: Render

🖥️ Environment Setup
🔹 Prerequisites

- Python >=3.9
- Node.js >=18 and npm
- Git

🔧 Backend Setup (Flask)

1. Create virtual environment:
   python -m venv .venv

2. Activate the environment:
   On Windows:
     .venv\Scripts\activate
   On macOS/Linux:
     source .venv/bin/activate

3. Install Python dependencies:
   pip install -r requirements.txt

4. Database setup:
   - The app uses SQLite by default.
   - If you want to modify the DB config, update config.py

5. Run backend server:
   python app.py
   - The server will run on: http://localhost:5000

🎨 Frontend Setup (React)

1. Navigate to the frontend directory:
   cd frontend

2. Install dependencies:
   npm install

3. Run development server:
   npm start
   - The app will be available at http://localhost:3000

🤖 Scraper Setup (Selenium)

1. Install Selenium:
   pip install selenium

2. Install browser driver:
   - For Chrome: https://sites.google.com/chromium.org/driver/
   - For Firefox: https://github.com/mozilla/geckodriver/releases

   Place the driver binary in your system's PATH or project root.

3. Run the scraper:
   python scraper/scraper.py
   - This will scrape job listings and store them into the database automatically.

🛠 Project Structure

job_listing_app/
├── backend/  
├── frontend/           
├── scraper/            
├── .render.yaml        
├── requirements.txt
└── README.md

📌 Notes

- If you encounter CORS issues, make sure Flask has CORS(app) enabled.
- Customize database or deploy PostgreSQL using Render’s add-on.

📫 Contact
Feel free to open issues or pull requests. Built by Kanzagulzar (https://github.com/Kanzagulzar)
