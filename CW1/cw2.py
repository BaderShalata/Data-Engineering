import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Before start working on the Task, many Data preparation steps here:
# (1) some rows had different ['Date'] formats (Some missing %f format - milliseconds),
# so had to parse them into one function to read correctly
# (2) Filling values in ['Flag'] and ['Flag Text'] columns from ['Date'] extraction
# This is done to group/filter rows correctly
# (3) New pipeline: from the raw data (Installed from blackboard)
# I loaded the new updated data (with Flag, Flag text columns) into a new csv file
# (4) Some rows had missing values in the ['Speed (mph)'] column (INCOMPLETE DATA!),
# There are many ways to fix this issue, my solution:
# Since for my task, only 2 rows had missing values - not too many missing values,
# I calculated the average for all relevant other rows
# and input the average onto the missing values
# All steps above were done in file cw1.py

# Task 2.I
df = pd.read_csv("/Users/badershalata/Documents/DataEngineeringCW/Datasets 2/updated_rawpvr_2018-02-01.csv")
# Here, we have another data preparation step:
# To actually start working on the data, I need to filter it to the task goal
# Here I filter only Tuesday
tuesday_only_data = df[df['Flag Text'] == 'Tuesday'].copy()
# Make Date do day time
tuesday_only_data['Date'] = pd.to_datetime(tuesday_only_data['Date'])
# Here, I filter between 9 am to less than 10 am range
tuesday_only_data = tuesday_only_data[(tuesday_only_data['Date'].dt.hour == 9)
                                      & (tuesday_only_data['Date'].dt.minute < 60)]
print("Filtered only 9am to 10 am", tuesday_only_data)
# NORTH LANES
# Filter North Lanes only (Their Direction column is equal to 1)
north_lanes = tuesday_only_data[tuesday_only_data['Direction'] == 1]
print(north_lanes)
# This is the DDS report profiling that has Range, Q1, Q2, Q3 and IQR
NorthDDS = north_lanes.groupby('Lane')['Speed (mph)'].agg(
    Range = lambda x:x.max() - x.min(),
    Q1 = lambda x: np.percentile(x,25),
    Q2 = lambda x: np.percentile(x,50),
    Q3 = lambda x: np.percentile(x, 75),
    IQR = lambda x: np.percentile(x, 75) - np.percentile(x,25)
)
print("NORTH LANE SPEED DDS")
print(NorthDDS)
print()
# Task 2.II
# SOUTH LANES
# Same as before, this DDS reports Range, Q1, Q2, Q3 and IQR
# South Lanes direction == 2
south_lanes = tuesday_only_data[tuesday_only_data['Direction'] == 2]
SouthDDS = south_lanes.groupby('Lane')['Speed (mph)'].agg(
    SouthRange = lambda x: x.max() - x.min(),
    SouthQ1 = lambda x: np.percentile(x,25),
    SouthQ2 = lambda x: np.percentile(x,50),
    SouthQ3 = lambda x: np.percentile(x,75),
    SouthIQR = lambda x: np.percentile(x,75) - np.percentile(x,25)
)
print("SOUTH LANE SPEED DDS")
print(SouthDDS)
print()


# Task 2.III
# For this task, to actually get to calculate DDS measures for each individual lane
# I have split the data into 3 time intervals, 9AM - 9:20AM, 9:20AM - 9:40AM and 9:40 AM - 10:00AM
# Reason for doing this is to obtain different values for each lane which I can then
# calculate DDS measures for each individual lane
# E.g:
# Lane 1 size(traffic volume) at 9AM - 9:20 AM - 10 cars
# Lane 1 size(traffic volume) at 9:20AM - 9:40 AM - 15 cars
# Lane 1 size(traffic volume) at 9:40AM - 10:00 AM - 18 cars
# From the example above I can then calculate DDS measures for traffic volume for Lane 1, on Tuesday, in this specific hour.
print("TASK 2.III")
# North Lanes
task3north = tuesday_only_data.copy()
# Direction of North Lanes == 1
task3north = task3north[task3north['Direction'] == 1]

# Split time -> Group By North Lanes
task3dffirstpart_north = task3north[(task3north['Date'].dt.hour == 9) & (task3north['Date'].dt.minute < 20)]
task3dffirstpart_north = task3dffirstpart_north.groupby('Lane')

task3dfsecondpart_north = task3north[(task3north['Date'].dt.hour == 9) & (task3north['Date'].dt.minute >= 20) & (task3north['Date'].dt.minute < 40)]
task3dfsecondpart_north = task3dfsecondpart_north.groupby('Lane')

task3dfthirdpart_north = task3north[(task3north['Date'].dt.hour == 9) & (task3north['Date'].dt.minute >= 40) & (task3north['Date'].dt.minute < 60)]
task3dfthirdpart_north = task3dfthirdpart_north.groupby('Lane')

# Filter South lanes
task3south = tuesday_only_data.copy()
task3south = task3south[task3south['Direction'] == 2]  # Assuming '2' is the South direction

# Split time -> Group By South Lanes
task3dffirstpart_south = task3south[(task3south['Date'].dt.hour == 9) & (task3south['Date'].dt.minute < 20)]
task3dffirstpart_south = task3dffirstpart_south.groupby('Lane')

task3dfsecondpart_south = task3south[(task3south['Date'].dt.hour == 9) & (task3south['Date'].dt.minute >= 20) & (task3south['Date'].dt.minute < 40)]
task3dfsecondpart_south = task3dfsecondpart_south.groupby('Lane')

task3dfthirdpart_south = task3south[(task3south['Date'].dt.hour == 9) & (task3south['Date'].dt.minute >= 40) & (task3south['Date'].dt.minute < 60)]
task3dfthirdpart_south = task3dfthirdpart_south.groupby('Lane')


# Function to calculate DDS Measures and collect Q1, Q2, and Q3 values for plotting
def DDSMeasure(taskDirection1, taskDirection2, taskDirection3, number, lanes, Q1north, Q2north,
               Q3north, rangenorth, IQRnorth):
    for i in range(number, number + 3):
        firstpartLane = taskDirection1.size().get(i, 0)
        secondpartLane = taskDirection2.size().get(i, 0)
        thirdpartLane = taskDirection3.size().get(i, 0)

        lanes.append(f'Lane {i}')

        Lanesize = np.array([firstpartLane, secondpartLane, thirdpartLane])
        print("Lane Size [First Third, Second Third, Last Third] of the hour: ", Lanesize)
        maxVal = Lanesize.max()
        minVal = Lanesize.min()
        rangeVal = maxVal - minVal
        Q1 = np.percentile(Lanesize, 25)
        Q2 = np.percentile(Lanesize, 50)
        Q3 = np.percentile(Lanesize, 75)
        IQR = Q3 - Q1

        rangenorth.append(rangeVal)
        Q1north.append(Q1)
        Q2north.append(Q2)
        Q3north.append(Q3)
        IQRnorth.append(IQR)

        print(f"Q1 Lane {i}: {Q1}, Q2 Lane {i}: {Q2}, Q3 Lane {i}: {Q3}\n")


# lists for north lane for plotting
lanes_north = []
rangenorth = []
Q1north = []
Q2north = []
Q3north = []
IQRnorth = []

print("NORTH LANES")
# calculate DDS Measures for North lanes (Q1, Q2, and Q3 values)
DDSMeasure(task3dffirstpart_north, task3dfsecondpart_north, task3dfthirdpart_north, 1, lanes_north,
           Q1north, Q2north, Q3north, rangenorth, IQRnorth)

x = np.arange(5)
bar_width = 0.2

plt.figure(figsize=(12, 6))

# loop through each lane and plot
for i, lane in enumerate(lanes_north):
    plt.bar(x + i * bar_width, [rangenorth[i], Q1north[i], Q2north[i], Q3north[i], IQRnorth[i]],
            width=bar_width, label=f'{lane}')

plt.xticks(x + bar_width, ['Range', 'Q1', 'Q2', 'Q3', 'IQR'])

# labels and titles
plt.xlabel('DDS')
plt.ylabel('Traffic Volume (North)')
plt.title('Task 2.III - Traffic Volume DDS Measures For Each North Lane')
plt.legend(title='Lanes')
plt.tight_layout()
plt.yticks(range(0, 1500, 100))
plt.grid()
plt.show()

# South Lanes
# Function to calculate DDS Measures and collect Q1, Q2, Q3 values for plotting
def DDSMeasure(taskDirection1, taskDirection2, taskDirection3, number, lanes, Q1south, Q2south,
               Q3south, rangesouth, IQRsouth):
    for i in range(number, number + 3):
        firstpartLane = taskDirection1.size().get(i, 0)
        secondpartLane = taskDirection2.size().get(i, 0)
        thirdpartLane = taskDirection3.size().get(i, 0)

        lanes.append(f'Lane {i}')
        Lanesize = np.array([firstpartLane, secondpartLane, thirdpartLane])
        print("Lane Size [First Third, Second Third, Last Third] of the hour: ", Lanesize)
        maxVal = Lanesize.max()
        minVal = Lanesize.min()
        rangeVal = maxVal - minVal

        Q1 = np.percentile(Lanesize, 25)
        Q2 = np.percentile(Lanesize, 50)
        Q3 = np.percentile(Lanesize, 75)
        IQR = Q3 - Q1

        rangesouth.append(rangeVal)
        Q1south.append(Q1)
        Q2south.append(Q2)
        Q3south.append(Q3)
        IQRsouth.append(IQR)

        print(f"Q1 Lane {i}: {Q1}, Q2 Lane {i}: {Q2}, Q3 Lane {i}: {Q3}\n")


# lists for south lane for plotting
lanes_south = []
rangesouth = []
Q1south = []
Q2south = []
Q3south = []
IQRsouth = []

print("SOUTH LANES")
# calculate DDS Measures for South lanes (Q1, Q2, and Q3 values)
DDSMeasure(task3dffirstpart_south, task3dfsecondpart_south, task3dfthirdpart_south, 4, lanes_south,
           Q1south, Q2south, Q3south, rangesouth, IQRsouth)

x_south = np.arange(5)
bar_width = 0.2

plt.figure(figsize=(12, 6))

# plot bars for each lane
for i, lane in enumerate(lanes_south):
    plt.bar(x_south + i * bar_width, [rangesouth[i], Q1south[i], Q2south[i], Q3south[i], IQRsouth[i]],
            width=bar_width, label=f'{lane}')

# x axis names
plt.xticks(x_south + bar_width, ['Range', 'Q1', 'Q2', 'Q3', 'IQR'])

# labels and titles
plt.xlabel('DDS')
plt.ylabel('Traffic Volume (South)')
plt.title('Task 2.III - Traffic Volume DDS Measures For Each South Lane')
plt.legend(title='Lanes')
plt.tight_layout()
plt.yticks(range(0, 1500, 100))
plt.grid()
plt.show()



#Task 3.I
# Created a function to get the relevant rows depending on the day
# Then make a time interval between 7AM and 11:59PM
# grouped them by hour to calculate each hour traffic volume
# then, calculated the mean (average per hour)
def avghourFunc(day):
    dfday = df[df['Flag Text'] == day].copy()
    dfday['Date'] = pd.to_datetime(dfday['Date'])
    dfday['Hour'] = dfday['Date'].dt.hour
    dfday_hour_filtered = dfday[(dfday['Hour'] >= 7) & (dfday['Hour'] <= 23)]
    dfday_avgtraffic = dfday_hour_filtered.groupby('Hour').size()

    print(dfday_hour_filtered)
    print(day)
    print(dfday_avgtraffic)
    print("AVG: ", dfday_avgtraffic.mean())
    return dfday_avgtraffic
avg_traffic_tuesday = avghourFunc("Tuesday")
avg_traffic_friday = avghourFunc("Friday")

plt.figure(figsize=(10, 6))
# plotting Tuesday
plt.plot(avg_traffic_tuesday.index, avg_traffic_tuesday.values, marker='o', color='blue', label='Tuesday',
         linestyle='-')
# plotting Friday
plt.plot(avg_traffic_friday.index, avg_traffic_friday.values, marker='o', color='orange', label='Friday', linestyle='-')
# tuesday & friday averages
avg_tuesday = avg_traffic_tuesday.mean()
avg_friday = avg_traffic_friday.mean()
# horizontal average
plt.axhline(avg_tuesday, color='blue', linestyle='-', label=f'Average Tuesday: {avg_tuesday:.2f}')
plt.axhline(avg_friday, color='orange', linestyle='-', label=f'Average Friday: {avg_friday:.2f}')
# labels and title
plt.title('Task 3.I - Average Hourly Traffic Volume (7 AM to 11 PM)')
plt.xlabel('Hour')
plt.ylabel('Traffic Volume')
plt.yticks(range(0, 25000, 1000))
plt.xticks(avg_traffic_tuesday.index)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()




