'''
Iterative version of gradient descent for linear regression
Code is adapted from and data comes from
: ...github.com/mattnedrich/GradientDescentExample
'''
import numpy
import csv
import matplotlib.pyplot as plt

def gradient(b_current, m_current, points, learningRate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(2/N) * (y - ((m_current * x) + b_current))
        m_gradient += -(2/N) * x * (y - ((m_current * x) + b_current))
    new_b = b_current - (learningRate * b_gradient)
    new_m = m_current - (learningRate * m_gradient)
    return [new_b, new_m]

def gradient_descent(points, starting_b, starting_m, learning_rate, num_iter):
    b = starting_b
    m = starting_m
    for i in range(num_iter):
        b, m = gradient(b, m, points, learning_rate)
    return [b, m]

def plot_results(points,m,b):
    x_train = [point[0] for point in points]
    y_train = [point[1] for point in points]
    y_predict = [m*x + b for x in x_train]
    plt.plot(x_train,y_predict,color='r')
    plt.scatter(x_train,y_train,color='g')
    plt.title("Iterative Linear Regression")
    plt.show()

def init():

    #read file into list of x,y coordinates, one set per line
    reader = list(csv.reader(open("input.csv", "rb"), delimiter=','))
    points = numpy.array(reader).astype('float')

    #set the initial parameters
    learning_rate = 0.0001  #step size
    b = 0 # initial y-intercept guess
    m = 0 # initial slope guess
    num_iter = 1000 #number of iterations of gradient across all points
    return points, learning_rate, b, m, num_iter

def main():
    points, learning_rate, b, m, num_iter = init()
    [b, m] = gradient_descent(points, b, m, learning_rate, num_iter)
    plot_results(points,m,b)

main()
