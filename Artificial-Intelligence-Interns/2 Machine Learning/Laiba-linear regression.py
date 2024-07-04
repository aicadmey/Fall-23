from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Sample data
X = [[0.5, 0.7, 0.8, 0.9, 0.2],
     [0.6, 0.8, 0.7, 0.9, 0.3],
     [0.4, 0.6, 0.9, 0.7, 0.2]]
y = [10, 12, 8]  # Replace with your target values

# Data split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Make predictions
new_data = [[0.55, 0.75, 0.85, 0.95, 0.25]]
predictions = model.predict(new_data)
print("Predictions:", predictions)
