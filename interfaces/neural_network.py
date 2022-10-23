import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dense
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy
import numpy as np
import pandas as pd
import sklearn
from sklearn import preprocessing as pp
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
import tensorflow.lite as tflite
import time
import random
from data_processing import DataProcessing

class NeuralNetwork:

    def __init__(self, number_of_labels, labels, data, train_data_provided):
        self.number_of_labels = number_of_labels
        self.labels = labels
        self.data = data
        self.train_data_provided = train_data_provided
        self.processing = DataProcessing(self.data)
        
    def clean_data(self):    
        p = self.data
        try:
            p = p.drop(['Unnamed: 0'], axis=1)
            p = p.drop(['time'], axis=1)           
        except KeyError:
            pass

        p_columns = self.processing.series_to_list(p.columns)
        for column in p_columns:
            p[column].fillna(0, inplace=True)         
        raw_x = p.drop([self.labels], axis=1)
        p_columns = self.processing.series_to_list(raw_x.columns)
        for column in p_columns:
            for value in raw_x[column]:
                if type(value) == int:
                    pass
                else:
                    column_to_change = self.processing.series_to_list(raw_x[column])
                    for i in range(len(column_to_change)):
                        if type(column_to_change[i]) == int:
                            pass
                        else: 
                            try:
                                column_to_change[i] = int(column_to_change[i])
                            except ValueError:                                                   
                                column_to_change[i] = 0
                    raw_x[column] = pd.DataFrame(column_to_change)              
        clean_X = pd.DataFrame(raw_x) 

        #process the y vairable 
        # only convert strings 
        map_stirngs_to_digits = []
        for string in p[self.labels]:
            if type(string) == str:
                map_stirngs_to_digits.append(string)
            else:
                pass
        # get rid of the noise
        clean_map_of_strings = []
        for i in range(len(map_stirngs_to_digits)):
            string = map_stirngs_to_digits[i]
            if map_stirngs_to_digits.count(string) > 1:
                if string in clean_map_of_strings:
                    pass
                else:
                    clean_map_of_strings.append(string)
        #map each string class to a number
        for i in range(len(map_stirngs_to_digits)):
            for j in range(len(clean_map_of_strings)):
                string = map_stirngs_to_digits[i]
                classes = clean_map_of_strings[j]
                if string == classes:
                    map_stirngs_to_digits[i] = j
                else:
                    pass
        p[self.labels] = pd.DataFrame(map_stirngs_to_digits)
        print(p)
        try:
            X = np.array(clean_X.drop([0], axis=1))
        except KeyError:
            X = np.array(clean_X)
        Y = np.array(p[self.labels])
        if self.train_data_provided:
            pass
        else:
            train_labels, train_samples = shuffle(X,Y)            
        return train_labels, train_samples

    def initialize_model(self, X, Y):
        model = Sequential([
            Dense(units=len(self.data.columns), activation='relu'),
            Dense(units=32, activation='relu'),
            Dense(units=32, activation='relu'),
            Dense(units=self.number_of_labels, activation='softmax')
        ])

        X = np.asarray(X).astype('float32')
        model.compile(optimizer=Adam(learning_rate=0.0001), loss='sparse_categorical_crossentropy', metrics=['accuracy']) 

        model.fit(X, Y, epochs=30, shuffle=True, batch_size=30, use_multiprocessing=True, verbose=2)
        return model

    def save_best_model(self, x_data, y_data, repeats=15):
        model = self.initialize_model()
        best = (0, None)
        for n in range(repeats):
            x_train, x_test, y_train, y_test = train_test_split(x_data, y_data)
            model.fit(x_train, y_train, epochs=30, shuffle=True, batch_size=30, use_multiprocessing=True)
            acc = model.evaluate(x_data, y_data, use_multiprocessing=True)[1]
            if acc > best[0]:
                best = (acc, model)
        print(f'Best was {best[0] * 100}%')
        best[1].save('model2.tf')
        lite_model = tflite.TFLiteConverter.from_keras_model(best[1])
        open("model2.tflite", "wb").write(lite_model.convert())
        model = load_model('model2.tf')
        return model, acc

    def iterate_predictions(self, model, X, Y, labels):
        while True:
            position = random.randint(0,len(X))
            n1 = X[position]
            n = self.processing.series_to_list(n1)
            h = []
            h.append(n)
            n = np.array(h, dtype='float32')
            prediction = model.predict(n)
            try:
                predicted_label = labels[np.argmax(prediction)]
                actual_label = labels[Y[position]]
            except TypeError:
                predicted_label = prediction
                actual_label = Y[position]
            print(f"prediction : {predicted_label}, actual : {actual_label}")
            time.sleep(5)
        
labels = 'class'
filename = r'app\aps_failure_test_set.csv'
data = pd.read_csv(filename)
data = data.sample(n=200,axis='rows')
nnets = NeuralNetwork(2, labels, data, False)

X, Y = nnets.clean_data()