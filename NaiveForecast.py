'''
Naive Forecasting, Hard Problem: https://platform.stratascratch.com/coding?code_type=2

Some forecasting methods are extremely simple and surprisingly effective. Naïve forecast is one of them; we simply set all forecasts to be the value of the last observation. 
Our goal is to develop a naïve forecast for a new metric called "distance per dollar" defined as the (distance_to_travel/monetary_cost) in our dataset and measure its accuracy.

To develop this forecast,  sum "distance to travel"  and "monetary cost" values at a monthly level before calculating "distance per dollar". This value becomes your actual value for the current month. The next step is to populate the forecasted value for each month. 
This can be achieved simply by getting the previous month's value in a separate column. Now, we have actual and forecasted values.
This is your naïve forecast. Let’s evaluate our model by calculating an error matrix called root mean squared error (RMSE). RMSE is defined as sqrt(mean(square(actual - forecast)). Report out the RMSE rounded to the 2nd decimal spot.
'''
import pandas as pd

#uber_request_logs.head()
df = uber_request_logs
df = df.sort_values('request_date')
df = df.fillna(0)
df['month_year'] = df['request_date'].dt.strftime("%B %Y")
df1 = df.groupby('month_year')['monetary_cost'].sum().reset_index()
df2 = df.groupby('month_year')['driver_to_client_distance'].sum().reset_index()

finalDF = df1.merge(df2, on='month_year')

finalDF['distance per dollar'] = finalDF['driver_to_client_distance']/finalDF['monetary_cost']
finalDF['previous_distance_per_dollar'] = finalDF['distance per dollar'].shift(1)
finalDF.head()
