'''
Demonstrates
    Plotting a linear decison boundary
    We have two features
    theta = [-3, 1, 1]
    h_theta = g(theta_transpose * X) = g(theta0*X0+theta1*x1+theta2*x2)
    y = 1 if h_theta(X) >= 0
    y = 1 if -3*X0 + 1*x1 + +*x2 >= 0

    So, x1 + x2 >= 3
    and x2 = -x1 + 3

    The program plots x2 = -x1 + 3
    and randomly generates values above and below the line
    
'''
import random
import numpy as np
import matplotlib.pyplot as plt

def main():
    m = -1
    b = 3
    lower = -20
    upper = 20
    
    num_points = 25
    x1 = [random.randrange(start=1,stop=9) for i in range(num_points)]
    x2 = [random.randrange(start=1,stop=9) for i in range(num_points)]

    y1 = [random.randrange(start=lower,stop=(m*x+b)-1) for x in x1]
    y2 = [random.randrange(start=1 + m*x+b ,stop=upper) for x in x2]
    plt.plot(np.arange(num_points), m*np.arange(num_points) + b)
    plt.scatter(x1,y1,c='blue')
    plt.scatter(x2,y2,c='red')
    plt.show()
        

    
main()
    
