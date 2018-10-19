import pandas
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from sklearn.model_selection import train_test_split
import numpy as np

dataset = pandas.read_csv("housing.csv", header=None).values

x_train, x_test, y_train, y_test = train_test_split(dataset[:,0:13], dataset[:,13], test_size = 0.25, random_state=87)

np.random.seed(155)
nn = Sequential()
nn.add(Dense(20, input_dim=13, activation='relu'))
nn.add(Dense(1, activation='sigmoid'))
nn.compile(loss='binary_crossentropy', optimizer='adam')
nn_fitted = nn.fit(x_train, y_train, epochs=100, verbose=0)

print(nn.summary())
print(nn.evaluate(x_test, y_test, verbose=0))