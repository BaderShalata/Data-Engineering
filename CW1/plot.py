from cw2 import *
import matplotlib.pyplot as plt
#PLOTTING FOR TASKS 2.I & 2.II
#NORTH LANE SPEED
lanes = NorthDDS.index
ranges = NorthDDS['Range']
q1 = NorthDDS['Q1']
q2 = NorthDDS['Q2']
q3 = NorthDDS['Q3']
qiqr = NorthDDS['IQR']
x = np.arange(len(lanes))
width = 0.1

plt.figure(figsize=(10, 6))
plt.title('Task 2.I - North Lane Speed DDS')
plt.xlabel("Lanes")
plt.ylabel("Values")

plt.bar(x - width, q1, width, label='Q1', color='lightblue')
plt.bar(x, q2, width, label='Q2 (Median)', color='orange')
plt.bar(x + width, q3, width, label='Q3', color='lightgreen')
plt.bar(x + 2*width, qiqr, width, label='IQR', color='black')
plt.bar(x + 3*width, ranges, width, label='Range', color='wheat')
plt.xticks(x + width, ['Lane 1', 'Lane 2', 'Lane 3'])
plt.ylim(0, 120)
y_ticks = np.arange(0, 120, 5)
plt.yticks(y_ticks)
plt.legend()

# SOUTH LANE SPEED
# Extract lanes and quartiles from NorthDDS
lanes = SouthDDS.index
ranges = SouthDDS['SouthRange']
q1s = SouthDDS['SouthQ1']
q2s = SouthDDS['SouthQ2']
q3s = SouthDDS['SouthQ3']
qiqrs = SouthDDS['SouthIQR']
x = np.arange(len(lanes))
width = 0.1
plt.figure(figsize=(10, 6))
plt.title('Task 2.II - South Lane Speed DDS')
plt.xlabel("Lanes")
plt.ylabel("Values")

plt.bar(x - width, q1s, width, label='Q1', color='lightblue')
plt.bar(x, q2s, width, label='Q2 (Median)', color='orange')
plt.bar(x + width, q3s, width, label='Q3', color='lightgreen')
plt.bar(x + 2*width, qiqrs, width, label='IQR', color='black')
plt.bar(x + 3*width, ranges, width, label='Range', color='wheat')
plt.xticks(x + width, ['Lane 4', 'Lane 5', 'Lane 6'])
plt.ylim(0,120)
plt.yticks(y_ticks)
plt.legend()
plt.show()

