from numpy import *
import matplotlib.pyplot as plt

def step_gradient(b_current, m_current, points, learningRate):
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

def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m
    for i in range(num_iterations):
        b, m = step_gradient(b, m, array(points), learning_rate)
    return [b, m]

def compute_mean_error(points,b,m):
    error = 0
    for i in range(0, len(points)):
        x = points[i,0]
        y = points[i,1]
        error += (y - (m * x + b)) ** 2 
    return (error / float(len(points))) ** 0.5

def display_error(m,b,error):
    print "Slope: " + str(m)
    print "Y Intercept: " + str(b)
    print "Error: " + str(error)

def plot_results(points,m,b):
    x_train = [point[0] for point in points]
    y_train = [point[1] for point in points]
    y_predict = [m*x + b for x in x_train]
    plt.plot(x_train,y_predict,color='red')
    plt.scatter(x_train,y_train,color='green')
    plt.show()

def init():
    points = genfromtxt("input.csv", delimiter=",")
    learning_rate = 0.0001
    b = 0 # initial y-intercept guess
    m = 0 # initial slope guess
    num_iter = 1000
    return points, learning_rate, b, m, num_iter

def main():
    points, learning_rate, b, m, num_iter = init()
    [b, m] = gradient_descent_runner(points, b, m, learning_rate, num_iter)
    error = compute_mean_error(points,b,m)
    display_error(m,b,error)
    plot_results(points,m,b)

main()
