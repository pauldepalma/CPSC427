from numpy import *
import operator


#inPt is an array: [0,0] for example.  It is the point, the distance to we want
#to calculate
#group is the matrix from createDataSet
#labels is the label vector above
#k is the nearest neighbor parameter
def classify0(inPt, group, labels, k):
    distances = calcDistances(inPt,group)

    #produce a list of indices to items in the distances vector.  index 0
    #refers to the smallest item in distances, index 1 to the next smallest,
    #and so forth. 
    distancesIdx = distances.argsort()

    #determine how many times each label appears in the top k entries
    voteCount = {}
    for i in range(k):
        labelI = labels[distancesIdx[i]]
        if labelI in voteCount:
            voteCount[labelI] = voteCount[labelI] + 1
        else:
            voteCount[labelI] = 1

    #turn the dictionary into a list of tuples, sorting the tuples by the
    #second item, i.e., the number of votes the label (the first item) got
    #itemgetter gets the second (1) item in the dictionary.
    #The idea here is that we're sorting the dictionary by the second item,
    #the number of votes.
    sortedVoteCount = sorted(voteCount.iteritems(), key=operator.itemgetter(1),
                             reverse = True)
    #the first entry in sortedVoteCount is the label with the most votes
    return sortedVoteCount[0][0] #0th item in 0th tuple
        

   
'''calculate the distance for each point in the original group to the new
   point by Euclidean distance'''
def calcDistances(inPt,group):
    #get number of rows in group
    dataSetSize = group.shape[0]
    
    #create a matrix, each row of which is inPt
    #ultimately what we'll do is find the distance from inPt to each
    #of the points represented as a row in group
    m = tile(inPt, (dataSetSize,1))

    #subtract each row in group from each row in m
    diffMat = m - group
    

    #square each entry in diffMat
    sqDiffMat = diffMat**2

    #Sum the squares of the x,y coordinates row-wise, producing a vector, one
    #entry per row
    #each entry, i, is the distance from the point represented by the ith
    #row in group
    sqDist = sqDiffMat.sum(axis = 1)

    #find the hypotenuse. each entry represents the distance from the
    #corresponding row in the original group to the new input
    #This is the Euclidean distance
    distances = sqDist**.5

    return distances
    
