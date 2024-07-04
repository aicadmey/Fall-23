# Import the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# First element of array is on x-axix and 2nd elemeny on y-axix
data = np.array([[1, 4], [3, 2], [1, 2], [1,3], [3,3], [3,4], [2,2], [2,4], [7, 8], [8, 9], [9, 8], [9, 7],[8,6]])

# Here data fit and decide how much we want cluster
kmeans = KMeans(n_clusters=2)
kmeans.fit(data)

# Step 3: Get cluster labels
labels = kmeans.labels_

# Step 4: Plot the data points with different colors for each cluster
plt.scatter(data[:, 0], data[:, 1], c=labels)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', marker='x', s=100)
plt.title("K-Means Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()