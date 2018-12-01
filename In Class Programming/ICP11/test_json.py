from __future__ import print_function

from keras.preprocessing import sequence
from keras.datasets import imdb
from keras.models import model_from_json

maxlen = 100
max_features = 20000
print('Loading data...')
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)
x_test = sequence.pad_sequences(x_test, maxlen=maxlen)

json = open('model.json', 'r')
loaded_model_json = json.read()
json.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("model.h5")
print("successfully loaded model")

loaded_model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
score, acc = loaded_model.evaluate(x_test, y_test, verbose=0)
print('Test score:', score)
print('Test accuracy:', acc)

