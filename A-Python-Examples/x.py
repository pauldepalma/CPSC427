'''
Demonstrates
    Plotting a decison boundary
    
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
    
