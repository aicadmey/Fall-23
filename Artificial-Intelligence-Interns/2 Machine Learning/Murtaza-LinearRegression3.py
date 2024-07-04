from sklearn.tree import DecisionTreeClassifier

# Sample data (weight in grams, 1 for red, 0 for orange)
X = [[150, 1], [130, 1], [180, 0], [160, 0], [120, 1]]
y = ["apple", "apple", "orange", "orange", "apple"]

# Create a decision tree classifier
classifier = DecisionTreeClassifier()

# Train the classifier on the data
classifier.fit(X, y)

# Input new data (weight and color)
user_weight = int(input("Enter the weight of the fruit in grams: "))
user_color = int(input("Enter the color (1 for red, 0 for orange): "))

# Make a prediction
predicted_fruit = classifier.predict([[user_weight, user_color]])

print("Predicted fruit:", predicted_fruit[0])