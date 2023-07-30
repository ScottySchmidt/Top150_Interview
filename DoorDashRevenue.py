'''
Lowest Revenue Generated Restaurants: https://platform.stratascratch.com/coding/2036-lowest-revenue-generated-restaurants?code_type=2

Write a query that returns a list of the bottom 2% revenue generating restaurants. 
Return a list of restaurant IDs and their total revenue from when customers placed orders in May 2020.
You can calculate the total revenue by summing the order_total column. And you should calculate the bottom 2% by partitioning the total revenue into evenly distributed buckets.
'''

import pandas as pd

search_year=2020
search_month=5

df = doordash_delivery[['placed_order_with_restaurant_datetime', 'restaurant_id', 'order_total']]

filtered_df = df[df['placed_order_with_restaurant_datetime'].dt.year == search_year]
filtered_df = df[df['placed_order_with_restaurant_datetime'].dt.month == search_month]


total_df = filtered_df.groupby('restaurant_id')['order_total'].sum().reset_index()

sorted_df = total_df.sort_values(by='order_total')
sorted_df.head()
