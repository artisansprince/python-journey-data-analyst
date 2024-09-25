# pandas_intro.py

import pandas as pd

# This program demonstrates basic operations using Pandas

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [30, 25, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)

# Basic DataFrame operations
print("\nMean Age:", df['Age'].mean())
print("\nDataFrame Summary:\n", df.describe())

