# ⚽ FIFA World Cup 2022 — Interactive Football Analytics Dashboard 

![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-Querying-orange?style=for-the-badge&logo=databricks&logoColor=white)
![Wikipedia](https://img.shields.io/badge/Web%20Scraping-BeautifulSoup-green?style=for-the-badge)
![CSV](https://img.shields.io/badge/Data-CSV-blue?style=for-the-badge) 
![License](https://img.shields.io/badge/License-Educational-lightgrey?style=for-the-badge)

> A professional-grade, interactive Power BI dashboard delivering deep analytical insights into the performance of the **Top 20 National Football Teams** based on FIFA World Cup 2022 statistics — featuring dynamic filters, historical intelligence, and player-level tactical analysis.

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Dashboard Features](#-dashboard-features)
- [Data Pipeline](#-data-pipeline)
- [Tech Stack](#-tech-stack)
- [Project Architecture](#-project-architecture)
- [Key Insights](#-key-insights)
- [Getting Started](#-getting-started)
- [Screenshots / Demo](#-screenshots--demo)
- [License](#-license)

---

## 🌍 Overview

This project transforms raw FIFA World Cup data into a fully interactive business intelligence solution. By combining **automated web scraping**, **data engineering with Python**, **SQL-based querying via SQLite**, and **advanced Power BI visualizations**, this dashboard enables football analysts, enthusiasts, and data professionals to explore team performance, historical achievements, and player-level metrics in a single, unified interface.

The dashboard covers:
- All group stage and knockout matches from the **2022 FIFA World Cup (Qatar)**
- Historical World Cup records across all participating nations
- Forward-looking integration of the **2026 FIFA World Cup fixture schedule**

---

## 📊 Dashboard Features

| Feature | Description |
|---|---|
| 🔘 **Dynamic Team Selection** | Multi-select filter to explore and compare stats across national teams simultaneously |
| 📋 **Match Overview** | Summary view of matches played, wins, losses, draws, and current FIFA world rankings |
| 📅 **2026 Fixture Integration** | Upcoming World Cup schedule embedded directly into the dashboard |
| 🏅 **Historical Achievements** | Comprehensive win/loss records across all FIFA World Cup editions |
| 🎯 **Goals Analysis** | Team contributions to total goals scored, attacking efficiency metrics, and scoring patterns |
| 🕹️ **Player-Level Radar Chart** | Comparative radar visualization for key metrics — passes, assists, goals, and touches |
| 📈 **Recent Form Tracker** | Visualization of each team's last 5 match outcomes |
| 🌐 **World Ranking View** | FIFA ranking integration for contextual performance benchmarking |

---

## ⚙️ Data Pipeline

```
Wikipedia / Web Sources
        │
        ▼
  Python (BeautifulSoup + Requests)        ← Web Scraping Layer
        │
        ▼
  Pandas (Data Cleaning & Wrangling)       ← Data Engineering Layer
        │
        ▼
  SQLite Database (football_data.db)       ← Relational Storage Layer
        │
        ▼  (SQL queries via Python)
  Aggregated Query Results                 ← SQL Analytics Layer
        │
        ▼
  CSV Export (Structured Output)           ← Data Transfer Layer
        │
        ▼
  Power Query (Null Handling, Filters)     ← ETL Layer
        │
        ▼
  DAX Measures (Advanced Calculations)     ← BI Analytics Layer
        │
        ▼
  Power BI Dashboard (Visualizations)      ← Presentation Layer
```

### Pipeline Breakdown

- **Web Scraping** — Automated extraction of World Cup wins, losses, and historical records directly from Wikipedia using `requests` and `BeautifulSoup`
- **Data Cleaning** — Applied `Pandas` for null-value handling, column normalization, and type casting before loading into the database
- **SQLite Storage** — Cleaned DataFrames are written to a local SQLite database (`football_data.db`) using Python's built-in `sqlite3` module, creating a structured, queryable data store
- **SQL Querying** — Analytical SQL queries are executed against the SQLite database to aggregate KPIs such as total goals per team, win rates, and match counts — results are then exported as CSVs for Power BI ingestion
- **Power Query (M Language)** — Applied further transformations inside Power BI including null replacement, conditional columns, and data type enforcement
- **DAX Calculations** — Built calculated measures for aggregated KPIs, rolling averages, win-rate percentages, and ranking logic
- **Image Handling** — National team flags and logos managed via Base64 encoding and Wikipedia-sourced CSV references for seamless visual integration

---

## 🛠️ Tech Stack

### Data Collection & Engineering
| Tool | Purpose |
|---|---|
| **Python 3.x** | Core scripting language for the data pipeline |
| **BeautifulSoup4** | HTML parsing for structured web scraping |
| **Requests** | HTTP library for fetching Wikipedia pages |
| **Pandas** | Data manipulation, cleaning, and CSV export |
| **NumPy** | Numerical operations and array handling |
| **Jupyter Notebook** | Exploratory data analysis and pipeline development |

### Data Storage & Database
| Tool | Purpose |
|---|---|
| **SQLite** | Lightweight relational database storing cleaned match and team data |
| **SQL (sqlite3)** | Querying and aggregating data from the SQLite database before Power BI export |
| **CSV** | Final structured output format for Power BI ingestion |
| **Base64 Encoding** | Embedding team flag images directly into Power BI |
| **Wikipedia CSV References** | Sourcing image URLs for visual integration |

### Business Intelligence & Visualization
| Tool | Purpose |
|---|---|
| **Power BI Desktop** | Primary dashboard development and visualization |
| **Power Query (M Language)** | ETL transformations within Power BI |
| **DAX (Data Analysis Expressions)** | Advanced calculated measures and KPIs |
| **Power BI Data Model** | Relational model connecting teams, players, and fixtures |

---

## 🏗️ Project Architecture

```
📦 football-dashboard/
 ┣ 📂 data/
 ┃ ┣ 📂 raw/                    # Raw scraped data from Wikipedia
 ┃ ┣ 📂 processed/              # SQL-queried, aggregated CSV exports
 ┃ ┣ 📂 database/               # SQLite database file
 ┃ ┃ ┗ 🗄️ football_data.db      # Relational store for cleaned match data
 ┃ ┗ 📂 images/                 # Base64 encoded flag images / wiki CSV references
 ┣ 📂 notebooks/
 ┃ ┗ 📓 scraping_pipeline.ipynb # Web scraping, cleaning, SQLite & SQL queries
 ┣ 📂 scripts/
 ┃ ┣ 🐍 scraper.py              # Web scraping module
 ┃ ┣ 🐍 clean_data.py           # Data cleaning & SQLite loading module
 ┃ ┗ 🐍 sql_queries.py          # SQL aggregation queries & CSV export module
 ┣ 📊 FootballDashboard.pbix    # Power BI dashboard file
 ┣ 📄 requirements.txt          # Python dependencies
 ┗ 📄 README.md
```

---

## 💡 Key Insights

This dashboard surfaces the following analytical narratives:

- **Team Performance Benchmarking** — Side-by-side comparison of nations across goals scored, wins, and tournament progression
- **Historical Dominance Patterns** — Longitudinal analysis of traditional powerhouses versus emerging football nations
- **Player Tactical Profiles** — Radar charts enabling tactical evaluation of individual players across key contribution metrics
- **Attacking Strength Index** — Identifies which teams overperformed or underperformed relative to their FIFA world ranking
- **Form & Momentum Analysis** — 5-match form strips revealing momentum trends heading into the 2026 World Cup cycle

---

## 🚀 Getting Started

### Prerequisites

```bash
pip install -r requirements.txt
```

**Requirements include:** `pandas`, `numpy`, `requests`, `beautifulsoup4`, `jupyter`

> `sqlite3` is included in Python's standard library — no separate install needed.

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/football-dashboard.git
   cd football-dashboard
   ```

2. **Scrape and clean the data**
   ```bash
   python scripts/scraper.py
   python scripts/clean_data.py
   ```
   This generates the raw CSVs and loads the cleaned data into `data/database/football_data.db`.

3. **Run SQL queries to generate aggregated exports**
   ```bash
   python scripts/sql_queries.py
   ```
   This executes SQL against the SQLite database and exports the results to `data/processed/` as CSVs. Example query inside the script:
   ```python
   import sqlite3
   import pandas as pd

   conn = sqlite3.connect("data/database/football_data.db")

   query = """
       SELECT team,
              SUM(goals_scored)  AS total_goals,
              COUNT(*)           AS matches_played,
              SUM(CASE WHEN result = 'Win' THEN 1 ELSE 0 END) AS total_wins
       FROM world_cup_stats
       GROUP BY team
       ORDER BY total_goals DESC
   """

   df_aggregated = pd.read_sql(query, conn)
   df_aggregated.to_csv("data/processed/goals_summary.csv", index=False)
   conn.close()
   ```

4. **Open Power BI**
   - Launch `FootballDashboard.pbix` in Power BI Desktop

5. **Update data source paths**
   - In Power BI → Transform Data → Data Source Settings
   - Point the source paths to your local `data/processed/` directory

6. **Refresh the dataset**
   - Click **Refresh** in Power BI to load the latest SQL-aggregated data

---

## 🎥 Screenshots / Demo

> 📽️ *[Insert demo GIF or video link here]*

> 📸 *[Insert dashboard screenshot here]*

---

## 📜 License

This project is developed for **educational and analytical purposes only**.  
Data is sourced from [Wikipedia](https://www.wikipedia.org/) and processed using open-source Python libraries and Microsoft Power BI.

---

## 🤝 Connect

If you found this project insightful or have suggestions, feel free to connect or raise an issue!

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/your-profile)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=flat&logo=github)](https://github.com/your-username)

---

*Built with ❤️ for football data enthusiasts and analytics professionals.*
