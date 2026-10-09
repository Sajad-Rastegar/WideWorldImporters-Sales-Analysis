import os

import pandas as pd
import pyodbc
import matplotlib.pyplot as plt


# Create output folders
os.makedirs("reports", exist_ok=True)
os.makedirs("charts", exist_ok=True)


# Connect to SQL Server and retrieve monthly sales

connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=YOUR_SERVER_NAME;"
    "DATABASE=WideWorldImporters;"
    "Trusted_Connection=yes;"
)

query = """
SELECT
    YEAR(O.OrderDate) AS [Year],
    MONTH(O.OrderDate) AS [Month],
    SUM(OL.Quantity * OL.UnitPrice) AS TotalSale
FROM Sales.Orders AS O
INNER JOIN Sales.OrderLines AS OL
    ON OL.OrderID = O.OrderID
GROUP BY
    YEAR(O.OrderDate),
    MONTH(O.OrderDate)
ORDER BY
    [Year],
    [Month];
"""

connection = pyodbc.connect(connection_string)


data = pd.read_sql_query(query, connection)



print("Data retrieved successfully.")
print(f"Dataset shape: {data.shape}")


# Monthly sales analysis

monthly_sales = (
    data.sort_values(["Year", "Month"])
    .reset_index(drop=True)
)

monthly_sales["Period"] = (
    monthly_sales["Year"].astype(int).astype(str)
    + "-"
    + monthly_sales["Month"].astype(int).astype(str).str.zfill(2)
)

monthly_sales["PreviousMonthSale"] = (
    monthly_sales["TotalSale"].shift(1)
)

monthly_sales["NextMonthSale"] = (
    monthly_sales["TotalSale"].shift(-1)
)

monthly_sales["SaleChange"] = (
    monthly_sales["TotalSale"]
    - monthly_sales["PreviousMonthSale"]
)

monthly_sales["SaleChangePct"] = (
    monthly_sales["SaleChange"]
    / monthly_sales["PreviousMonthSale"]
    * 100
)

print("\nMonthly Sales Analysis:")
print(monthly_sales.head(10).round(2))


# Highest and lowest sales months

best_month = monthly_sales.loc[
    monthly_sales["TotalSale"].idxmax()
]

worst_month = monthly_sales.loc[
    monthly_sales["TotalSale"].idxmin()
]

print("\nMonth with the highest sales:")
print(best_month)

print("\nMonth with the lowest sales:")
print(worst_month)


# Yearly sales analysis

yearly_sales = (
    monthly_sales.groupby("Year", as_index=False)["TotalSale"]
    .sum()
    .sort_values("Year")
    .reset_index(drop=True)
)

yearly_sales["PreviousYearSale"] = (
    yearly_sales["TotalSale"].shift(1)
)

yearly_sales["GrowthPct"] = (
    (
        yearly_sales["TotalSale"]
        - yearly_sales["PreviousYearSale"]
    )
    / yearly_sales["PreviousYearSale"]
    * 100
)

print("\nYearly Sales Analysis:")
print(yearly_sales.round(2))


# Export reports

monthly_sales.to_csv(
    "reports/monthly_sales_report.csv",
    index=False
)

yearly_sales.to_csv(
    "reports/yearly_sales_report.csv",
    index=False
)

print("\nReports saved successfully.")


# Chart 1: Monthly sales trend

plt.figure(figsize=(12, 5))

plt.plot(
    monthly_sales["Period"],
    monthly_sales["TotalSale"],
    marker="o",
    markersize=3,
    linewidth=1.5
)

tick_positions = list(range(0, len(monthly_sales), 3))

plt.xticks(
    tick_positions,
    monthly_sales["Period"].iloc[tick_positions],
    rotation=45,
    ha="right"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Year-Month")
plt.ylabel("Total Sales")
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig(
    "charts/monthly_sales_trend.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# Chart 2: Yearly sales comparison

plt.figure(figsize=(9, 5))

plt.bar(
    yearly_sales["Year"].astype(int).astype(str),
    yearly_sales["TotalSale"]
)

plt.title("Total Sales by Year")
plt.xlabel("Year")
plt.ylabel("Total Sales")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

plt.savefig(
    "charts/yearly_sales_comparison.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# Chart 3: Top five sales months

top_5_months = (
    monthly_sales.nlargest(5, "TotalSale")
    .copy()
    .sort_values("TotalSale")
)

plt.figure(figsize=(9, 5))

plt.barh(
    top_5_months["Period"],
    top_5_months["TotalSale"]
)

plt.title("Top 5 Months by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Year-Month")
plt.grid(axis="x", alpha=0.3)
plt.tight_layout()

plt.savefig(
    "charts/top_5_sales_months.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


print("\nAll analysis and charts completed successfully.")
