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
    print("2X3 matrix")
    M = np.array([ [1,2,3],[4,5,6] ])
    print(M)
    print("Shape " + str(M.shape))
    print()

    print("column vector")
    CV = np.array([ [10],[122],[3], [9] ])
    print(CV)
    print("Shape " + str(CV.shape))
    print()

   
    print("row vector")
    RV = np.array( [ [10,122,3,9] ])
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

    print("addition")
    M = np.array([ [1,0],[2,5], [3,1] ])
    N = np.array([ [4,0.5],[2,5], [0,1] ])
    print(M + N)
    print()

    print("scalar multiplication")
    M = np.array([ [1,0],[2,5],[3,1] ])
    print("3 * M")
    print(3 * M)

    print("transpose")
    A = np.array([ ['a','b'],['c','d'] ])
    print(A)
    print("A transpose")
    print(A.T)

    print("matrix vector multiplication")
    A = np.array([ [1,3],[4,0],[2,1] ])
    B = np.array([ [1],[5] ])
    print(A)
    print(B)
    print(np.matmul(A,B))

    print("matrix maxtrix multiplication")
    A = np.array([ [1,3,2], [4,0,1] ])
    B = np.array([ [1,3],[0,1],[5,2] ])
    print(A)
    print(B)
    print(np.matmul(A,B))
    print()

    print("Identity matrices")
    A = np.array([ [1,2],[3,4] ])
    I = np.array([ [1,0],[0,1] ])
    print(A)
    print(I)
    print(np.matmul(A,I))
    print()
    
    print("matrix inverse")
    A = np.array([ [3,4],[2,16] ])
    print(A)
    print(lin.inv(A))
    print(np.matmul(A,lin.inv(A)))
    print()

    print("dot product")
    print("two column vectors")
    u = np.array([ [1],[2],[3] ])
    v = np.array([ [4],[5],[6] ])
    print(u)
    print(v)
    print(np.matmul(u.T,v))
    print("two row vectors")
    x = np.array([ [10, 20, 30] ])
    y = np.array([ [2, 3, 4] ])
    print(x)
    print(y)
    print(np.inner(x,y))
    print()

    print("power")
    x = np.array([1,2,3,4,5])
    print(x)
    print(np.power(x,3))
    print()

    print("reciprocal")
    x = np.array([1.0,2.0,3.0,4.0,5.0])
    print(np.reciprocal(x))
    print()

    print("element-wise operations")
    a = np.array([1,2,3,4])
    b = np.ones(4) + 1
    print(a - b)
    a = np.array([ [1],[2],[3],[4] ])
    b = np.array([ [1],[2],[3],[4] ])
    print(a * b)
    print()

    print("4 x 4 identity matrix")
    x4 = np.eye(4)
    print(x4)

    print("sum elements, columns and rows")
    a = np.array([[1,2],[3,4]])
    print(a)
    print("sum elements")
    print(a.sum()) #sum elements
    print("sum columns")
    print(a.sum(axis=0)) #sum columns
    print("sum rows")
    print(a.sum(axis=1)) #sum rows
    print()

    print("create a magic square")
    print("sum of every row and every column is equal")
    print("N must be odd")
    M = magic_square(3)
    print(M)
    print()

    print("max element")
    print(np.max(M)) #max element
    print("create row with max of each col")
    print(np.max(M,axis=0))
    print("create row with max of each rol")
    print(np.max(M,axis=1)) 
    print()


    print("insert a colum of zeros into an existing matrix")
    A = magic_square(5)
    print(A)
    B = np.insert(A,5,values=0,axis=1)
    print(B)
    print()
   
    print("Duplicate the last column")
    print(A)
    C = np.insert(A,5,values=A[:,4], axis = 1)
    print(C)

   

    print("Two Arguments for Vectorization")
    print()
    
    print("Two Matrices")
    X = np.array([[12,7,3],
                 [4,5,6],
                 [7,8,9]])
    print(X)
    print(X.shape)
    print()
    
    Y = np.array([[5,8,1,2],
                 [6,7,3,0],
                 [4,5,9,1]])
    print(Y)
    print(Y.shape)
    print()

    import time
    print("vectorized matrix multiplication")
    t0 = time.time()
    Z = np.matmul(X,Y)
    t1 =time.time()
    print(Z)
    print("time = " + str(t1-t0))
    print()

    print("iterative matrix multiplication")
    Z = np.zeros((3,4))

    t0 = time.time()
    #iterate over rows of X
    for rx in range(len(X)):
        #iterate over cols of Y
        for cy in range(len(Y[0])):
            #iterate over rows of Y
            for ry in range(len(Y)):
                Z[rx][cy] += X[rx][ry] * Y[ry][cy]
    t1 = time.time()
    print(Z)
    print("time = " + str(t1-t0))
    
    




