'''
Extremely Late Delivery, Hard DoorDash/Yelp Interview: https://platform.stratascratch.com/coding/2113-extremely-late-delivery?code_type=2

To remain competitive, the company you work with must reduce the number of extremely late deliveries.
A delivery is flagged as extremely late if the actual delivery time is more than 20 minutes (not inclusive) after the predicted delivery time.
You have been asked to calculate the percentage of orders that arrive extremely late each month.
Your output should include the month in the format 'YYYY-MM' and the percentage of extremely late orders as a percentage of all orders placed in that month.
'''

import pandas as pd
df=delivery_orders

#function to transform datetime to minutes:
def diff_mins(dt):
    return dt.hour * 60 + dt.minute

# Get time difference between the two timestamps:
df['order_convert'] = df['order_placed_time'].apply(diff_mins)
df['deliver_convert'] = df['actual_delivery_time'].apply(diff_mins)
df['Time_Mins']= df['deliver_convert']-df['order_convert']

# Get year and month of order date for a groupby later on:
df['date'] = df['order_placed_time'].dt.strftime('%Y-%m')

# Filter dataframe:
threshold = 20
filter_df = df[df['Time_Mins'] > threshold]

# Get Counts
distinct_df = filter_df.groupby(['date'])['delivery_id'].nunique().reset_index(name='LongOrders')
total_count_df = df.groupby(['date'])['delivery_id'].size().reset_index(name='total_count')

# Merge Counts to one dataframe:
merge_df = pd.merge(distinct_df, total_count_df, on=['date'])
merge_df['ratio'] = merge_df['LongOrders']/merge_df['total_count']
merge_df[['date','ratio']]
