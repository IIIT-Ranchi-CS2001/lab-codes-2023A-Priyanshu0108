#First importing both the libraries
import pandas as pd
import numpy as np

#importing data set file
df = pd.read_csv('AQI_DATA.csv')

#display first 5 rows
print("Displaying first 5 rows")
print(df.head(5)) 
#display  last 6 rows
print("Displaying last 6 rows")
print(df.tail(6))
#show summary stats for all columns
print("showing the summary statistics")
print(df.describe())

# calculating the mean of AQI, PM 2.5 and PM 10
aqi_mean= np.mean(df['AQI'])
pm2_mean= np.mean(df['PM2.5'])
pm10_mean= np.mean(df['PM10'])
# print the mean of AQI, PM 2.5, PM 10
print("The mean of AQI is:")
print(aqi_mean)
print("The mean of PM 2.5 is:")
print(pm2_mean)
print("The mean of PM 10 is ")
print(pm10_mean)

#Calculating the average of AQI
average_aqi = df.groupby('City')['AQI'].agg(np.mean).reset_index()

# Printing the average of AQI
print("The average AQI of all cities is:")
print(average_aqi)

# Calculating the max PM 10 level
max_pm10 = df.groupby('City')['PM10'].agg(np.max).reset_index()
# Printing the max PM10 level
print("Maximum PM 10 level")
print(max_pm10)

# Merging the two previous data set
merged_data = pd.merge(average_aqi, max_pm10, on='City')

# Saving the merged data to a CSV file
merged_data.to_csv('AVERAGE_AQI_AND_PM_10.csv', index=False)

