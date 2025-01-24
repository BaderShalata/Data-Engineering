import pandas as pd
import numpy as np
df = pd.read_csv("/Users/badershalata/Documents/DataEngineeringCW/Datasets 2/rawpvr_2018-02-01_28d_1415 TueFri.csv")
print(df)
# THIS FILE IS JUST TO FILL IN FLAG TEXT AND FLAG COLUMNS
# function to prepare the data as some rows had different format
# (Were missing the %f factor)
def parse_dates(date_str):
    try:
        # first attempt with the first format
        return pd.to_datetime(date_str, format='%Y-%m-%d %H:%M:%S', errors='raise')
    except ValueError:
        # If that fails, try the second format
        return pd.to_datetime(date_str, format='%Y-%m-%d %H:%M:%S.%f', errors='coerce')

# apply the function to the 'Date' column
df['Date'] = df['Date'].apply(parse_dates)

# set the weekday name
df['Flag Text'] = df['Date'].dt.day_name()
# map the ['Flag'] to the day
daymapping = {"Tuesday" : 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6, "Sunday": 7, "Monday": 1}

df['Flags'] = df['Flag Text'].map(daymapping)
# Save the DataFrame to a new CSV file
output_file = "/Users/badershalata/Documents/DataEngineeringCW/Datasets 2/updated_rawpvr_2018-02-01_1415.csv"
df.to_csv(output_file, index=False)
