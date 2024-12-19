import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

#imports the data
data = pd.read_csv("part5-unsupervised-learning/customer_data.csv")
x = data[["Annual Income", "Spending Score"]]

#standardize the data
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

#the value of k has been defined for you
k = 5

#apply the kmeans algorithm
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(x_scaled)

#get the centroid and label values
centroids = kmeans.cluster_centers_
labels = kmeans.labels_

#sets the size of the graph
plt.figure(figsize=(5,4))

#use a for loop to plot the data points in each cluster
for cluster in range(k):
    cluster_data = x_scaled[labels == cluster]
    plt.scatter(cluster_data[:, 0], cluster_data[:, 1], label=f"Cluster {cluster + 1}")

#plot the centroids
plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', s=100, c='r', label='Centroids')

            
#shows the graph
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.legend()
plt.show()