# 🛒 Instacart Order Analysis

**A Complete Product Analytics Portfolio Project**

---

## 📌 Project Overview

This project is an end-to-end product analytics case study using the Instacart Market Basket Dataset. It demonstrates the full workflow of a Data Analyst: from data engineering (PostgreSQL) to statistical analysis (Python) to business visualization (Looker Studio).

**Dataset:** 3.4 million grocery orders, 131,000 unique users, and 49,000 products.

**Goal:** Identify growth opportunities, customer retention drivers, and product performance trends to drive data-informed business decisions.

---

## 🔧 Tools Used

| Tool | Purpose |
| :--- | :--- |
| **PostgreSQL** | Data warehousing, complex SQL queries, indexing for performance |
| **pgAdmin** | Database management and query execution |
| **Python** | Statistical validation (T-Test), data visualization (Boxplot), automation |
| **Looker Studio** | Interactive dashboard for stakeholders |
| **GitHub** | Version control and portfolio hosting |

---

## 📂 Repository Structure

```
Instacart-Order-Analysis/
├── README.md
├── BUSINESS_MEMO.md
├── Business_Memo.pdf
├── Queries/
│   ├── 01_product_health.sql
│   ├── 02_best_sellers.sql
│   ├── 03_rfm_segmentation.sql
│   └── 04_ab_test_simulation.sql
├── Python/
│   └── instacart_analysis.py
├── Data/
│   ├── Product Health.csv
│   ├── Best Sellers.csv
│   ├── RFM Customer Segmentation.csv
│   ├── A_B Test (Weekend_Weekday).csv
│   ├── ab_test_raw_data.csv
│   └── weekend_weekday_chart.png
└── Dashboard/
    ├── dashboard_link.txt
    └── Instacart.pdf
```

---

## 🔍 Key Analytical Queries

### 1. Product Health KPIs
**Purpose:** Monitor overall business performance.
- Total orders
- Unique customers
- Average basket size
- Average days between purchases

### 2. Best Sellers by Reorder Rate
**Purpose:** Identify products with the highest customer retention.
- Bananas: 18,726 purchases, 88.4% reorder rate
- Organic Low Fat Milk: 91.3% reorder rate

### 3. RFM Customer Segmentation
**Purpose:** Segment users into actionable groups using **NTILE** window functions.
- **53,622 Champions** (High frequency, recent buyers)
- **19,950 At-Risk** (Low frequency, old buyers)

### 4. A/B Test Simulation (Weekend vs Weekday)
**Purpose:** Compare basket sizes between weekend and weekday shoppers.
- **Weekend average:** 11.46 items
- **Weekday average:** 10.06 items
- **Lift:** +14%
- **Statistical Validation:** T-Test P-Value = 0.0000000000

---

## 📊 Python Statistical Analysis

The Python script (`instacart_analysis.py`) does the following:

1. Connects to PostgreSQL and extracts raw basket size data (131,209 orders).
2. Runs an independent two-sample T-Test (Welch's T-Test) comparing weekend vs weekday basket sizes.
3. Generates a professional boxplot (`weekend_weekday_chart.png`) visualizing the distribution.
4. Automatically exports clean CSV files for dashboard integration.

**Key Result:** The 14% weekend lift is statistically significant (P-Value ≈ 0.00).

---

## 📈 Live Dashboard

An interactive dashboard was built in Looker Studio to present findings to stakeholders.

🔗 **Dashboard Link:** [Click Here to View](https://datastudio.google.com/reporting/8fac75f1-af58-4064-a7d0-dd44ffdac431)

**Dashboard Components:**
- KPI Scorecards (Average Basket Size, Total Orders, Days Between Orders)
- Weekend vs Weekday Bar Chart
- Top 10 Products by Reorder Rate
- RFM Customer Segmentation Pie Chart

---

## 💡 Key Business Insights

| Insight | Recommendation |
| :--- | :--- |
| Weekend shoppers buy 14% more items than weekday shoppers. | Invest in weekend-specific promotions and UI features. |
| Bananas and Organic Milk have reorder rates above 88%. | Guarantee 100% stock availability for these staples. |
| 19,950 At-Risk users are showing signs of churn. | Launch a targeted win-back campaign with discount vouchers. |
| Average purchase frequency is 17 days. | Explore subscription or reminder features to shorten the cycle. |

---

## 🚀 How to Replicate This Project

### Prerequisites
- PostgreSQL installed (v15 or higher)
- Python 3.10+ with required libraries: `psycopg2-binary`, `pandas`, `scipy`, `matplotlib`, `seaborn`
- Looker Studio account (free with Google account)

### Step 1: Database Setup
1. Download the Instacart Market Basket Dataset from Kaggle.
2. Run the `CREATE TABLE` commands from the `Queries/` folder.
3. Use `COPY` or pgAdmin's import tool to load the CSV data.
4. Create indexes on `user_id` and `product_id` for performance.

### Step 2: Run the Analysis
1. Execute the 4 analytical SQL queries in pgAdmin.
2. Export results as CSV files.
3. Run the Python script: `python instacart_analysis.py`

### Step 3: Build the Dashboard
1. Upload all CSV files to Looker Studio.
2. Build scorecards, bar charts, and pie charts as shown in the README.
3. Share publicly and embed the link.

---

## 📝 License

This project is for educational and portfolio purposes. Data sourced from the Instacart Market Basket Dataset (Kaggle).

---

## ⭐ Acknowledgments

- Instacart for providing the public dataset.
- PostgreSQL, Python, and Looker Studio for their powerful open-source and free tools.
