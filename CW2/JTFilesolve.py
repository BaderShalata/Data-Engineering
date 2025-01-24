import pandas as pd
import numpy as np
# Task 6.I
# FRIDAY FOR SITE 1415, HOUR BETWEEN 17:00 - 18:00, NORTH LANES.
df1415 = pd.read_csv("/Users/badershalata/Documents/DataEngineeringCW/Datasets 2/updated_rawpvr_2018-02-01_1415.csv")
df1415['Date'] = pd.to_datetime(df1415['Date'])
df1415 = df1415[df1415['Flag Text'] == "Friday"]
df1415 = df1415[(df1415['Date'].dt.hour ==17)]
northLanes1415 = df1415[df1415['Direction'] == 1]
print(northLanes1415)
print(northLanes1415.shape[0])

# FRIDAY FOR SITE 1083, HOUR BETWEEN 17:00 - 18:00, NORTH LANES
df1083 = pd.read_csv("/Users/badershalata/Documents/DataEngineeringCW/Datasets 2/updated_rawpvr_2018-02-01.csv")
df1083['Date'] = pd.to_datetime(df1083['Date'])
df1083 = df1083[df1083['Flag Text'] == "Friday"]
df1083 = df1083[(df1083['Date'].dt.hour ==17)]
northLanes1083 = df1083[df1083['Direction'] == 1]
print(northLanes1083)
print(northLanes1083.shape[0])

# data integration of both dataframes to one
dfconcat = pd.concat([northLanes1415,northLanes1083])
dfconcat.to_csv("/Users/badershalata/Documents/DataEngineeringCW/Datasets 2/combinedcsv.csv", index=False)
print(dfconcat.shape[0])
# read the file we combined
twositesdf = pd.read_csv("/Users/badershalata/Documents/DataEngineeringCW/Datasets 2/combinedcsv.csv")
# calculate avg for all north lanes in both sites
avgspeed = twositesdf['Speed (mph)'].mean()
print(avgspeed)
# conversion speed mph to speed km/h
avgspeedkm = avgspeed * 1.60934
print("AVG SPEED IN KM: ", avgspeedkm)
# journey time calculation
JT = 4.86/avgspeedkm
# Journey time by minutes
print("Jounrey Time: ", JT*60)

# data quality checks
number_of_cells = twositesdf.shape[0]
missing_speed_rows = twositesdf[twositesdf['Speed (mph)'].isna()]
print("Missing speed values: ", missing_speed_rows.shape[0])
number_of_non_empty_cells = twositesdf['Speed (mph)'].count()
column_completeness = (number_of_non_empty_cells*100)/ number_of_cells
print(column_completeness)

