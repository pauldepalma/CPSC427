from numpy import *
from kNN import *
import matplotlib
import matplotlib.pyplot as plt
    
    
def main():
    data_matrix, labels_vector = file2matrix("datingTestSet.txt")
    fig = plt.figure()
    tr_fig = fig.add_subplot(1,1,1) #translate the axes up and to the right
    #x = video games, y = ice cream
    #tr_fig.scatter(data_matrix[:,1], data_matrix[:,2])
    #x = frequent flyer miles, y = video games
    tr_fig.scatter(data_matrix[:,0], data_matrix[:,1])
    plt.show()

main()
