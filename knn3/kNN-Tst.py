from kNN import *

def main():
    data_matrix, labels_vector = file2matrix("datingTestSet.txt")
    #plot_data(data_matrix)
    norm_data_matrix, range_vals, min_vals = normalize(data_matrix)
    #test_classifier(norm_data_matrix, labels_vector)
    classify_person(norm_data_matrix, range_vals, min_vals, labels_vector)
    
    
    
    
main()
