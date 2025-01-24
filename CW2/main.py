import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis
import matplotlib.pyplot as plt
import seaborn as sns

# Task 5.I
# Filtered the data to Tuesday between 7AM - 19PM

df = pd.read_csv("/Users/badershalata/Documents/DataEngineeringCW/Datasets 2/updated_rawpvr_2018-02-01.csv")
df['Date'] = pd.to_datetime(df['Date'])
df = df[df['Flag Text'] == "Tuesday"]
df = df[(df['Date'].dt.hour >=7) & (df['Date'].dt.hour <19)]
number_of_cells = df.shape[0]
print("Number of all rows in Tuesday between 7AM - 19PM: ", number_of_cells)
missing_gap_rows = df[df['Gap (s)'].isna()]
print("Number of missing gap rows: ", missing_gap_rows.shape[0])
number_of_non_empty_cells = df['Gap (s)'].count()
print("number of non empty cells: ", number_of_non_empty_cells)

# Calculation of column completeness
column_completeness = (number_of_non_empty_cells*100)/ number_of_cells
print(column_completeness)



# Task 5.II
#This is for north lanes
print("THIS IS FOR NORTH LANES")
df1 = df[df['Direction'] ==1]
detailedProfile1 = df1['Gap (s)'].describe()
print(detailedProfile1)
skewness1 = skew(df1['Gap (s)'].dropna())
kurtosisness1 = kurtosis(df1['Gap (s)'].dropna())
print("Skewness: ", skewness1)
print("Kurtosis: ", kurtosisness1)
mode1 = df1['Gap (s)'].dropna().mode()[0]
median1 = df1['Gap (s)'].dropna().median()
print("MEDIAN: ", median1)
print("MODE1: ", mode1)
plt.figure(figsize=(12, 6))
sns.histplot(df1['Gap (s)'].dropna(), bins=30, kde=True, color='blue')
plt.title('Distribution of Gap (s) with KDE For North Lanes')
plt.xlabel('Gap (s)')
plt.ylabel('Frequency')
plt.annotate(f"Skewness: {skewness1:.2f}", xy=(0.75, 0.85), xycoords='axes fraction', fontsize=12)
plt.annotate(f"Kurtosis: {kurtosisness1:.2f}", xy=(0.75, 0.8), xycoords='axes fraction', fontsize=12)
plt.show()
# This profile is dedicated to the North Lane NB_MID only
print("THIS IS FOR NB_MID")
df2 = df[df['Lane'] == 2]
detailedProfile2 = df2['Gap (s)'].describe()
print(detailedProfile2)
skewness2 = skew(df2['Gap (s)'].dropna())
kurtosisness2 = kurtosis(df2['Gap (s)'].dropna())
median2 = df2['Gap (s)'].dropna().median()
mode2 = df2['Gap (s)'].dropna().mode()[0]
print("Skewness: ", skewness2)
print("Kurtosis: ", kurtosisness2)
print("MEDIAN2: ", median2)
print("MODE2: ", mode2)


plt.figure(figsize=(12, 6))
sns.histplot(df2['Gap (s)'].dropna(), bins=30, kde=True, color='blue')
plt.title('Distribution of Gap (s) with KDE For NB_MID')
plt.xlabel('Gap (s)')
plt.ylabel('Frequency')
plt.annotate(f"Skewness: {skewness2:.2f}", xy=(0.75, 0.85), xycoords='axes fraction', fontsize=12)
plt.annotate(f"Kurtosis: {kurtosisness2:.2f}", xy=(0.75, 0.8), xycoords='axes fraction', fontsize=12)
plt.show()

# Splitting Here (7AM-10AM)
df3 = df[df['Lane'] == 2]
df3 = df3[df3['Lane Name'] == "NB_MID"]
df3 = df3[(df3['Date'].dt.hour >= 7) & (df3['Date'].dt.hour <10)]
print(df3)
print("7AM-10AM PROFILE")
detailedProfile3 = df3['Gap (s)'].describe()
skewness3= skew(df3['Gap (s)'].dropna())
kurtosisness3 = kurtosis(df3['Gap (s)'].dropna())
median3 = df3['Gap (s)'].dropna().median()
mode3 = df3['Gap (s)'].dropna().mode()[0]

print(detailedProfile3)
print("Skewness: ", skewness3)
print("Kurtosis: ", kurtosisness3)
print("MEDIAN3: ", median3)
print("MODE3: ", mode3)

# Splitting Here (10AM-13PM)
df4 = df[df['Lane'] == 2]
df4 = df4[df4['Lane Name'] == "NB_MID"]
df4 = df4[(df4['Date'].dt.hour >=10) & (df4['Date'].dt.hour <13)]
print(df4)
print("10AM-13PM")
detailedProfile4 = df4['Gap (s)'].describe()
skewness4= skew(df4['Gap (s)'].dropna())
kurtosisness4 = kurtosis(df4['Gap (s)'].dropna())
median4 = df4['Gap (s)'].dropna().median()
mode4 = df4['Gap (s)'].dropna().mode()[0]


print(detailedProfile4)
print("Skewness: ", skewness4)
print("Kurtosis: ", kurtosisness4)
print("MEDIAN4: ", median4)
print("MODE4: ", mode4)

# Splitting here, (13PM-16PM)
df5 = df[df['Lane'] == 2]
df5 = df5[df5['Lane Name'] == "NB_MID"]
df5 = df5[(df5['Date'].dt.hour >=13) & (df5['Date'].dt.hour <16)]
print(df5)
print("13PM-16PM")
detailedProfile5 = df5['Gap (s)'].describe()
skewness5= skew(df5['Gap (s)'].dropna())
kurtosisness5 = kurtosis(df5['Gap (s)'].dropna())
median5 = df5['Gap (s)'].dropna().median()
mode5 = df5['Gap (s)'].dropna().mode()[0]

print(detailedProfile5)
print("Skewness: ", skewness5)
print("Kurtosis: ", kurtosisness5)
print("MEDIAN5: ", median5)
print("MODE5: ", mode5)



# Splitting here (16PM-19PM)
df6 = df[df['Lane'] == 2]
df6 = df6[df6['Lane Name'] == "NB_MID"]
df6 = df6[(df6['Date'].dt.hour >=16) & (df6['Date'].dt.hour <19)]
print(df6)
print("16PM-19PM")
detailedProfile6 = df6['Gap (s)'].describe()
skewness6= skew(df6['Gap (s)'].dropna())
kurtosisness6 = kurtosis(df6['Gap (s)'].dropna())
median6 = df6['Gap (s)'].dropna().median()
mode6 = df6['Gap (s)'].dropna().mode()[0]

print(detailedProfile6)
print("Skewness: ", skewness6)
print("Kurtosis: ", kurtosisness6)
print("MEDIAN6: ", median6)
print("MODE6: ", mode6)



# Function to plot figures
def plotfigure(dataframes, vars, hours):
    # 2x2 plot
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    axs = axs.flatten()

    # loop through all variables and dataframes
    for i, (dataframe, (varskew, varkurtosis), hour) in enumerate(zip(dataframes, vars, hours)):
        sns.histplot(dataframe['Gap (s)'].dropna(), bins=30, kde=True, color='blue', ax=axs[i])
        axs[i].set_title(f'Distribution of Gap (s) with KDE For NB_MID {hour}:00 - {hour + 3}:00')
        axs[i].set_xlabel('Gap (s)')
        axs[i].set_ylabel('Frequency')
        axs[i].annotate(f"Skewness: {varskew:.2f}", xy=(0.75, 0.85), xycoords='axes fraction', fontsize=12)
        axs[i].annotate(f"Kurtosis: {varkurtosis:.2f}", xy=(0.75, 0.8), xycoords='axes fraction', fontsize=12)

    plt.tight_layout()
    plt.show()

dataframes = [df3, df4, df5, df6]  # dataframes parts
details = [(skewness3,kurtosisness3),
           (skewness4, kurtosisness4), (skewness5, kurtosisness5), (skewness6,kurtosisness6)]
hours = [7, 10, 13,16]  # hours start
plotfigure(dataframes, details, hours)





