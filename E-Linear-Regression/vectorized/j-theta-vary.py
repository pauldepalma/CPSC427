from random import *
import numpy as np
import matplotlib.pyplot as plt

def j_theta(x,y,theta,m):
    jtheta = []
    for elt in theta:
        for i in range(m):
            th = [(elt*x[i] - y[i])**2 for i in range(m)]
        jtheta.append(1.0/(2*m) * sum(th))
    return jtheta

def main():
    #parameters for scatter plot
    m = 5 
    x = [i for i in range(1,m+1)]
    y = [i for i in x]
    theta = [2.0,1.5,1.0,0.5,0.0]
    jtheta = j_theta(x,y,theta,m)
    plt.scatter(theta,jtheta,color='g')
    plt.title("jtheta against variable theta")
    plt.show()
    
main()
    
