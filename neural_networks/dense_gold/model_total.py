from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
import numpy
import sys

#Fix random to ensure consistent results during testing
#seed = 4
#numpy.random.seed(seed)

io_info_train = open("io_dimensions_train.txt", "r")
io_info_test = open("io_dimensions_test.txt", "r")
one = io_info_train.readline().split()
two = io_info_test.readline().split()

input_dimensions = int(one[0])
output_dimensions = int(one[1])
i_dimensions = int(two[0])
o_dimensions = int(two[1])

if input_dimensions!= i_dimensions:
    sys.stderr.write("There is a mismatch in input dimensions\n")
    sys.exit(1)
if output_dimensions!= o_dimensions:
    sys.stderr.write("There is a mismatch in output dimensions\n")
    sys.exit(1)
print "Getting training data...."
X_train = numpy.load("X_train.npy")
Y_train = numpy.load("Y_train.npy")

print "Getting testing data..."
X_test = numpy.load("X_dev.npy")
Y_test = numpy.load("Y_dev.npy")

print Y_test[0]
#Create model
print "Creating model..."
model = Sequential()
model.add(Dense(150, input_dim = input_dimensions, init='uniform'))
model.add(Activation('relu'))
model.add(Dense(150))
model.add(Activation('relu'))
model.add(Dense(output_dimensions))
model.add(Activation('softmax'))

#Compile model
model.compile(loss='categorical_crossentropy', 
        optimizer='adam', metrics=['accuracy'])

print "Fitting model...."
hist = model.fit(X_train, Y_train, nb_epoch=50, batch_size=1000)

#Evaluate model

scores = model.evaluate(X_test, Y_test)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
