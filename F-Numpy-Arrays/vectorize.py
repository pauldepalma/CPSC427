import numpy as np

def main():

    print "Two Arguments for Vectorization"
    print
    
    print "Two Matrices"
    X = np.array([[12,7,3],
                 [4,5,6],
                 [7,8,9]])
    print X
    print X.shape
    print
    
    Y = np.array([[5,8,1,2],
                 [6,7,3,0],
                 [4,5,9,1]])
    print Y
    print Y.shape
    print

    print "vectorized matrix multiplication"
    Z = np.matmul(X,Y)
    print Z
    print


    print "iterative matrix multiplication"
    Z = np.zeros((3,4))

    #iterate over rows of X
    for rx in range(len(X)):
        #iterate over cols of Y
        for cy in range(len(Y[0])):
            #iterate over rows of Y
            for ry in range(len(Y)):
                Z[rx][cy] += X[rx][ry] * Y[ry][cy]
    print Z
    print

    print "another example"
    print
    print  "h_theta(X) = -40 _ 0.25 * x"
    print "X is a 4 X 1 vector"
   
    X = np.array([[2104], [1416], [1534], [852]])
    print X
    print
    
    print "insert a col of zeroes before existing col 0"
    X = np.insert(X,0,values=1,axis=1)
    print X
    print
 
    print "Theta is a 2 x 1 vector, theta0 followed by theta1"
    Theta = np.array([[-40],[0.25]])
    print Theta
    print

    print "vectorized product"
    Z = np.matmul(X,Theta)
    print Z
    print
   
    print "iterative version"
    Z = np.zeros((4,1))

    #iterate over rows of X
    for rx in range(len(X)):
        #iterate over cols of Theta
        for cy in range(len(Theta[0])):
            #iterate over rows of Theta
            for ry in range(len(Theta)):
                Z[rx][cy] += X[rx][ry] * Theta[ry][cy]

    print Z
    print
    
main()
