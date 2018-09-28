import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets, metrics
from sklearn.model_selection import train_test_split

# Loading the dataset
irisdataset = datasets.load_iris()

# getting the data and response of the dataset
x = irisdataset.data
y = irisdataset.target
print(irisdataset.data)
print(irisdataset.target)

from sklearn.svm import SVC

X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=0)

svm = SVC()
svm.fit(X_train, y_train)
print('Accuracy of SVM classifier on training set: {:.2f}'.format(svm.score(X_train, y_train)))
print('Accuracy of SVM classifier on test set: {:.2f}'.format(svm.score(X_test, y_test)))