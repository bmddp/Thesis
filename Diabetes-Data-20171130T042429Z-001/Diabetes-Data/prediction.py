import pandas as pd
from keras.models import Sequential
from keras.layers import *
import numpy as np
from sklearn.model_selection import train_test_split

training_data_df = pd.read_csv("person1.csv")
del training_data_df['date']
del training_data_df['code']

train, test = train_test_split(training_data_df, test_size=0.2)

X = train.drop('Bedtime', axis=1).values
# Y = train[['code']].values
Y = train[['Bedtime']].values

X_test = test.drop('Bedtime', axis=1).values
Y_test = test[['Bedtime']].values

# Define the model
model = Sequential()
model.add(Dense(50, input_dim=3, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(50, activation='relu'))
model.add(Dense(1, activation='linear'))
model.compile(loss='mean_squared_error', optimizer='adam')

# Train the model
model.fit(
    X,
    Y,
    epochs=30,
    shuffle=True
)

test_error_rate = model.evaluate(X_test, Y_test, verbose=0)
print("The mean squared error (MSE) for the test data set is: {}".format(test_error_rate))


X = pd.read_csv("person1_test.csv").values

# Make a prediction with the neural network
prediction = model.predict(X)

# Grab just the first element of the first prediction (since that's the only have one)
prediction = prediction[0]

for i in prediction:
	print("Earnings Prediction for Proposed Product - ${}".format(i))
