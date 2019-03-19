'''
Demonstrates
    Sigmoid function

To install matlib, bring up a terminal window:
    sudo apt-get install python-pip
    python -mpip install -U matplotlib
'''

from math import *
import matplotlib.pyplot as plt

def main():
    #parameters for scatter plot
   
   
    x = [i for i in range(-100,100)]
    y = [1.0/(1+exp(-i)) for i in x]
    plt.plot(x,y)
    plt.show()
    
main()
    
