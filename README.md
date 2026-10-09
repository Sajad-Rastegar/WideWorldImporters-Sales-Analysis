# WideWorldImporters Sales Analysis

## Project Overview

This project analyzes sales data from the WideWorldImporters database using SQL Server and Python.

The goal is to explore monthly and yearly sales performance, identify the highest and lowest sales months, calculate sales changes, and visualize the results through charts.

## Technologies Used

- **SQL Server:** Data extraction and aggregation using SQL queries.
- **Python:** Data analysis and automation.
- **Pandas:** Data manipulation and analysis.
- **PyODBC:** Connecting Python to SQL Server.
- **Matplotlib:** Data visualization.

## Project Features

- Retrieve monthly sales data from SQL Server.
- Calculate previous-month and next-month sales.
- Calculate monthly sales changes and percentage changes.
- Identify the highest and lowest sales months.
- Aggregate monthly sales into yearly sales totals.
- Calculate year-over-year sales growth.
- Export analysis results to CSV files.
- Generate charts to visualize sales performance.

## Project Structure

```text
WideWorldImporters-Sales-Analysis/
│
├── sales_analysis.py
├── README.md
├── charts/
│   ├── monthly_sales_trend.png
│   ├── yearly_sales_comparison.png
│   └── top_5_sales_months.png
└── reports/
    ├── monthly_sales_report.csv
    └── yearly_sales_report.csv
```

## Visualizations

### 1. Monthly Sales Trend

Shows how sales change over time, month by month.

![Monthly Sales Trend](charts/monthly_sales_trend.png)

### 2. Yearly Sales Comparison

Compares total sales across different years. The latest year may contain incomplete data.

![Yearly Sales Comparison](charts/yearly_sales_comparison.png)

### 3. Top 5 Months by Sales

Highlights the five months with the highest calculated sales.

![Top 5 Sales Months](charts/top_5_sales_months.png)

## Output Reports

The project generates two CSV reports:

- `monthly_sales_report.csv`: Monthly sales, previous-month sales, next-month sales, sales changes, and percentage changes.
- `yearly_sales_report.csv`: Annual sales totals, previous-year sales, and year-over-year growth percentages.

## How to Run

### Prerequisites

- Python
- Microsoft SQL Server
- The WideWorldImporters sample database
- ODBC Driver 17 for SQL Server
- The following Python libraries: `pandas`, `pyodbc`, and `matplotlib`

### Installation

Install the required Python libraries:

```bash
pip install pandas pyodbc matplotlib
```

### Database Configuration

Update the SQL Server instance name in `sales_analysis.py` to match your local SQL Server configuration.

The project uses Windows integrated authentication.

### Run the Project

Execute the Python script:

```bash
python sales_analysis.py
```

The analysis reports and charts will be generated automatically in the `reports` and `charts` directories.

## Notes

- Sales are calculated using order-line quantity multiplied by unit price.
- The latest year's data may be incomplete, so its total should not be directly compared with full-year totals.
- A local SQL Server instance and an accessible WideWorldImporters database are required to run the script.

## Author

**Sajad Rastegar**

Computer Engineering Graduate | SQL Server | Python | Data Analysis