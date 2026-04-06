# NGO Analytics Dashboard 

**A full-stack data analytics pipeline built to help NGOs stop guessing and start deciding.**

🔗 **[View Live Dashboard](https://harjotiris.github.io/NGO-Data-Analytics-Project/)**
📡 **[API](https://ngo-analytics-dashboard.onrender.com/docs)**

---

## The Problem

Most NGOs are doing important work. but making decisions based on gut feeling, scattered spreadsheets, and monthly reports nobody reads. Data exists, but it just sits there.

This project attempts to change that.

---

## What This Does

Raw program data goes in. Actionable insights come out.

A program manager can now answer in seconds:
- Which city has the highest dropout rate?
- Which program costs the most per beneficiary?
- Is our reach growing or flatlining?
- Where should we focus funding next quarter?

These aren't small questions with no practical impact. The answers drive real decisions that affect real people. A funding change somewhere can impact new lives and bring positive change.

---

## What's Under the Hood

This isn't just a dashboard. It's a complete data pipeline built from scratch:

| Layer | Technology | What it does |
|---|---|---|
| Data Cleaning | Python + Pandas | Validates, transforms, and enriches raw data |
| Database | SQLite | Stores clean data for reliable querying |
| API | FastAPI | Serves data through 7 live endpoints |
| Dashboard | HTML + Chart.js | Interactive visualizations with live filters |
| Report Export | jsPDF | One-click PDF reports reflecting current filters |

---

## Features

- **4 interactive charts** - beneficiaries by city/program, dropout rates, cost efficiency, trends over time
- **3 simultaneous filters** - city, program, and year — all charts update instantly
- **KPI cards** - headline numbers at a glance
- **PDF report download** - filtered, formatted, ready to send to donors or board
- **Live REST API** - with auto-generated documentation at `/docs`
- **Deployed** - no setup required, works in any browser

---

## Key Insights (from synthetic data)

- Vocational training has the highest dropout rate (7.2%) and highest cost per beneficiary (₹407)
- Digital skills programs are the most cost-efficient (₹391 per beneficiary)
- Patna has the highest cost per beneficiary across all cities
- Beneficiary volume and dropout rate are negatively correlated — larger cohorts retain better

---

## Running Locally
```bash
# Clone the repo
git clone https://github.com/HarjotIris/NGO-Data-Analytics-Project.git
cd NGO-Data-Analytics-Project

# Install dependencies
pip install -r requirements.txt

# Generate and clean data
python generate_dataset.py
python cleaning_and_summarization.py

# Start the API
uvicorn main:app --reload

# Open dashboard
python -m http.server 3000
# Visit http://localhost:3000
```

---

## API Endpoints

| Endpoint | Description |
|---|---|
| `GET /` | Health check |
| `GET /cities` | City-level summary |
| `GET /programs` | Program-level summary |
| `GET /full_table` | All 432 records |
| `GET /cities/{city}` | Data for a specific city |
| `GET /programs/{program}` | Data for a specific program |
| `GET /filter?city=&program=` | Flexible multi-parameter filter |

Full interactive docs: [https://ngo-analytics-dashboard.onrender.com/docs](https://ngo-analytics-dashboard.onrender.com/docs)

---

## Built With Real NGOs in Mind

This project was built using synthetic data modelled on real NGO program structures - literacy, vocational training, and digital skills across four North Indian cities.

If you're an NGO with real program data, I'd love to rebuild this with your numbers. Reach out.

---

## Author

**Harjot Singh aka Iris** - aspiring data analyst, built this to demonstrate what's possible when NGO data is actually used.

*This data is synthetic. Real NGO data would tell an even more powerful story.*
