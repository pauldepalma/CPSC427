from kNN import *

def main():
    data_matrix, labels_vector = file2matrix("dating_test_set.txt")
    #plot_data(data_matrix)
    normalize(data_matrix)
    
main()
