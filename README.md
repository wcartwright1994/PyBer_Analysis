# PyBer_Analysis
Performing analysis on the ride sharing data by city type to create a multiple-line graph that shows the total weekly fares for each city type. This will be used to present the differences in rides per city type for decision-makers at PyBer.

**Overview of the PyBer Analysis**

The purpose of this analysis is to:
1. Create a formatted summary data table based on the city_data and rides_data datasets for Rural, Suburban, and Urban "types", including:
    * Total Rides
    * Total Drivers
    * Total Fares
    * Average Fare per Ride
    * Average Fare per Driver 
2. Pivot the data to create a multile-line graph to show the change in fares between January and April for each of the city types.

**PyBer Analysis Results**
Based on the summary data table created from joining the city_data and rides_data datasets, the following conclusions can be drawn:
1. Although total fares in Urban areas are higher than the other city types, averages fares are the lowest. This is consistent with the understanding that rides in Urban areas will have, on average, a lower distance than rides in other areas.
2. Across the board, there were less rides in the dataset than there were drivers. As the data was provided was for more than a 4 month period, this could be indicitive of an incomplete dataset. Additional inquiries to management could be needed to understand if there is additional datapoint that should be included.

Based on the line chart created by pivoting the dataset, the following conclusions can be drawn:
1. Fares peaked towards the end of Februrary across all city types and then sharply declined in the weeks that followed.
2. Although the chart shows a larger variance in fares in March in Urban areas, the percentage change was not as significant over this time period.

**PyBer Analysis Summary**
Based on the datasets provided, I would not be in any position to provide any specific business recommendations to the CEO to address disparities among the city types for the following reasons:
1. The dataset appears incomplete, incorrect, or hard to understand, as the sum of the driver_count field in city_data is less than the total number of rides in rides_data. This would mean each driver, on average, provided less than1 ride during this time period. This could, however, indicate that many more drivers are signed-up than actually provided rides.
2. Additional ride statistics should be provided, including length of trip in miles and time, to better understand the components of the fare.
3. The chart is misleading and shows that Urban areas have higher total fares, but have the lowest average fares. Additional charts should be created based on average fare and profit. This exercise does not consider cost to the company, so no real conclusions can be drawn.
