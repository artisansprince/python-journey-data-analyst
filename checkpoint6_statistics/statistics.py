# statistics.py

import numpy as np

# This program demonstrates basic statistics calculations

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calculate mean, median, and standard deviation
mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)

print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)

