from numpy import *
import operator

'''
in_pt is an array: [0,0] for example.  Calculate the distance from all points
in the data to in_pt
group is the matrix created in the calling program
labels is the label vector from the calling program
k is the nearest neighbor parameter
returns the label with the greates number of votes
'''
def classify(in_pt, group, labels, k):

    #vector with ith entry containing euclidean distance from ith point in group
    #to in_point
    distances = calc_distances(in_pt,group)

    #produce a list of indices to items in the distances vector.  index at
    #position 0 is the index to the smallest item in distances, index 1 to
    #the next smallest, and so forth
    distances_idx = distances.argsort()

    #determine how many times each label appears in the smallest k entries
    class_count = {}
    for i in range(k):
        #extract index associated with ith entry in distances_idx
        #use it to find the associated label
        vote_label = labels[distances_idx[i]]
        #add 1 to the label entry if > 0.  if it does not exist add 1 to 0
        class_count[vote_label] = class_count.get(vote_label,0) + 1

    #class_count is a collection of label:vote pairs, where 'vote' is the number
    #of votes gotten by the label.  sorted_vote_count is list of label,vote tuples, sorted by
    #votes in reverse numerical order.  So, the 0th item in the list is the tuple containing the label
    #with the most votes, the 1st item is the tuple containing the second highest vote count
    #and so forth
    sorted_vote_count = sorted(class_count.iteritems(), key=operator.itemgetter(1),
                             reverse = True)
    return sorted_vote_count[0][0] #0th item in 0th tuple, i.e, the label with the most votes
        
'''
Calculate the euclidean distance from in_pt to every point in the group matrix
Returns a vector of distances to in_pt, in the same order as the points themselves
appear in group
'''
def calc_distances(inPt,group):
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
    
