import pandas as pd
from keras.models import Sequential
from keras.layers import *
import numpy as np
from sklearn.model_selection import train_test_split

training_data_df = pd.read_csv("0-64.csv")
del training_data_df['date']
del training_data_df['code']

training_data = training_data_df

train, test = train_test_split(training_data, test_size=0.1)

X = train.drop('Lunch', axis=1).values
Y = train[['Lunch']].values

X_test = test.drop('Lunch', axis=1).values
Y_test = test[['Lunch']].values

# Define the model
model = Sequential()
model.add(Dense(50, input_dim=3, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(50, activation='relu'))
model.add(Dense(1, activation='linear'))
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['acc'])

# Train the model
model.fit(
    X,
    Y,
    epochs=len(training_data),
    shuffle=True
)

test_error_rate = model.evaluate(X_test, Y_test, verbose=0)
print("The mean squared error (MSE) for the test data set is: {}".format(test_error_rate))

