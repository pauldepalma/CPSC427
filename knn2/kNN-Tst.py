import kNN
from numpy import *

def create_data_set():
    group = array([[3,104],[2,100],[1,81],[101,10],[99,5],[98,2]])
    labels = ['r','r','r','a','a','a']
    
    return group, labels


    
def main():

    unKnown = [18,90]
    k = 3
    group, labels = create_data_set()
    bucket = kNN.classify(unKnown, group, labels, k)
    print bucket


              

main()
