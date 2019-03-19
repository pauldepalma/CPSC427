import numpy as np

def main():
    
   

    X = np.array([[1,2,3]])
    print X.shape

    Y = np.array([ [1],
                   [2],
                   [3]])
    print Y.shape


    Z = np.matmul(X,Y)
    print Z


    
main()
