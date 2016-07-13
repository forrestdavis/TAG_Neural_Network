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
X_dev = numpy.load("X_dev.npy")
Y_dev = numpy.load("Y_dev.npy")

#Create model
model = Sequential()
model.add(Dense(400, input_dim=input_dimensions, init='uniform', activation='relu'))
model.add(Dense(300, input_dim=input_dimensions, activation='relu'))
model.add(Dense(200, input_dim=input_dimensions, activation='relu'))
model.add(Dense(100, input_dim=input_dimensions, activation='relu'))
model.add(Dense(50, input_dim=input_dimensions, activation='relu'))
model.add(Dense(output_dimensions, input_dim=input_dimensions, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
hist = model.fit(X_train, Y_train, nb_epoch=50, batch_size=1000)

scores = model.evaluate(X_dev, Y_dev)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
