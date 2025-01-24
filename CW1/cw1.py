import pandas as pd
# reading the file
df = pd.read_csv("/Users/badershalata/Documents/DataEngineeringCW/Datasets 2/rawpvr_2018-02-01_28d_1083 TueFri.csv")

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

# Noticed some rows had missing values for column ['Speed (mph)']
# First I had to see how many rows are missing, depending on number of rows there are different solutions
# Since only 2 rows had missing values, (small number of rows), one solution can be average of other rows
lane2_data = df[df['Lane'] == 2]
tuesday_data = lane2_data[lane2_data['Flag Text'] == 'Tuesday']
missing_speed_rows = tuesday_data[tuesday_data['Speed (mph)'].isna()]
avg_speed_tuesday = df[(df['Lane'] == 2) & (df['Flag Text'] == 'Tuesday')]['Speed (mph)'].mean()
df.loc[missing_speed_rows.index, 'Speed (mph)'] = avg_speed_tuesday
# Display rows with missing values in 'Speed'
print("Rows with missing 'Speed' values in Lane 2 on Tuesday:")
print(df.loc[missing_speed_rows.index])

# Save the DataFrame to a new CSV file
output_file = "/Users/badershalata/Documents/DataEngineeringCW/Datasets 2/updated_rawpvr_2018-02-01.csv"
df.to_csv(output_file, index=False)

total_traffic_weekday = df.groupby('Flag Text').size()
print(total_traffic_weekday)