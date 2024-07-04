from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a random forest classifier with 100 trees
rf_classifier = RandomForestClassifier(n_estimators=10, random_state=42)

# Train the classifier on the training data
rf_classifier.fit(X_train, y_train)

# Make predictions on the test data
predictions = rf_classifier.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)

# Display classification report
print("Classification Report:")
print(classification_report(y_test, predictions))

# Example: Predict the species for a new iris flower
new_flower_features = [[5.1, 3.5, 1.4, 0.2]]  # Example features of a new iris flower
predicted_species = rf_classifier.predict(new_flower_features)
print("Predicted Species:", iris.target_names[predicted_species][0])
