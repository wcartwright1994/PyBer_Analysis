# -*- coding: utf-8 -*-
"""
Created on Sun May 23 00:29:17 2021

@author: Billy
"""

# Add Matplotlib inline magic command
#%matplotlib inline
# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd

# File to Load (Remember to change these)
city_data_to_load = r"C:\Users\Billy\Documents\Bootcamp - Module 5\city_data.csv"
ride_data_to_load = r"C:\Users\Billy\Documents\Bootcamp - Module 5\ride_data.csv"

# Read the City and Ride Data
city_data_df = pd.read_csv(city_data_to_load)
ride_data_df = pd.read_csv(ride_data_to_load)

# Combine the data into a single dataset
pyber_data_df = pd.merge(ride_data_df, city_data_df, how="left", on=["city", "city"])

# Display the data table for preview
pyber_data_df.head()

for col in pyber_data_df:
    print(col)

print('\n----\n')
#  1. Get the total rides for each city type
print('total_rides')
total_rides = pyber_data_df.groupby(['type']).count().rename(columns={'ride_id':'Total Rides'})['Total Rides'].reset_index()
print(total_rides)

print('\n----\n')

# 2. Get the total drivers for each city type
print('total_drivers')
total_drivers = pyber_data_df.groupby(['type']).sum(['driver_count']).rename(columns={'driver_count':'Total Drivers'})['Total Drivers'].reset_index()
print(total_drivers)

print('\n----\n')

#  3. Get the total amount of fares for each city type
print('total_fare')
total_fare = pyber_data_df.groupby('type').sum('fare').rename(columns={'fare':'Total Fares'})['Total Fares'].reset_index()
print(total_fare)

print('\n----\n')

#  4. Get the average fare per ride for each city type. 
print('avg_fare')
avg_fare = pyber_data_df.groupby(['type']).mean(['fare']).rename(columns={'fare':'Average Fare per Ride'})['Average Fare per Ride'].reset_index()
print(avg_fare)

print('\n----\n')

# 5. Get the average fare per driver for each city type. 
###done below in combined output

#  6. Create a PyBer summary DataFrame. 
pyber_summary_df = pd.merge(total_rides, total_drivers,how='left',on=['type'])
pyber_summary_df = pd.merge(pyber_summary_df,total_fare,how='left',on=['type'])
pyber_summary_df = pd.merge(pyber_summary_df,avg_fare,how='left',on=['type'])

pyber_summary_df['Average Fare per Driver'] = pyber_summary_df['Total Fares']/pyber_summary_df['Total Drivers']

print(pyber_summary_df)
#  7. Cleaning up the DataFrame. Delete the index name
###pyber_summary_df.index.name = None
###already done above
#  8. Format the columns.

# 1. Read the merged DataFrame
print(pyber_data_df.head())

# 2. Using groupby() to create a new DataFrame showing the sum of the fares 
#  for each date where the indices are the city type and date.
df = pyber_data_df.groupby(['type','date']).sum('fare').rename(columns={'fare':'Total Fares'})['Total Fares']
#print(grouped_df)
# 3. Reset the index on the DataFrame you created in #1. This is needed to use the 'pivot()' function.
df = df.reset_index()
print(df)

# 4. Create a pivot table with the 'date' as the index, the columns ='type', and values='fare' 
# to get the total fares for each type of city by the date. 
df = df.pivot('date','type','Total Fares').reset_index()
print(df)

df['date'] = pd.to_datetime(df['date'],format='%Y-%m-%d %H:%M:%S')
print(df.dtypes)
# 5. Create a new DataFrame from the pivot table DataFrame using loc on the given dates, '2019-01-01':'2019-04-29'.
df = df[(df['date'] >= '2019-01-01') & (df['date'] < '2019-04-30')]
print(df)

# 6. Set the "date" index to datetime datatype. This is necessary to use the resample() method in Step 8.
# df.index = pd.to_datetime(df.index)
df = df.set_index('date')

# 7. Check that the datatype for the index is datetime using df.info()
df.info()

# 8. Create a new DataFrame using the "resample()" function by week 'W' and get the sum of the fares for each week.
df = df.resample('W').sum()
print(df)
# 8. Using the object-oriented interface method, plot the resample DataFrame using the df.plot() function. 
df.plot()
plt.title('Total Fare by City Type')
plt.ylabel('Fare ($USD)')
# Import the style from Matplotlib.
from matplotlib import style
# Use the graph style fivethirtyeight.
style.use('fivethirtyeight')

plt.savefig(r'C:\Users\Billy\Documents\Bootcamp - Module 5\PyBer_fare_summary.png')


