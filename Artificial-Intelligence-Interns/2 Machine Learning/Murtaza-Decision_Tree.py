from sklearn.tree import DecisionTreeClassifier

# Sample data (weight in grams, 1 for red, 0 for orange, 2 for yellow,3 for dark-red)
X = [[70, 1], [80, 1], [90,1], [50, 0], [60, 0], [40,0], [75,0], [110,1], [130,1], [150,3], [250,3], [200,3], [8,2], [30,2], [22,2], [17,2]]
y = ["apple", "apple", "apple", "orange", "orange", "orange", "orange", "apple", "apple", "pomogranate" , "pomogranate", "pomogranate", "Banana", "Banana", "Banana", "Banana"]

# Create a decision tree classifier
classifier = DecisionTreeClassifier()

# Train the classifier on the data
classifier.fit(X, y)

# Input new data (weight and color)
user_weight = int(input("Enter the weight of the fruit in grams: "))
user_color = int(input("Enter the color (1 for red, 0 for orange, 2 for yellow,3 for dark-red): "))

# Make a prediction
predicted_fruit = classifier.predict([[user_weight, user_color]])

print("Predicted fruit:", predicted_fruit[0])