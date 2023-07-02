'''
Extremely Late Delivery, Hard DoorDash/Yelp Interview: https://platform.stratascratch.com/coding/2113-extremely-late-delivery?code_type=2

To remain competitive, the company you work with must reduce the number of extremely late deliveries.
A delivery is flagged as extremely late if the actual delivery time is more than 20 minutes (not inclusive) after the predicted delivery time.
You have been asked to calculate the percentage of orders that arrive extremely late each month.
Your output should include the month in the format 'YYYY-MM' and the percentage of extremely late orders as a percentage of all orders placed in that month.
'''

# In Progress:
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
df['Month'] = df['order_placed_time'].dt.month
df['Year'] = df['order_placed_time'].dt.year

# Filter dataframe:
threshold = 20
filter_df = df[df['Time_Mins'] > threshold]

distinct_df = filter_df.groupby(['Year', 'Month'])['delivery_id'].nunique().reset_index(name='LongOrders')

total_count_df = df.groupby(['Year', 'Month'])['delivery_id'].size().reset_index(name='total_count')

merge_df = pd.merge(distinct_df, total_count_df, on=['Year', 'Month'])
merge_df.head()
