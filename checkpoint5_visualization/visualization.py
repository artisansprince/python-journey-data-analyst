# visualization.py

import matplotlib.pyplot as plt
import seaborn as sns

# This program demonstrates basic data visualization using Matplotlib and Seaborn

# Sample data
data = [1, 3, 2, 5, 4]

# Create a simple line plot
plt.plot(data)
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# Create a seaborn bar plot
sns.barplot(x=["A", "B", "C", "D"], y=[4, 2, 5, 3])
plt.title("Bar Plot using Seaborn")
plt.show()

