'''
The Cheapest Airline Connection, Delta Airlines:
https://platform.stratascratch.com/coding/2008-the-cheapest-airline-connection?code_type=5

COMPANY X employees are trying to find the cheapest flights to upcoming conferences. 
When people fly long distances, a direct city-to-city flight is often more expensive than taking two flights with a stop in a hub city. Travelers might save even more money by breaking the trip into three flights with two stops. But for the purposes of this challenge, let's assume that no one is willing to stop three times! You have a table with individual airport-to-airport flights, which contains the following columns:

• id - the unique ID of the flight;
• origin - the origin city of the current flight;
• destination - the destination city of the current flight;
• cost - the cost of current flight.

Your task is to produce a trips table that lists all the cheapest possible trips that can be done in two or fewer stops.
This table should have the columns origin, destination and total_cost (cheapest one). 
Sort the output table by origin, then by destination. 
The cities are all represented by an abbreviation composed of three uppercase English letters. 
Note: A flight from SFO to JFK is considered to be different than a flight from JFK to SFO.

Example of the output:
origin | destination | total_cost
DFW | JFK | 200
'''
import pandas as pd

#original dataframe
df = da_flights

#NO STOP, DIRECT FLIGHT:
no_stop = df
no_stop['route'] = no_stop['origin'] + ' -> ' + no_stop['destination']

#ONE STOP DF:
one_stop= pd.merge(df, df, left_on='origin', right_on='destination')
one_stop['total_cost'] = one_stop['cost_x'] + one_stop['cost_y']
one_stop['route'] = one_stop['origin_x'] + ' -> '+ one_stop['destination_y']

#TWO STOP:
two_stop= pd.merge(df, df, left_on='origin', right_on='destination')
two_stop= pd.merge(two_stop, df, left_on='destination_y', right_on='origin')
two_stop['total_cost'] = two_stop['cost_x'] + two_stop['cost_y'] + two_stop['cost']
two_stop['route'] = two_stop['origin_x'] + ' -> '+ two_stop['destination_y'] + ' -> ' + two_stop['destination']
two_stop = two_stop[['origin_x', 'destination', 'total_cost', 'route']].rename(columns={'origin_x': 'origin', 'destination': 'destination', 'total_cost': 'cost'})

#COMBINE ALL THREE DATASETS, need same column name:
no_stop = no_stop[['origin', 'destination', 'cost', 'route']]
one_stop = one_stop[['origin_x', 'destination_y', 'total_cost']].rename(columns={'origin_x': 'origin', 'destination_y': 'destination', 'total_cost': 'cost'})

result_df = pd.concat([no_stop, one_stop, two_stop]).drop_duplicates().reset_index(drop=True)

# Group by 'origin' and 'destination', find the minimum cost, and keep the 'route' column
three_df = df[df['origin'] != df['destination']].groupby(['origin', 'destination'])[['cost', 'route']].agg({'cost': 'min', 'route': 'first'}).reset_index()

return three_df

''' 
FINAL OUTPUT WITH ARROWS:
origin	destination	cost	route
DFW	JFK	200	DFW -> JFK
DFW	MCO	100	DFW -> MCO
JFK	LHR	1000	JFK -> LHR
SFO	DFW	200	SFO -> DFW
SFO	JFK	500	SFO -> JFK
SFO	MCO	400	SFO -> MCO
'''



#SQL Server and MySQL Solution:
with one_stop as (
SELECT 	a.origin as first_origin,
a.destination as first_dest, 
a.cost as cost1, 
b.origin as second_origin, 
b.destination as second_dest, 
b.cost as cost2,
a.cost+b.cost as total_cost,
concat(a.origin, ' -> ', b.destination) as route
FROM da_flights a, da_flights b
WHERE a.destination = b.origin
),

two_stop as (
SELECT 	a.origin as first_origin,
a.destination as first_dest, 
a.cost as cost1, 
b.origin as second_origin, 
b.destination as second_dest, 
b.cost as cost2,
c.origin as third_origin, 
c.destination as third_dest,
c.cost,
a.cost+b.cost+c.cost as total_cost,
concat(a.origin, ' -> ', b.destination, ' -> ', c.destination)  as route
FROM da_flights a, da_flights b, da_flights c
WHERE a.destination = b.origin
AND b.origin = c.destination
),

final_flights as (
SELECT origin, destination, cost as total_cost, concat(origin, ' -> ' , destination) as route
FROM da_flights
UNION ALL
SELECT first_origin, second_dest, total_cost, route
FROM one_stop
UNION ALL
SELECT first_origin, third_dest, total_cost, route
FROM two_stop)

SELECT origin, destination, min(total_cost) as cheapest_flight, min(route) as route
FROM final_flights
GROUP BY origin, destination
ORDER BY cheapest_flight
