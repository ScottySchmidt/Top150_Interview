'''
Best Selling Item: https://platform.stratascratch.com/coding/10172-best-selling-item?code_type=2
Amazon, Ebay, Best Buy Interview question; Hard Level

Find the best selling item for each month (no need to separate months by year) where the biggest total invoice was paid. 
The best selling item is calculated using the formula (unitprice * quantity). 
Output the description of the item along with the amount paid.
'''
import pandas as pd

df = online_retail[['quantity', 'unitprice', 'invoicedate']]

# New Total Column
df['total'] = df['quantity'] * df['unitprice']

# Extracting the month from the invoicedate column
df['month'] = df['invoicedate'].dt.month

# Find the index of the maximum total within each month
idx = df.groupby('month')['total'].idxmax()

# Use the index to retrieve the entire row, including the original unitprice
best_selling_items = df.loc[idx]

print(best_selling_items[['month', 'unitprice', 'total']])


# SQL_Server and mySQL Solution:
'''
with month_sales as ( 
select stockcode, description, sum(quantity*unitprice) as month_total,
month(invoicedate) as month 
FROM online_retail 
GROUP BY stockcode, description, month(invoicedate)
)

SELECT month, stockcode, description, max(month_total) as max_month_total
FROM month_sales
GROUP BY stockcode, description, month
'''
