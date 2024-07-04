from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Load the California housing dataset
california_housing = fetch_california_housing()
X = california_housing.data
y = california_housing.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a KNN regressor with k=5
knn_regressor = KNeighborsRegressor(n_neighbors=5)

# Train the regressor on the training data
knn_regressor.fit(X_train, y_train)

# Make predictions on the test data
predictions = knn_regressor.predict(X_test)

# Calculate evaluation metrics: Mean Squared Error and R-squared
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Mean Squared Error:", mse)
print("R-squared:", r2)

# Example: Predict the house price for a new set of features
new_house_features = np.array([[0.1, 1772, 6, 3000, 2, 1, 4, 40]])  
predicted_price = knn_regressor.predict(new_house_features)
print("Predicted House Price:", predicted_price[0])
