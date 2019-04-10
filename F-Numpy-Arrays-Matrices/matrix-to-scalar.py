import numpy as np
import matplotlib.pyplot as plt

#technique to extract scalars from a matrix or array object

'''
Data is sequence of rows, where each row is sequence of tab-separated,
floating point features.  There are m rows and n features.  In this case,
m = 100 and n = 2
'''
def loadData(file_name):
    with open(file_name) as fin:
        #remove white space and split on the tabs such that
        #each line is a list of features stored in a python
        #object that may be iterated over
        rows = (line.strip().split('\t') for line in fin)
        
        #each row is a list. map is a python command that takes a function
        #as its first argument and the input to the function as the second.
        #The task here is to transfrom each list of n strings into a list of
        #n floating point objects.
        dataIn = [map(float,row) for row in rows]

    #transform a list of lists to a numpy matrix.  Numpy matrices are 2D, unlike
    #numpy arrays which may be ndimensional.  Matrix objects inherit from
    #ndarrays but have their own notation for matrix manipulations (p * q for
    #matrix multiplication).  The 2D limit may be tricked, as in this case,
    #where the column is itself an object containing multiple floating
    #point values

    dataMat = np.mat(dataIn) 
    
    #same technique works for array objects 
    #dataMat = np.array(dataIn) 
    return dataMat

def plot_data(dataMat):
    #The problem here is that dataMat is a matrix, each row of which
    #is a list of two floating point numbers. matplolib's 2D scatterplot
    #requires a python list values for the x and y axes. 


    #Split the matrix into two numpy matrices, the first with the 0th col of
    #each row, the second with the 1st column of each row
    xMatrix = dataMat[:,0]
    yMatrix = dataMat[:,1]

    #xMatrix, as a numpy matrix, has two dimensions, the 0th being the
    #number of rows.    
    m = np.shape(xMatrix)[0]

    #extract the scalars from the matrices using the matrix object'sitem command
    xm = [xMatrix.item(i) for i in range(m)]
    ym = [yMatrix.item(i) for i in range(m)]

    plt.scatter(xm,ym,marker='D',color='m')
    plt.show()
 

def main():
    dataMat = loadData("testSet1.txt")

    plot_data(dataMat)
    
main()

