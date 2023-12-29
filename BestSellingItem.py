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

return best_selling_items[['month', 'unitprice', 'total']]


# SQL YouTube Solution: https://www.youtube.com/watch?v=ON61CG7BvGs
# My SQL Solution:
with items as(SELECT month(invoicedate) as month, description, 
sum(unitprice * quantity) as total_sales,
dense_rank() OVER(PARTITION BY month(invoicedate) ORDER BY sum(unitprice * quantity) DESC) as ranked
FROM online_retail
GROUP BY month(invoicedate), description
)

# Select final table with rank 1 and change month to 01 format:
SELECT LPAD(month, 2, "0") as month, description, total_sales
FROM items
WHERE ranked =1
