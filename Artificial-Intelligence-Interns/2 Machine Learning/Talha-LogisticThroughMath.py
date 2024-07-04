import numpy as np
HourStudy = np.array([29, 15, 33, 28, 39])
PassOrFail = np.array([0, 0, 1, 1, 1])
# Add a bias term (intercept) to the features
X = np.c_[np.ones_like(HourStudy), HourStudy]
# Initialize coefficients (weights) to zero
coefficients = np.zeros(X.shape[1])

# Define the logistic function (sigmoid function)
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
# Define the gradient descent function to update coefficients
def gradient_descent(X, y, coefficients, learning_rate, iterations):
    for _ in range(iterations):
        predictions = sigmoid(np.dot(X, coefficients))
        error = predictions - y
        gradient = np.dot(X.T, error) / len(y)
        coefficients -= learning_rate * gradient
    return coefficients

# Perform gradient descent to find the optimal coefficients
learning_rate = 0.01
iterations = 10000
coefficients = gradient_descent(X, PassOrFail, coefficients, learning_rate, iterations)
hours_studied = 33
new_data = np.array([1, hours_studied])

# Calculate the probability of passing using the trained coefficients
probability_pass = sigmoid(np.dot(new_data, coefficients))

print("Probability of passing for a student who studied 33 hours:", probability_pass)
