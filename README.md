# 8-Ball Pool Analytics & Strategy Model 🎱

**Author:** Dhruv
**Role:** Data Analyst

## 📌 Project Overview
This project simulates, stores, and analyzes data from 1,000 matches of 8-Ball Pool to determine the most profitable gameplay strategies. By treating game mechanics like business decisions, this project demonstrates an end-to-end data analytics pipeline: synthesizing raw data, engineering a local database, querying for statistical insights, and visualizing expected value (EV) and bankroll trajectories over time.

## 🛠️ Tech Stack
* **Language:** Python 3
* **Libraries:** `pandas`, `numpy`, `matplotlib`, `seaborn`
* **Database:** SQLite3
* **Query Language:** SQL (aggregated via Python)

## 📊 The Data Pipeline (Methodology)

### 1. Data Generation (`data_generator.py`)
Since live server data is inaccessible, I engineered a Python script to generate a synthetic dataset of 1,000 matches. The script utilizes weighted probabilities to assign break types (Power Break, Second-Ball Break, Soft Break, Dry Break), wagers based on table tiers, and realistic win/loss outcomes based on the strategic advantage of each break pattern. 
* **Output:** `pool_match_data.csv`

### 2. Database Engineering (`load_to_sql.py`)
To replicate a production environment, the raw CSV is automatically extracted and loaded into a structured SQLite database (`pool_analytics.db`) using Python's `sqlite3` library. 
* **Output:** `match_history` SQL table.

### 3. Exploratory Data Analysis (`sql_analysis.py`)
I wrote SQL queries to aggregate the data and uncover hidden trends. Using `SUM(CASE WHEN...)` and `GROUP BY` statements, the script calculates the exact win percentage and net coin profit for every single break strategy.

### 4. Data Visualization (`visualize_data.py`)
I used Matplotlib and Seaborn to build a dual-chart dashboard communicating the findings:
* **Bar Chart:** Visualizes the win rate percentage by break type.
* **Line Chart:** Tracks the cumulative bankroll growth over 1,000 matches, proving the long-term ROI of optimal play.

## 💡 Key Insights & Business Logic
> **The Second-Ball Break is the optimal strategy.** 
While the "Power Break" is the most common (40% of matches), querying the data revealed that the "Second-Ball Break" yields a statistically significant higher win rate (~65%) and generates the highest net profit. Conversely, "Soft Breaks" and "Dry Breaks" actively drain the bankroll and result in negative Expected Value (EV).

## 🚀 How to Run Locally
1. Clone this repository.
2. Install required libraries: `pip install pandas numpy matplotlib seaborn`
3. Run the pipeline in order:
   * `python data_generator.py` (Generates the CSV)
   * `python load_to_sql.py` (Builds the SQLite Database)
   * `python sql_analysis.py` (Prints SQL insights to terminal)
   * `python visualize_data.py` (Generates the dashboard `.png`)
