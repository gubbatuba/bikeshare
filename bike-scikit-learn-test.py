import pylab as pl
from numpy import *
from sklearn import datasets, linear_model, cross_validation

X = genfromtxt('dataset1.csv', delimiter=',')
Y = genfromtxt('output.csv', delimiter=',')

print(X)
print(Y)

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, Y, test_size=0.4, random_state=0)

clf = linear_model.Ridge (alpha = 1000)
clf.fit (X_train,y_train)
print(clf.score(X_test,y_test))

