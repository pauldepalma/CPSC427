import numpy as np
import numpy.linalg as lin

def magic_square(N):
    mag = np.zeros((N,N), dtype=int)
    
    n = 1
    i, j = 0, N//2

    while n <= N**2:
        mag[i,j] = n
        n+=1
        newi, newj = (i-1)%N, (j+1)%N
        if mag[newi,newj]:
            i+= 1
        else:
            i, j = newi, newj
    return mag


def main():
    print "3X2 matrix"
    M = np.array([ [1,2],[3,4],[5,6] ])
    print M
    print

    print "row vector"
    RV = np.array( [ [1],[2],[3] ])
    print RV
    print

    print "column vector"
    CV = np.array([1,2,3])
    print CV
    print    

    print "dimensions"
    print M.shape
    print RV.shape
    print CV.shape
    print

    print "special matrices"
    A = np.ones((3,3))
    print A
    B = np.zeros((3,2))
    print B
    C = np.full((2,2),7)
    print C
    D = np.random.random((5,5))
    print D
    print

    print "matrix multiplicaition"
    N = np.array([ [1,1],[2,2] ])
    print M
    print M.shape
    print N.shape
    P = np.matmul(M,N)
    print P
    print P.shape
    print

    print "element-wise operations"
    x1 = np.array([1,2,3,4,5])
    print np.dot(x1,3)
    print np.power(x1,3)
    print 2**x1
    x2 = x1 * 2
    print x2
    a = np.array([1,2,3,4])
    b = np.ones(4) + 1
    print a - b
    x3 = np.array([1.0,2.0,3.0,4.0,5.0])
    print np.reciprocal(x3)
    print


    print "identity and inverse matrices"
    x4 = np.eye(4)
    print x4
    a = np.array([[3.,4.],[2.,16.] ])
    ainv = lin.inv(a)
    print ainv
    print np.matmul(a,ainv)

    print "sum elements, columns and rows"
    a = np.array([[1,2],[3,4]])
    print a.sum() #sum elements
    print a.sum(axis=0) #sum columns
    print a.sum(axis=1) #sum rows
    print

    print "transpose"
    b = np.array([ [1,2,3],[4,5,6] ])
    print b
    print b.transpose()
    print 


    print "create a magic square"
    print "N must be odd"
    M = magic_square(3)
    print M
    print

    print "max"
    print np.max(M) #max element
    print np.max(M,axis=0) #row vector with max of each col
    print np.max(M,axis=1) #row vector with max of each row
    print

    print "insert a colum of zeros into an existing matrix"
    A = magic_square(3)
    print A
    B = np.insert(A,3,values=0,axis=1)
    print B
    print

   
    print "Duplicate the last column"
    print A
    C = np.insert(A,3,values=A[:,2], axis = 1)
    print C
   

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
    
    
    print "Multiply Vectors"
    X = np.array([[1,2,3]])
    print X.shape

    Y = np.array([ [1],
                   [2],
                   [3]])
    print Y.shape


    Z = np.matmul(X,Y)
    print Z


    
main()



main()
