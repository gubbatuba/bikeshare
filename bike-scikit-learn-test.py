import pylab as pl
from numpy import *
from sklearn import datasets, linear_model

X = genfromtxt('dataset1.csv', delimiter=',')
Y = genfromtxt('output.csv', delimiter=',')

print(X)
print(Y)