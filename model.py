#import tensorflow as tf
#from tensorflow.keras.layers import Dense
#from tensorflow.keras import Sequential
import csv
#model.compile(optimizer='sgd', loss='mse', metrics=['accuracy'])
#model.fit(X, y, epochs=100, batch_size=32)

inputs = []
outputs = []
with open("output.csv", 'r') as csvfile:
    for line in csvfile:
        line = line.split(',')
        for item in line:
            inputs.append(item)
        for n in range(26):
            outputs.append(n)

print(inputs)
print(outputs)



X, y = df.values[:, :-1], df.values[:, -1]
# ensure all data are floating point values
X = X.astype('float32')
# encode strings to integer
y = LabelEncoder().fit_transform(y)
print(X_train.shape, X_test.shape)
# determine the number of input features
n_features = X_train.shape[1]
model = Sequential()
model.add(Dense(10, activation='relu', kernel_initializer='he_normal', input_shape=(n_features,)))
model.add(Dense(8, activation='relu', kernel_initializer='he_normal'))
model.add(Dense(26, activation='softmax'))
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=150, batch_size=32, verbose=0)
# evaluate the model
loss, acc = model.evaluate(X_test, y_test, verbose=0)
print('Test Accuracy: %.3f' % acc)
# make a prediction
row = [5.1,3.5,1.4,0.2]
yhat = model.predict([row])
print('Predicted: %s (class=%d)' % (yhat, argmax(yhat)))
