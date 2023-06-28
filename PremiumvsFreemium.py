'''
Premium vs Freemium, Hard Microsoft Data Analyst: https://platform.stratascratch.com/coding/10300-premium-vs-freemium?code_type=2

Find the total number of downloads for paying and non-paying users by date. Include only records where non-paying customers have more downloads than paying customers. 
The output should be sorted by earliest date first and contain 3 columns date, non-paying downloads, paying downloads.
DataFrames: ms_user_dimension, ms_acc_dimension, ms_download_factsExpected Output Type: pandas.DataFrame
'''
# Final Correct Solution:
import pandas as pd

# Three Datasets:
df = ms_user_dimension
df2= ms_acc_dimension
df3= ms_download_facts

# Join Datasets:
mergeDF = pd.merge(df, df2, on="acc_id")
mergeDF = pd.merge(mergeDF, df3, on="user_id")
#mergeDF.head()

# Use Group By:
#groupDF=mergeDF.groupby(['date', 'paying_customer'])['downloads'].sum()

# Use Group By:
groupDF=mergeDF.groupby(['date', 'paying_customer']).agg({'downloads': 'sum'}).unstack()# unstack will act as a pivot
groupDF=groupDF.reset_index().sort_values('date')
#print(groupDF.columns) #MultiIndex([(date',''),   ('downloads',  'no'),  ('downloads', 'yes')]

# Rename the columns directly
groupDF.columns = ['date', 'free',  'paying']

#Include only records where non-paying customers have more downloads than paying customers:
groupDF['diff'] = groupDF['free']-groupDF['paying'].fillna(0)
rslt_df = groupDF[groupDF['diff'] > 0]
rslt_df[['date', 'free',  'paying']]



# Initial Draft Solution Passes half of the rows correctly:
import pandas as pd

# Three Datasets:
df = ms_user_dimension
df2= ms_acc_dimension
df3= ms_download_facts

# Join Datasets:
mergeDF = pd.merge(df, df2, on="acc_id")
mergeDF = pd.merge(mergeDF, df3, on="user_id")
#mergeDF.head()

# Use Group By:
groupDF=mergeDF.groupby(['date', 'paying_customer'])['downloads'].sum()

# Three Datasets:
df = ms_user_dimension
df2= ms_acc_dimension
df3= ms_download_facts

# Join Datasets:
mergeDF = pd.merge(df, df2, on="acc_id")
mergeDF = pd.merge(mergeDF, df3, on="user_id")
#mergeDF.head()

# Use Group By:
groupDF=mergeDF.groupby(['date', 'paying_customer']).agg({'downloads': 'sum'}).unstack() # unstack will act as a pivot
groupDF=groupDF.reset_index().sort_values('date')
