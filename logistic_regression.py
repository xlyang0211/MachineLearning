__author__ = 'seany'

from math import exp
from numpy import *
class LogisticRegression:
    def logistic_regression(self, x, y):
        theta = [0] * len(x)
        alpha = 0.01
        for i in theta:

    def h_x(self, theta, x):
        return 1 / (1 + exp(-dot(theta, x)))