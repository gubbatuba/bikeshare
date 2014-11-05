print(__doc__)


# Code source: Jaques Grobler
# License: BSD 3 clause


import pylab as pl
import numpy*
from sklearn import datasets, linear_model

X = genfromtxt('dataset1.csv', delimiter=',')
Y = genfromtxt('output.csv', delimiter=',')