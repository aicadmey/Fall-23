# -*- coding: utf-8 -*-
"""DL-RNN

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ExRZohEs4iDB6Qkk7iWzJnLq6pQ80sGH
"""

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from sklearn.model_selection import train_test_split
import numpy as np
html_code_examples = [
    "<div>Hello, World!</div>",
    "<h1>This is a heading</h1>",
    "<p>This is a paragraph</p>",
    "<img src='image.jpg' />",
    "<p>This is another paragraph</h1>",
    "<a href='https://example.com'>Visit our website</a>",
    "<h1>This is a correct heading</h1>",
    "<p>This is a correct paragraph</p>",
    "<a href='https://example.com'>Correct link</a>",
    "<img src='correct_image.jpg' />",
]

bad_practices = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0]

tokenizer = Tokenizer()
tokenizer.fit_on_texts(html_code_examples)
total_words = len(tokenizer.word_index) + 1
sequences = tokenizer.texts_to_sequences(html_code_examples)
padded_sequences = pad_sequences(sequences)
X = np.array(padded_sequences)
y = np.array(bad_practices)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = Sequential()
model.add(Embedding(total_words, 16, input_length=X.shape[1]))
model.add(LSTM(100))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Accuracy: {accuracy * 100:.2f}%")

import matplotlib.pyplot as plt
history = model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))
def plot_history(history):
    plt.plot(history.history['accuracy'], label='Training Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.title('Training and Validation Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.show()

    plt.plot(history.history['loss'], label='Training Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.title('Training and Validation Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()
plot_history(history)
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Accuracy: {accuracy * 100:.2f}%")