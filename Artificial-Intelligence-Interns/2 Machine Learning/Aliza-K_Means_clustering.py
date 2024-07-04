import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

# Create sample data (two distinct clusters)
data = np.random.rand(100, 2)
data[50:] += [2, 2]  # Shift the second cluster

# Fit K-Means clustering model
kmeans = KMeans(n_clusters=2)
kmeans.fit(data)

# Get cluster centers and labels
centers = kmeans.cluster_centers_
labels = kmeans.labels_

# Plot the original data points
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='rainbow')
plt.scatter(centers[:, 0], centers[:, 1], c='black', marker='X', s=200, label='Cluster Centers')
plt.title('K-Means Clustering')
plt.legend()
plt.show()
