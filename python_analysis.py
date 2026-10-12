
import pandas as pd

file_path = "data/Online Retail.xlsx"
df = pd.read_excel(file_path)

# Calculate sales revenue
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

print("===== E-COMMERCE SALES ANALYSIS =====")

# Total transactions
print("\nTotal Records:", len(df))

# Total revenue
print("Total Revenue: £", round(df["Revenue"].sum(), 2))

# Top 10 products by quantity sold
valid_sales = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]

top_products = (
    valid_sales.groupby("Description")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Products by Quantity Sold:")
print(top_products)

# Sales by country
country_sales = (
    valid_sales.assign(
        Revenue=valid_sales["Quantity"] * valid_sales["UnitPrice"]
    )
    .groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Countries by Revenue:")
print(country_sales.round(2))

# Monthly Sales Analysis
valid_sales = valid_sales.copy()

valid_sales["InvoiceDate"] = pd.to_datetime(valid_sales["InvoiceDate"])
valid_sales["Revenue"] = (
    valid_sales["Quantity"] * valid_sales["UnitPrice"]
)

valid_sales["Month"] = (
    valid_sales["InvoiceDate"].dt.to_period("M").astype(str)
)

monthly_sales = valid_sales.groupby("Month")["Revenue"].sum()

print("\n===== MONTHLY SALES ANALYSIS =====")
print(monthly_sales.round(2))

import matplotlib.pyplot as plt

# Create Monthly Sales Chart
plt.figure(figsize=(12, 6))
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly E-Commerce Sales Analysis")
plt.xlabel("Month")
plt.ylabel("Revenue (£)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

plt.savefig("monthly_sales_chart.png")
plt.show()

# Country-wise Sales Chart
country_sales = (
    valid_sales.groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 6))
country_sales.sort_values().plot(kind="barh")

plt.title("Top 10 Countries by Revenue")
plt.xlabel("Revenue (£)")
plt.ylabel("Country")
plt.tight_layout()

plt.savefig("country_sales_chart.png")
plt.show()


