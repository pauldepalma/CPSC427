'''
Demonstrates:
    Plotting a function with matplotlib
    Install matplotlib from the command line using pip (pip is package manager for
    python)

To install matlib, bring up a terminal window:
    sudo apt-get install python-pip
    python -mpip install -U matplotlib
'''

import matplotlib.pyplot as plt


def main():
    x = [i for i in range(0,10)]
    y = [i**2 for i in x]
    plt.plot(x,y)
    plt.show()
    
main()
    
