import numpy as np  
import matplotlib.pyplot as plt
from sklearn import linear_model  
from sklearn.datasets import load_diabetes  
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split  
from sklearn.metrics import accuracy_score, confusion_matrix

# Loading the sklearn diabetes dataset  
X, Y = load_diabetes(return_X_y=True)  

# Selecting a single feature for binary classification
X = X[:, 8].reshape(-1, 1)

# Converting the problem into binary classification
Y = (Y > 150).astype(int)  # 1 if patient has diabetes (target > 150), 0 otherwise

# Splitting the dataset into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=10)

# Creating an instance for the logistic regression model of sklearn  
logreg = LogisticRegression()

# Training the logistic regression model  
logreg.fit(X_train, Y_train)

# Making predictions on the test set
Y_pred = logreg.predict(X_test)

# Calculating accuracy and confusion matrix
accuracy = accuracy_score(Y_test, Y_pred)
conf_matrix = confusion_matrix(Y_test, Y_pred)

# Printing the accuracy and confusion matrix
print(f"Accuracy: {accuracy}")
print("Confusion Matrix:")
print(conf_matrix)

# Plotting the output
plt.scatter(X_test, Y_test, color="black", label="original data")
plt.scatter(X_test, Y_pred, color="red", label="predicted data")
plt.xlabel("Independent Feature")
plt.ylabel("Diabetes (1) / No Diabetes (0)")
plt.title("Logistic Regression")
plt.legend()
plt.show()
