from math import sqrt
from operator import itemgetter

# TESTSET
def testSet(city):
    testSet = []
    berkas = open('test.csv','r')
    data=eval(berkas.read())
    for i in range(len(data)-1):
        if data[i]['name']==city.capitalize():
            testSet.append(data[i])
    berkas.close()
    return testSet

#TRAININGSET
def trainingSet():
    trainingSet = []
    berkas = open('test.csv','r')
    data=eval(berkas.read())
    for i in range(len(data)):
        trainingSet.append([data[i]])
    berkas.close()
    return trainingSet

#print(trainingSet())) #OUTPUT TYPE : LIST, len : 20
#print(testSet('bekasi')) #OUTPUT TYPE : LIST

# -- THE FUNCTIONS TO GET EUCLIDEAN DISTANCE &  CITY WITH NEARLY SAME CONDITION --

def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x]['coord']['lon'] - instance2[x]['coord']['lon']), 2)
        distance += pow((instance1[x]['coord']['lat'] - instance2[x]['coord']['lat']), 2)
    return sqrt(distance)

def getNeighbors(testInstance, k, trainingSet=trainingSet()):
	distances = []
	length = 1
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		if trainingSet[x]!=testInstance:
		    distances.append((trainingSet[x], dist))
	distances.sort(key=itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors

print(getNeighbors(testSet('kebumen'),3))