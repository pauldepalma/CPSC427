from kNN import *

def classify_person(norm_data_matrix, range_vals, min_vals, labels_vector,k):
    labels = ['in large doses', 'in small doses', 'not at all']
    raw_labels = ['largeDoses', 'smallDoses', 'didntLike']
    percent_video = float(raw_input("percentage of time spent playing video games " +
                                    "over the past year?\n"))
    freq_flier_miles = float(raw_input("Number of frequent flyer miles earned in " +
                                       "the past year?\n"))
    liters_ice_cream = float(raw_input("Number of liters of ice cream eaten in " +
                                       "the past year?\n"))

    in_pt = array([freq_flier_miles, percent_video, liters_ice_cream])
    in_pt_norm = normalize_point(in_pt, min_vals, range_vals)
    
    result = classify(in_pt_norm, norm_data_matrix, labels_vector, k)
    potential = 'out of range'
    for i in range(k):
        if result == raw_labels[i]:
            potential = labels[i]
            break
                  
    print ("You will probably like this person: " + potential)

def main():
    k = 3
    data_matrix, labels_vector = file2matrix("datingTestSet.txt")
    #plot_data(data_matrix)
    norm_data_matrix, range_vals, min_vals = normalize(data_matrix)
    #test_classifier(norm_data_matrix, labels_vector,k)
    classify_person(norm_data_matrix, range_vals, min_vals, labels_vector, k)
    
    
    
    
main()
