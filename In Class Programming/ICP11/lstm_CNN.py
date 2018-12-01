from __future__ import print_function

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.layers import Embedding
from keras.layers import LSTM
from keras.layers import Conv1D, MaxPooling1D
from keras.preprocessing.text import Tokenizer
from nltk.corpus import stopwords
import nltk
import pandas as pd
from nltk.stem import WordNetLemmatizer


nltk.download("stopwords")
# Embedding

maxlen = 100
embedding_size = 128

# Convolution
kernel_size = 5
filters = 64
pool_size = 4

# LSTM
lstm_output_size = 70

# Training
batch_size = 30
epochs = 2

'''
Note:
batch_size is highly sensitive.
Only 2 epochs are needed as the dataset is very small.
'''

print('Loading data...')

stop_words = stopwords.words('english')

df1 = pd.read_csv('imdb_master.csv', encoding='latin1')
df1 = df1[df1['label']!= 'unsup']
df1['label'] = df1['label'].map({'neg':0,'pos':1})
df1.apply(lambda x: x.astype(str).str.lower())
max_features= 6000
tokenizer = Tokenizer(num_words=max_features)
tokenizer.fit_on_texts(df1['review'])
list_tokenized_train= tokenizer.texts_to_sequences(df1['review'])
list_no_stop = []
for token in list_tokenized_train:
    if (token not in stop_words):
        list_no_stop.append(token)

max_len= 130
x_train= sequence.pad_sequences(list_no_stop, maxlen=max_len)
y_train= df1['label']

print('Pad sequences (samples x time)')
x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
print('x_train shape:', x_train.shape)

print('Build model...')

model = Sequential()
model.add(Embedding(max_features, embedding_size, input_length=maxlen))
model.add(Dropout(0.25))
model.add(Conv1D(filters,
                 kernel_size,
                 padding='valid',
                 activation='relu',
                 strides=1))
model.add(MaxPooling1D(pool_size=pool_size))
model.add(LSTM(lstm_output_size))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

print('Train...')
model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs
)

model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
model.save_weights("model.h5")
