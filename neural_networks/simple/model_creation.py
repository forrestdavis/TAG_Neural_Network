from keras.models import Sequential
from keras.layers import Dense
import numpy
#import transform_fann

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
X_test = numpy.load("X_test.npy")
Y_test = numpy.load("Y_test.npy")

#Create model
model = Sequential()
model.add(Dense(400, input_dim=input_dimensions, init='uniform', activation='relu'))
model.add(Dense(300, input_dim=input_dimensions, activation='relu'))
model.add(Dense(200, input_dim=input_dimensions, activation='relu'))
model.add(Dense(100, input_dim=input_dimensions, activation='relu'))
model.add(Dense(50, input_dim=input_dimensions, activation='relu'))
model.add(Dense(output_dimensions, input_dim=input_dimensions, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
hist = model.fit(X_train, Y_train, nb_epoch=50, batch_size=10)

json_string = model.to_json()
open('C_model_architecture.json', 'w').write(json_string)
model.save_weights('C_model_weights.h5')

