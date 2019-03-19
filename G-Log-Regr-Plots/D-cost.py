'''
Demonstrates
    cost function for logistic regression

To install matlib, bring up a terminal window:
    sudo apt-get install python-pip
    python -mpip install -U matplotlib
'''
import math as m
import numpy as np
import matplotlib.pyplot as plt

def main():

    
   
    x = np.linspace(.001,.99,100)
    
    #y = [-m.log(i) for i in x]
    y = [-m.log(1-i) for i in x]
    plt.plot(x,y)
    plt.show()
    
main()
    
