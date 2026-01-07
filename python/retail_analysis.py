import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("D:\Data Analyst Project\Retail_Data_Analytics_Project\data\cleaned_data.csv")

print(df.head())
print(df.info())
total_revenue = df['Revenue'].sum()
total_customers = df['CustomerID'].nunique()
total_orders = df['InvoiceNo'].nunique()

print("Total Revenue:", total_revenue)
print("Total Customers:", total_customers)
print("Total Orders:", total_orders)
monthly_revenue = (
    df.groupby(['Year', 'Month'])['Revenue']
      .sum()
      .reset_index()
)

monthly_revenue['YearMonth'] = (
    monthly_revenue['Year'].astype(str) + '-' +
    monthly_revenue['Month'].astype(str)
)

plt.figure(figsize=(10,5))
plt.plot(monthly_revenue['YearMonth'], monthly_revenue['Revenue'])
plt.xticks(rotation=90)
plt.title('Monthly Revenue Trend')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.tight_layout()
plt.show()
top_products = (
    df.groupby('Description')['Revenue']
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(8,5))
top_products.plot(kind='bar')
plt.title('Top 10 Products by Revenue')
plt.ylabel('Revenue')
plt.tight_layout()
plt.show()
top_customers = (
    df.groupby('CustomerID')['Revenue']
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(8,5))
top_customers.plot(kind='bar')
plt.title('Top 10 Customers by Revenue')
plt.ylabel('Revenue')
plt.tight_layout()
plt.show()
orders_per_customer = (
    df.groupby('CustomerID')['InvoiceNo']
      .nunique()
)

plt.figure(figsize=(8,5))
orders_per_customer.hist(bins=30)
plt.title('Orders per Customer Distribution')
plt.xlabel('Number of Orders')
plt.ylabel('Customers')
plt.tight_layout()
plt.show()
last_purchase = df.groupby('CustomerID')['InvoiceDate'].max()

cutoff_date = df['InvoiceDate'].max() - pd.Timedelta(days=90)

churned_customers = last_purchase[last_purchase < cutoff_date]

print("Churned Customers:", churned_customers.count())
monthly_revenue.to_csv('../data/monthly_revenue.csv', index=False)
top_products.to_csv('../data/top_products.csv')





