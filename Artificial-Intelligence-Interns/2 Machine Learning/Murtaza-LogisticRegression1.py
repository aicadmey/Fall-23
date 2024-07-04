# Import the necessary libraries
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Step 1: Create some sample data
X = np.array([[1.2, 1.3], [1.4, 1.5], [1.8, 1.9], [3.4, 3.3], [3.5, 3.5], [3.2, 3.8]])
y = np.array([0, 0, 0, 1, 1, 1])

# Step 2: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Create a logistic regression model
model = LogisticRegression()

# Step 4: Fit the model to the training data
model.fit(X_train, y_train)

# Step 5: Make predictions on the test data
y_pred = model.predict(X_test)

# Step 6: Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

# Step 7: Display the results
print("Model Coefficients:", model.coef_)
print("Model Intercept:", model.intercept_)
print("Accuracy:", accuracy)
print(y_pred)


