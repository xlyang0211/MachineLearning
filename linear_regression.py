from numpy import *
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

__author__ = 'seany'



def theta_x(x, theta):
    #print x, theta
    ret = dot(transpose(x), transpose(theta))
    #print ret
    return ret

def get_j_theta(x, y, theta):
    tmp =  dot(x, theta) - y
    print tmp
    ret = sum([i ** 2 for i in tmp]) / 2
    #print "j(theta) is: ", ret
    return ret

def gradient_descent(theta, alpha, x, y):
    for j in xrange(len(theta)):
        old = float('inf')
        new = get_j_theta(x, y, theta)
        while new < old:
            old = new
            for i in xrange(len(x)):
                theta[j] = theta[j] - alpha * (y[i] - theta_x(x[i], theta)) * x[i][j]
                print theta
            new = get_j_theta(x, y, theta)
            print "new is: ", new

if __name__ == "__main__":
    alpha = 0.01
    theta = array([100, 100])
    x = array([
    [1, 81],
    [1, 76],
    [1, 99],
    [1, 83],
    [1, 120]])
    y = array([180, 171, 198, 185, 248])

    gradient_descent(theta, alpha, x, y)
    print theta
