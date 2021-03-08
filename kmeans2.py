import os
import sys
import random
import numpy as np

datapoints = np.loadtxt("input.txt")

k = sys.argv[1]

beginCentroids = random.sample(range(0,len(datapoints)), int(k))

centroids = []
for b in beginCentroids:
	centroids.append(datapoints[b])

centroids = np.array(centroids)

# find the distance between 2 data points
def distBetweenPoints(x1, x2):
	return (sum((x1 - x2)**2))**0.5

# put closest centroid to data points
def clusterAroundCentroid(cen, x):
	specCentroid = []
	for i in x:
		distance = []
		for j in cen:
			distance.append(distBetweenPoints(i, j))
		specCentroid.append(np.argmin(distance))
	return specCentroid

centroidIndexes = clusterAroundCentroid(centroids, datapoints)

def kmeans(clusters, x):
	newCentroids = []
	newDataFrame = pd.concat([pd.DataFrame(x),pd.DataFrame(clusters,columns=['cluster'])], axis = 1)
	for c in set(newDataFrame['cluster']):
		currentC = newDataFrame[newDataFrame['cluster'] == c][newDataFrame.columns[:-1]]
		meanC = currentC.mean(axis=0)
		newCentroids.append(meanC)
	return newCentroids

print("***point, label***")
for i in range(len(datapoints)):
	newarray = np.array([datapoints[i],centroidIndexes[i]])
	print(*newarray)
