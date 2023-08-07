'''
Growth of Airbnb:  Hard Data Analytics Question: https://platform.stratascratch.com/coding/9637-growth-of-airbnb?code_type=2
Estimate the growth of Airbnb each year using the number of hosts registered as the growth metric. 
The rate of growth is calculated by taking ((number of hosts registered in the current year - number of hosts registered in the previous year) / the number of hosts registered in the previous year) * 100.
Output the year, number of hosts in the current year, number of hosts in the previous year, and the rate of growth. 
Round the rate of growth to the nearest percent and order the result in the ascending order based on the year.
Assume that the dataset consists only of unique hosts, meaning there are no duplicate hosts listed.
'''

import pandas as pd

# Get the only filters needed:
df=airbnb_search_details[['host_since', 'id']]

# Get current year:
df['year'] = df['host_since'].dt.year

# Drop the old date column:
df.drop('host_since', axis=1, inplace=True)

#Get unique id count, group by year
unique_id_year = df.groupby('year')['id'].nunique().reset_index().rename(columns={'id': 'cur_id_count'})

#Calculate growth metric:
unique_id_year['prev_id_count'] = unique_id_year['cur_id_count'].shift(1).fillna(0)
unique_id_year['growth_metric'] = (unique_id_year['cur_id_count']-unique_id_year['prev_id_count'])/unique_id_year['prev_id_count']*100

unique_id_year['growth_metric']=unique_id_year['growth_metric'].round()
print(unique_id_year)
