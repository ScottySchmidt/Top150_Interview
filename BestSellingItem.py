'''
Best Selling Item: https://platform.stratascratch.com/coding/10172-best-selling-item?code_type=2
Amazon, Ebay, Best Buy Interview question; Hard Level

Find the best selling item for each month (no need to separate months by year) where the biggest total invoice was paid. 
The best selling item is calculated using the formula (unitprice * quantity). 
Output the description of the item along with the amount paid.
'''
import pandas as pd

df = online_retail[['quantity', 'description','unitprice', 'invoicedate', 'stockcode']]

# Get Total
df['total']= online_retail['quantity']*online_retail['unitprice']

# Get month:
df['month'] = online_retail['invoicedate'].dt.month

# Only need these columns:
df=df[['total', 'month', 'stockcode' , 'description']]

# GroupBy month and total:
grouped_df = df.groupby(['month', 'stockcode', 'description'])['total'].sum().reset_index(drop=False)

# Find Max for each 
max_totals_by_month = grouped_df.groupby(['stockcode', 'description', 'month'])['total'].max().reset_index()
print(max_totals_by_month)
