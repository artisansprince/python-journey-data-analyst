# statistical_analysis.py

import numpy as np
import pandas as pd
import statsmodels.api as sm

# This program demonstrates a simple linear regression analysis

# Sample data
data = {
    'X': [1, 2, 3, 4, 5],
    'Y': [2, 3, 5, 7, 11]
}

df = pd.DataFrame(data)

# Perform linear regression
X = df['X']
Y = df['Y']
X = sm.add_constant(X)  # Adds a constant term to the predictor
model = sm.OLS(Y, X).fit()

# Print the summary of the regression
print(model.summary())

