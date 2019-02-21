from random import *
import numpy as np
import matplotlib.pyplot as plt


def h_minus_y(x,y,theta1):
    return  (h_theta(theta1,x) - y)**2

def h_theta(theta1,x):
    return theta1 * x

def main():
    #parameters for scatter plot
    m = 100 
    X = [i for i in range(0,m)]
    theta = 1
    Y = [theta*i for i in X]
    plt.plot(X,Y,color='g')
    plt.title("h_theta(x) for theta1 = 1. y = x")
    plt.show()
    
main()
    
