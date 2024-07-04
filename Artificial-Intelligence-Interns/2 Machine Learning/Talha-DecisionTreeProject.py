import numpy as np  
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes  
from sklearn.model_selection import train_test_split  
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Loading the sklearn diabetes dataset  
X, Y = load_diabetes(return_X_y=True)  

# Selecting a single feature for binary classification
X = X[:, 8].reshape(-1, 1)

# Converting problem into binary classification
Y = (Y > 150).astype(int) 

# Splitting the dataset into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=10)

# Creating an instance for the decision tree classifier of sklearn  
dt_classifier = DecisionTreeClassifier(random_state=42)

# Training the decision tree classifier
dt_classifier.fit(X_train, Y_train)

# Making predictions on the test set
Y_pred = dt_classifier.predict(X_test)


accuracy = accuracy_score(Y_test, Y_pred)
conf_matrix = confusion_matrix(Y_test, Y_pred)

print(f"Accuracy: {accuracy}")
print("Confusion Matrix:")
print(conf_matrix)

plt.scatter(X_test, Y_test, color="black", label="original data")
plt.scatter(X_test, Y_pred, color="red", label="predicted data")
plt.xlabel("Independent Feature")
plt.ylabel("Diabetes (1) / No Diabetes (0)")
plt.title("Decision Tree Classifier")
plt.legend()
plt.show()
