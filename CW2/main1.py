import pandas as pd
from scipy.stats import skew, kurtosis
import seaborn as sns
import matplotlib.pyplot as plt

# load and filter the data for Tuesday, 7AM - 19PM, NB_MID Lane
df = pd.read_csv("/Users/badershalata/Documents/DataEngineeringCW/Datasets 2/updated_rawpvr_2018-02-01.csv")
df['Date'] = pd.to_datetime(df['Date'])
df = df[df['Flag Text'] == "Tuesday"]
df = df[(df['Lane Name'] == 'NB_MID')]
df = df[(df['Date'].dt.hour >= 7) & (df['Date'].dt.hour < 19)]

# missing values number
print(f"Number of all rows in Tuesday between 7AM - 19PM: {df.shape[0]}")
print(f"Number of missing gap rows: {df['Gap (s)'].isna().sum()}")

# calculate mean, median
median_val = df['Gap (s)'].median()
mean_val = df['Gap (s)'].mean()

print("MEDIAN:", median_val)
print("MEAN:", mean_val)

# stats before insertion
detailed_profile_before = df['Gap (s)'].describe()
print("NB_MID before insertion:")
print(detailed_profile_before)

# fill missing values with the median
df_median_filled = df.copy()
df_median_filled['Gap (s)'] = df_median_filled['Gap (s)'].fillna(median_val)

# fill missing values with the mean
df_mean_filled = df.copy()
df_mean_filled['Gap (s)'] = df_mean_filled['Gap (s)'].fillna(mean_val)

# stats after median insertion
print("\nNB_MID after inserting median:")
print(df_median_filled['Gap (s)'].describe())

# stats after mean insertion
print("\nNB_MID after inserting mean:")
print(df_mean_filled['Gap (s)'].describe())

# plot comparison: before,after insertion of mean and median
plt.figure(figsize=(12, 6))
sns.kdeplot(df['Gap (s)'].dropna(), label="Before Insertion", color='blue')
sns.kdeplot(df_median_filled['Gap (s)'], label="After Median Insertion", color='green')
sns.kdeplot(df_mean_filled['Gap (s)'], label="After Mean Insertion", color='red')
plt.title('Comparison of Gap (s) Distribution: Before vs After Inserting Median and Mean')
plt.xlabel('Gap (s)')
plt.ylabel('Density')
plt.legend()
plt.show()
