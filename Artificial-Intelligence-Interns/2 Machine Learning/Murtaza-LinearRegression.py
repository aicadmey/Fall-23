from sklearn.linear_model import LinearRegression

# DataSet of height and weight
heights = [[160], [165], [170], [175], [180]]
weights = [55, 60, 65, 70, 75]

# Create a linear regression model
model = LinearRegression()

# Train the model on the data
model.fit(heights, weights)

# This will Predict the weight for a given height
user_height = float(input("Enter your height in centimeters: "))
predicted_weight = model.predict([[user_height]])

print("Predicted weight:", predicted_weight[0])