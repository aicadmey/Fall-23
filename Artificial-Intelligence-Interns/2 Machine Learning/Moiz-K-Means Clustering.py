import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

n_samples = 300
n_features = 2
n_clusters = 3
X, _ = make_blobs(n_samples=n_samples, n_features=n_features, centers=n_clusters, random_state=42)
plt.scatter(X[:, 0], X[:, 1], s=20)
plt.title("Generated Data for K-means Clustering")
plt.show()

kmeans = KMeans(n_clusters=n_clusters)
kmeans.fit(X)
cluster_centers = kmeans.cluster_centers_
labels = kmeans.labels_

plt.scatter(X[:, 0], X[:, 1], c=labels, s=20, cmap='viridis')
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], c='red', s=200, marker='X', label='Cluster Centers')
plt.title("K-means Clustering")
plt.legend()
plt.show()