from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
import numpy

#Fix random to ensure consistent results during testing
seed = 4
numpy.random.seed(seed)

io_info = open("io_dimensions.txt", "r")
i = io_info.readline().split()
o = io_info.readline().split()

input_dimensions = int(o[1])
output_dimensions = int(o[2])

X_train = numpy.load("X_train.npy")
Y_train = numpy.load("Y_train.npy")

#Create model
model = Sequential()
model.add(Dense(150, input_dim = input_dimensions, init='uniform'))
model.add(Activation('relu'))
model.add(Dense(150))
model.add(Activation('relu'))
model.add(Dense(150))
model.add(Activation('relu'))
model.add(Dense(output_dimensions))
model.add(Activation('softmax'))

#Compile model
model.compile(loss='categorical_crossentropy', 
        optimizer='adam', metrics=['accuracy'])

hist = model.fit(X_train, Y_train, nb_epoch=50, batch_size=1000)

#Save model and weights
json_string = model.to_json()
open('150_model_architecture.json', 'w').write(json_string)
model.save_weights('150_model_weights.h5', overwrite=True)

