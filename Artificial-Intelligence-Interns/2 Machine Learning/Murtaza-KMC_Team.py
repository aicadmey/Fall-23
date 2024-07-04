# Import the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# First element of array is on x-axix and 2nd elemeny on y-axix
data = np.array([[2, 5], [3, 68], [2, 10], [3, 131], [2, 50], [3, 49], [2, 18], [3, 46], [2, 74], [3, 8], [2, 50], [3, 31], [2, 9], [3, 26]])

# Here data fit and decide how much we want cluster
kmeans = KMeans(n_clusters=2)
kmeans.fit(data)

# Step 3: Get cluster labels
labels = kmeans.labels_

# Step 4: Plot the data points with different colors for each cluster
plt.scatter(data[:, 0], data[:, 1], c=labels)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', marker='x', s=100)
plt.title("Babar Azam, M Rizwan Average in cwc23 By K Means Clustering")
plt.xlabel("Pakistan Players")
plt.ylabel("Score")
plt.show()