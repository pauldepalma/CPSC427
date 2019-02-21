from random import *
import numpy as np
import matplotlib.pyplot as plt


def h_minus_y(x,y,theta1):
    return  (h_theta(theta1,x) - y)**2

def h_theta(theta1,x):
    return theta1 * x

def main():
    #parameters for scatter plot
    m = 3 
    X = [i for i in range(0,m)]
    Y = [i for i in X]
    theta1 = 1 
    j_theta1 = 1/(2*m) * sum([h_minus_y(X[i],Y[i],theta1) for i in range(m)])
    plt.scatter(theta1,j_theta1,color='g')
    plt.title("jtheta 1 against theta1")
    plt.show()
    
main()
    
