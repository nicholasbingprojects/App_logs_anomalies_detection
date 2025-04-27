import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from keras.models import Sequential
from keras.layers import Dense
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report  # This line is crucial

class RandomForestModel:
    def __init__(self):
        self.model = RandomForestClassifier()

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)

    def evaluate(self, y_test, y_pred):
        return classification_report(y_test, y_pred)

class NeuralNetworkModel:
    def __init__(self, input_shape):
        self.model = Sequential()
        self.model.add(Dense(64, activation='relu', input_shape=(input_shape,)))
        self.model.add(Dense(1, activation='sigmoid'))  # Adjust based on your output

    def compile(self):
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    def train(self, X_train, y_train, epochs=10, batch_size=32):
        self.model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size)

    def evaluate(self, X_test, y_test):
        return self.model.evaluate(X_test, y_test)