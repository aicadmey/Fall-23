from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load a sample dataset (Iris dataset)
data = datasets.load_iris()
X = data.data
y = data.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Decision Tree Classifier
clf = DecisionTreeClassifier()

# Train the model on the training data
clf.fit(X_train, y_train)

# Make predictions on the test data
y_pred = clf.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Display classification report
print(classification_report(y_test, y_pred))
import matplotlib.pyplot as plt
import numpy as np

# Generate sample data (replace this with your data)
data = np.random.randn(1000)

# Create a histogram
plt.hist(data, bins=20, color='skyblue', edgecolor='black')

# Customize the histogram
plt.title('Histogram Example')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Display the histogram
plt.show()
