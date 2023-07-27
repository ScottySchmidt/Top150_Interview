'''
Customer Revenue In March  https://platform.stratascratch.com/coding/9782-customer-revenue-in-march?code_type=2

Calculate the total revenue from each customer in March 2019. Include only customers who were active in March 2019.
Output the revenue along with the customer id and sort the results based on the revenue in descending order.
'''
import pandas as pd

orders.head()
df = orders
df['order_date'] = pd.to_datetime(df['order_date'])  # Convert the column to datetime dtype

# Filter by year and month
year_to_filter = 2019
month_to_filter = 3

filtered_df = df[(df['order_date'].dt.year == year_to_filter) & (df['order_date'].dt.month == month_to_filter)]

filtered_df = filtered_df.groupby('cust_id')['total_order_cost'].sum().reset_index(drop=False)
filtered_df=filtered_df.sort_values(by='total_order_cost',  ascending=False)



'''
# SQL_Server Solution
with cte as (
select cust_id, sum(total_order_cost) as total_revenue
FROM orders
WHERE year(order_date) = '2019'
AND month(order_date) = '3'
GROUP BY cust_id
)

SELECT cust_id, total_revenue
FROM cte
ORDER BY total_revenue DESC
;
'''
