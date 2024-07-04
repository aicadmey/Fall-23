import numpy as np

# Given data for hospital injections over the last 5 years
years = np.array([1, 2, 3, 4, 5])  # Years
injections = np.array([100, 150, 200, 250, 300])  # Number of injections for each year

# Calculate the required sums
n = len(years)
sum_years = np.sum(years)
sum_injections = np.sum(injections)
sum_years_injections = np.sum(years * injections)
sum_years_squared = np.sum(years**2)

# Calculate the coefficients a0 and a1 for the linear regression model
a1 = (sum_years_injections - (1/n) * sum_years * sum_injections) / (sum_years_squared - (1/n) * sum_years**2)
a0 = (1/n) * sum_injections - a1 * (1/n) * sum_years

# Print the coefficients
print("a0 (intercept):", a0)
print("a1 (slope):", a1)

# Make a prediction for the number of injections in the 6th year
year_6_prediction = a0 + a1 * 6
print("Prediction for the 6th year's injections:", year_6_prediction)
