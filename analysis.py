import pandas as pd
import matplotlib.pyplot as plt
# Load Excel data
data = pd.read_excel("intern_performance.xlsx")
# Show first 5 rows
print("First 5 rows of the data set:")
print(data.head())
# Show basic information
print(" \nDataset information:")
data.info()
print("\nAverage Performance score:")
print(data["Performance"].mean())
print("\nBest performance intern:")
print(data.loc[data["Performance"].idxmax()])
print("\nWorst performing intern:")
print(data.loc[data["Performance"].idxmin()])
import matplotlib.pyplot as pyplot
# Scatter plot: Attendance vs Performance
plt.scatter(data["Attendance_Percentage"], data["Performance"])
plt.xlabel("Attendance Percentage")
plt.ylabel("Performance")
plt.title("Attendance vs Performance")
plt.show(block=True)
input("Press Enter to close the graph...")
