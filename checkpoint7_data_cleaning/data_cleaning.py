# data_cleaning.py

import pandas as pd

# This program demonstrates basic data cleaning and preprocessing

# Create a sample DataFrame with missing values
data = {
    'Name': ['Alice', 'Bob', None, 'Charlie'],
    'Age': [30, None, 25, 35],
    'City': ['New York', 'Los Angeles', 'Chicago', None]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Drop rows with missing values
df_cleaned = df.dropna()
print("\nCleaned DataFrame:\n", df_cleaned)

