# final_project.py

import pandas as pd

# This program demonstrates a complete data analysis workflow

# Load a dataset (replace 'data.csv' with your actual dataset file)
df = pd.read_csv('data.csv')

# Display the first few rows of the dataset
print("Dataset Head:\n", df.head())

# Perform basic data analysis
print("\nDataset Summary:\n", df.describe())

# Clean data if needed
df = df.dropna()  # Drop missing values
print("\nCleaned Dataset Summary:\n", df.describe())

# Example analysis: Count occurrences of a categorical variable
category_counts = df['Category'].value_counts()  # Replace 'Category' with your column name
print("\nCategory Counts:\n", category_counts)

