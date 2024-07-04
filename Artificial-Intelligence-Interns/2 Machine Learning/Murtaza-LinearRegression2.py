from sklearn.linear_model import LinearRegression

# DataSet of height and weight
heights = [160, 165, 170, 175, 180]
weights = [[55], [60], [65], [70], [75]]

# Create a linear regression model
model = LinearRegression()

# Train the model on the data
model.fit(weights,heights)

# This will Predict the height for a given weight
user_weight = int(input("Enter your weight: "))
predicted_height = model.predict([[user_weight]])

print("Predicted height:", predicted_height[0])