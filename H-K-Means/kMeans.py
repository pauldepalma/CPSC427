#First Draft
#Mostly from Peter Harrington, Machine Learning in Action

import numpy as np

'''
Data comes in like this:
0.xxx ...  0.yyyy
where the values are floating point numbers representing points in a space
my example is m x 2, but the code would work for n features
Read these into an m x 2 numpy matrix, where m is the number of points
'''
def loadData(file_name):
    with open(file_name) as fin:
        rows = (line.strip().split('\t') for line in fin)
        dataMat = [map(float,row) for row in rows]
    return np.mat(dataMat)

'''
Construct a k x n matrix of randomly generated points as the
initial centroids. The points have to be in the range of the points
in the data set
'''
def randCent(dataMat,k):
    numCol = np.shape(dataMat)[1]  #notice the number of cols is not fixed.
    centroids = np.mat(np.zeros((k,numCol))) #kxnumCol matrix of zeros
    for col in range(numCol):
        minCol = np.min(dataMat[:,col]) #minimum from each column
        maxCol = np.max(dataMat[:,col]) #maximum from each column
        rangeCol = float(maxCol - minCol)
        centroids[:,col] = minCol + rangeCol * np.random.rand(k,1)
    return centroids

'''
Compute the Euclidean distance between two points
Each point is vector, composed of n values, idicating a point in n space 
'''
def distEucl(vecA,vecB):
    return np.sqrt(np.sum(np.power(vecA - vecB,2)))

    

def kMeans(dataMat, k, distMeas=distEucl, createCent=randCent):
    m = np.shape(dataMat)[0]  #how many items in data set
    
    #create an mX2 natrix filled with zeros
    #each row stores centroi information for a point
    #col 0 stores the centroid index to which the point belongs
    #col 1 stores the distance from the point to the centroid
    clusterAssment = np.mat(np.zeros((m,2)))

    #create k randomly placed centroids
    centroids = createCent(dataMat,k)  

    #compute centroids
    #your code goes here
        
    
            
    return centroids       

def main():
    k = 4
    dataMat = loadData("testSet.txt")

    centroids = kMeans(dataMat, k, distEucl, randCent)

    print centroids
   
  
    #test code for auxiliary functions 
    print "point 0"
    print dataMat[0]
    print "point 1"
    print dataMat[1]
    print
    print "centroids"
    print randCent(dataMat,k)
    print
    print "distance from point 0 to point 1"
    print distEucl(dataMat[0], dataMat[1])

    
main()

