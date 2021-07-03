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
    print("3X2 matrix")
    M = np.array([ [1,2],[3,4],[5,6] ])
    print(M)
    print("Shape " + str(M.shape))
    print()

    print("column vector")
    CV = np.array([ [1],[2],[3]  ])
    print(CV)
    print("Shape " + str(CV.shape))
    print()
   
    print("row vector")
    RV = np.array( [ [1,2,3] ])
    print(RV)
    print("Shape " + str(RV.shape))
    print()
   

    print("special matrices")
    A = np.ones((3,2))
    print("Fill with 1s")
    print(A)
    print(A.shape)
    print()
    
    B = np.zeros((3,2))
    print("Fill with 0s")
    print(B)
    print(B.shape)
    print()
    
    C = np.full((3,2),7)
    print("Fill with 7s")
    print(C)
    print(C.shape)
    print()

    D = np.random.random((3,2))
    print("fill with random numbers")
    print(D)
    print(D.shape)
    print()

    E = np.random.randint(1,11,size=(3,2))
    print("fill with random inbtegers in range [1..10]")
    print(E)
    print(E.shape)
    print()

    print("Scalar")
    F = np.array([ [1,1],[2,2],[3,3] ])
    print(F)
    print("X 3")
    print(F*3)
    print()
   

    print("Dot(or inner )Product of two column vectors")
    G = np.array([ [1],[2],[3] ])
    print(G)
    H = np.array([ [1],[2],[3] ])
    print(H)
    print("Transpose the first vector")
    print("Row X Col")
    G = G.T
    print(G)
    print(np.dot(G,H))
    print()

    print("Dot(or inner )Product of two row vectors")
    I = np.array([ [1,2,3] ])
    print(I)
    J = np.array([ [1,2,3] ])
    print(J)
    print("Transpose the first vector")
    print("Col X Row")
    I = I.T
    print(I)
    print(np.dot(I,J))
    print()
    
    quit()


'''
    print "matrix multiplicaition"
    N = np.array([ [1,1],[2,2] ])
    print M
    print M.shape
    print N.shape
    P = np.matmul(M,N)
    print P
    print P.shape
    print

    print "dot product, power, reciprocal"
    x1 = np.array([1,2,3,4,5])
    print np.dot(x1,3)
    print np.power(x1,3)
    print 2**x1
    x2 = x1 * 2
    print x2
    x3 = np.array([1.0,2.0,3.0,4.0,5.0])
    print np.reciprocal(x3)
    print

    print "element-wise operations"
    a = np.array([1,2,3,4])
    b = np.ones(4) + 1
    print a - b
    a = np.array([ [1],[2],[3],[4] ])
    b = np.array([ [1],[2],[3],[4] ])
    print a * b
    pnt


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
    b = np.array([ [1,3],[4,0],[2,1]])
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


'''    
main()




