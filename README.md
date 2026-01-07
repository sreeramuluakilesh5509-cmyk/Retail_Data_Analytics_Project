# Retail Data Analytics Dashboard

## Project Overview
This project involves end-to-end retail data analysis to uncover revenue trends, customer behavior, and geographic performance. The objective was to transform raw transactional data into actionable business insights using Python, SQL, and Power BI.

The project follows a real-world data analyst workflow: data cleaning → data storage → analysis → dashboarding.

---

## Tools & Technologies
- **Python** (Pandas, NumPy) – Data cleaning and feature engineering  
- **SQL (MySQL)** – Data storage and analytical queries  
- **Power BI** – DAX measures, interactive dashboards, and drill-down analysis  

---

## Dataset
- Online Retail transactional dataset  
- Contains invoice-level data including:
  - Invoice number
  - Product details
  - Quantity
  - Unit price
  - Customer ID
  - Country
  - Invoice date  
- Dataset size: **500,000+ records**

---

## Data Processing Workflow
1. Loaded raw CSV data using Python  
2. Cleaned the data by:
   - Removing duplicate records
   - Filtering invalid quantity and unit price values
   - Handling missing customer information
3. Feature engineering:
   - Extracted Year and Month from invoice date
   - Created Revenue column (Quantity × Unit Price)
4. Exported cleaned data for SQL and Power BI analysis  

---

## SQL Implementation
- Created database and tables in MySQL
- Used SQL queries to:
  - Calculate total revenue
  - Identify total customers and orders
  - Analyze revenue by country
  - Analyze monthly revenue trends
- SQL scripts are organized for reproducibility

---

## Key KPIs (DAX Measures)
- **Total Revenue**
- **Total Customers**
- **Total Orders**
- **Average Order Value (AOV)**

---

## Dashboard Visualizations (Power BI)
- KPI Cards for high-level metrics  
- Monthly Revenue Trend (Line Chart)  
- Top 10 Countries by Revenue (Bar Chart)  
- Slicers:
  - Year
  - Month
  - Country  
- Drill-down functionality:
  - Country → Monthly Revenue

---

## Key Business Insights
- Identified seasonal patterns in monthly revenue  
- Highlighted top revenue-contributing countries  
- Enabled interactive filtering for time-based and regional analysis  
- Dashboard supports quick decision-making for business stakeholders  

---


---

## Dashboard Preview
Screenshots of the Power BI dashboard and drill-down analysis are available in the `screenshots/` folder.

---

## Conclusion
This project demonstrates practical experience in data cleaning, SQL-based analysis, and building interactive Power BI dashboards. It reflects real-world data analyst responsibilities and highlights the ability to convert raw data into meaningful business insights.

---

