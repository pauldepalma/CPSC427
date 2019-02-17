'''
Demonstrates
    Plotting a function with matplotlib
    Install matplotlib from the command line using pip (pip is package manager for
    python)

To install matlib, bring up a terminal window:
    sudo apt-get install python-pip
    python -mpip install -U matplotlib
'''
from random import *
import numpy as np
import matplotlib.pyplot as plt

def main():
    #parameters for scatter plot
    N = 25
    colors = np.random.rand(N) #colors of points
    area = (100 * np.random.rand(N)) #size of points
    transp = 1 #translucence of points 
    p = [randint(0,50) for i in range(N)] 
    q = [randint(0,50) for i in range(N)] 
    plt.scatter(p,q, s=area, c=colors, alpha=transp)
    x = [i for i in range(0,100)]
    y = [i for i in x]
    plt.plot(x,y)
    plt.show()
    
main()
    
