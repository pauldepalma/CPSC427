from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt

'''
in_pt is a tuple, (2,3), for example.  Calculate the distance from all points
in the data to in_pt
group is the matrix created in the calling program
labels is the label vector from the calling program
k is the nearest neighbor parameter
returns the label with the greates number of votes
'''
def classify(in_pt, group, labels, k):

    #column vector with ith entry containing euclidean distance from
    #ith point in group to in_point
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

    #class_count is a collection of label:vote pairs, where 'vote' is the
    #number of votes gotten by the label.  sorted_vote_count is list of label,
    #vote tuples, sorted by votes in reverse numerical order.
    #So, the 0th item in the list is the tuple containing the label
    #with the most votes, the 1st item is the tuple containing the
    #second highest vote count and so forth
    sorted_vote_count = sorted(class_count.iteritems(), 
            key=operator.itemgetter(1),
            reverse = True)
    #0th item in 0th tuple, i.e, the label with the most votes
    return sorted_vote_count[0][0]
        
'''
Calculate the euclidean distance from in_pt to every point in the group matrix
Returns a column vector of distances to in_pt, in the same order as the
points themselves appear in group
'''
def calc_distances(in_pt,group):
    #get number of rows in group
    data_set_size = group.shape[0]

    #create a matrix, m
    #(datasetSize,1) says make each row of m 1 repetition of in_pt
    m = tile(in_pt, (data_set_size,1))

    #The next 4 lines compute Euclidean distance

    #element-wise subtraction
    diff_mat = m - group

    #element-wise square
    sq_diff_mat = diff_mat**2

    #row-wise sum. columnwise sum would require axis = 0
    #produces a column vector
    sq_dist = sq_diff_mat.sum(axis = 1)

    #column-wise square root
    #produces column-vector of Euclidean distances the unclassified point to
    #each existin point
    distances = sq_dist**.5

    return distances

'''
file_name contains three columns of data plus a label column
'''
def file2matrix(file_name):
    #read file, initialize data matrix and label vector
    fin = open(file_name)
    line_lst = fin.readlines() #list of lines from file_name
    data_matrix = zeros((len(line_lst),3)) #num_lines X 3 matrix filled with zeros
    labels_vector = []

    #populate data matrix and label vector
    idx = 0
    for line in line_lst:
        line = line.strip()
        lst = line.split('\t') #list of columns forming a line
        #copy the first three columns of the line to row idx of data matrix
        data_matrix[idx,:] = lst[0:3]
        #copy last column of the line to label vector
        labels_vector.append((lst[-1]))
        idx += 1
    return data_matrix, labels_vector

def plot_data(data_matrix):
    fig = plt.figure()
    tr_fig = fig.add_subplot(1,1,1) #translate the axes up and to the right
    #x = video games, y = ice cream
    #tr_fig.scatter(data_matrix[:,1], data_matrix[:,2])
    #x = frequent flyer miles, y = video games
    tr_fig.scatter(data_matrix[:,0], data_matrix[:,1])
    plt.show()
    
'''
Normalizes data matrix using a conventional normalization technique extended to matrices
     norm = (orig_value - min_value) / range
         where range is max - min
         extended to matrices by using matrix element-wise subtraction followed
         by matrix element-wise division
'''
def normalize(data_matrix):
    #vectors composed of min and max of each column of data_matrix
    min_vals = data_matrix.min(axis=0) 
    max_vals = data_matrix.max(axis=0)

    range_vals = max_vals - min_vals
    
    #number of rows in data_matrix
    num_rows = data_matrix.shape[0] 

    #matrix where each row is ranges 
    ranges_data_matrix = tile(range_vals, (num_rows,1)) #matrix where each row is range_vals
    min_data_matrix = tile(min_vals, (num_rows,1)) #matrix where each row is min_vals
    
    #compute the normalized matrix according to normalization technique
    # norm = (orig_value - min_value) / range
    # where range is max - min
    #element-wise subtraction, followed by element-wise division
    norm_data_matrix = (data_matrix - min_data_matrix)/ ranges_data_matrix
    return norm_data_matrix, range_vals, min_vals

'''
Normalizes a single point using the technique described in normalize, but restricted to a vector
'''
def normalize_point(in_pt, min_vals, range_vals):
    return (in_pt - min_vals) / range_vals

'''
Test classifier by:
1. Holding out 10% of data
2. Training classifier on 90% of data
3. Testing classifer on held out data
'''
def test_classifier(norm_data_matrix, labels_vector):
    hold_out_ratio = 0.10
    num_rows = norm_data_matrix.shape[0]
    num_tst_points = int(num_rows * hold_out_ratio)
    error_ct = 0

    '''
    for each iteration over the test points, send to the classifier:
    1. test point: the ith point in norm_data_matrix drawn from the top hold_out_ratio % of the data
    2. training data: points drawn from the bottom hold_out_ration % of the data
    3. an integer, k, which the classifier uses to choose the k nearest neighbors
    '''
    for i in range(num_tst_points):
        result = classify(norm_data_matrix[i,:],
                      norm_data_matrix[num_tst_points:num_rows,:],
                      labels_vector[num_tst_points:num_rows],3)
    
        if (result != labels_vector[i]):
            error_ct += 1.0
            out1 = "Error on item " + str(i)
            out2 = "  classifier says: " + str(result) + " real answer: " + str(labels_vector[i])
            print out1
            print out2
            print
            
    print("Error Rate: %f" % (error_ct/float(num_tst_points) * 100)) + " percent"

'''
Uses user-input parameters to classify a dating candidate
'''
def classify_person(norm_data_matrix, range_vals, min_vals, labels_vector):
    labels = ['in large doses', 'in small doses', 'not at all']
    raw_labels = ['largeDoses', 'smallDoses', 'didntLike']
    k = 3
    percent_video = float(raw_input("percentage of time spent playing video games " +
                                    "over the past year?\n"))
    freq_flier_miles = float(raw_input("Number of frequent flyer miles earned in " +
                                       "the past year?\n"))
    liters_ice_cream = float(raw_input("Number of liters of ice cream eaten in " +
                                       "the past year?\n"))

    in_pt = array([freq_flier_miles, percent_video, liters_ice_cream])
    in_pt_norm = normalize_point(in_pt, min_vals, range_vals)
    
    result = classify(in_pt_norm, norm_data_matrix, labels_vector, k)
    for i in range(3):
        if result == raw_labels[i]:
            potential = labels[i]
            break
                  
    print ("You will probably like this person: " + potential)
    
        
              
            
    
    
    
    
                             
    
    


    
