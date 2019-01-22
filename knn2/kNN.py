from numpy import *
import operator


#in_pt is a numpy array. It reps. the point whose classification is unknown
#group is the matrix of points whose classification is knownlabels is the label vector, i.e., the classes
#k is the nearest neighbor parameter
def classify(in_pt, group, labels, k):
    distances = calcDistances(in_pt,group)

    #produce a vector containing the rank of each item in the distances
    #array from smallest to largest.
    #suppose distances = [3,2,7]
    #distances.argsort() produces [1,0,2]
    distances_idx = distances.argsort()

    #count votes
    class_count = {}
    for i in range(k):
        #label associated with the ith entry in distancesIdx
        vote_label = labels[distances_idx[i]]
        #add 1 to entry if entry exists, else insert entry and add 1 to 0
        class_count[vote_label] = class_count.get(vote_label,0) + 1

    #produce a list of tuples (class,votes), sorted on votes
    #class_count.iteritems() produces a generator which iterates through the entries
    #in the dictionary.
    #key=operator.itemgetter(1) tells sort to sort on the 2nd item in the tuple
    #reverse=True: sort is from largest to smallest
    sorted_class_count = sorted(class_count.iteritems(), key=operator.itemgetter(1),
                             reverse = True)
    
    #the the 0th entry in the 0th tuple is the label with the most votes
    #example: [('r',17),('a',3)
    return sorted_class_count[0][0] #0th item in 0th tuple
        

   
#calculate Euclidean distance from each point in the data to the point
#whose classification is unknown
#in_pt is the point whose class is unknown
#group is a matrix or points whose class is known.  The x,y coords of each
#point form a row
def calcDistances(in_pt,group):
    #get number of rows in group
    #That is, the number of points represented by out data
    dataSetSize = group.shape[0]
    
    #Construct a matrix, where each row is inPt
    m = tile(in_pt, (dataSetSize,1))

    #subtract each row in group from each row in m
    diff_mat = m - group
    
    #square each entry in diffMat
    sq_diff_mat = diff_mat**2

    #Sum the squares of the x,y coordinates row-wise (axis = 1)
    #This produces a vector, one entry per row
    #each entry, i, is the square of the distance from a known point
    #to the unknown point
    sq_dist = sq_diff_mat.sum(axis = 1)

    #Take the square root of each entry in sqDist
    #This gives a vector of distances of each point to the unknown point
    distances = sq_dist**.5

    return distances
    
