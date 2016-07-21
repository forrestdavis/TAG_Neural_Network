from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.callbacks import EarlyStopping
import numpy
import sys

#Fix random to ensure consistent results during testing
seed = 4
numpy.random.seed(seed)

io_info_train = open("io_dimensions_train_all.txt", "r")
io_info_test = open("io_dimensions_test.txt", "r")
one = io_info_train.readline().split()
two = io_info_test.readline().split()

input_dimensions = int(one[0])
output_dimensions = int(one[1])
i_dimensions = int(two[0])
o_dimensions = int(two[1])

#Ensure test and train data have same form
if input_dimensions!= i_dimensions:
    sys.stderr.write("There is a mismatch in input dimensions\n")
    sys.exit(1)
if output_dimensions!= o_dimensions:
    sys.stderr.write("There is a mismatch in output dimensions\n")
    sys.exit(1)

#Get train data
print "Getting data ..."
X_train = numpy.load("X_train_all.npy")
Y_train = numpy.load("Y_train_all.npy")

#Create model
print "creating model ..."
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

#Define early stopping 
early_stopping = EarlyStopping(monitor='val_loss', verbose = 1, patience=2)

print "fitting model..."
model.fit(X_train, Y_train, callbacks=[early_stopping], nb_epoch=50, verbose=1, batch_size=1000, 
         validation_split=0.1)

#Get test data
print "getting test data..."
X_test = numpy.load("X_dev.npy")
Y_test = numpy.load("Y_dev.npy")


#Get accurracy on test data
print "getting score on test..."
scores = model.evaluate(X_test, Y_test)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
