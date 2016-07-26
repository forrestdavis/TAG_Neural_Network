from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout, LSTM
from keras.callbacks import EarlyStopping
import numpy
import sys

#Fix random to ensure consistent results during testing
#seed = 4
#numpy.random.seed(seed)

#Get arguments from command line
#Arguments represnt model parameters

io_info_train = open("io_dimensions_train_1000.txt", "r")
io_info_test = open("io_dimensions_test.txt", "r")
one = io_info_train.readline().split()
two = io_info_test.readline().split()

input_examples = int(one[0])
input_dimensions = int(one[1])
output_dimensions = int(one[2])
i_dimensions = int(two[1])
o_dimensions = int(two[2])

#Ensure test and train data have same form
if input_dimensions!= i_dimensions:
    sys.stderr.write("There is a mismatch in input dimensions\n")
    sys.exit(1)
if output_dimensions!= o_dimensions:
    sys.stderr.write("There is a mismatch in output dimensions\n")
    sys.exit(1)
io_info_test = open("io_dimensions_test.txt", "r")
two = io_info_test.readline().split()

#Get train data
print "Getting data ..."
X_train = numpy.load("X_train_1000.npy")
Y_train = numpy.load("Y_train_1000.npy")

#Create model
print "creating model ..."

model = Sequential()
model.add(LSTM(32, input_shape = (input_examples, input_dimensions)))
model.add(Dense(output_dimensions, activation='softmax'))

#Compile model
model.compile(optimizer='rmsprop',loss='categorical_crossentropy') 

#Define early stopping 
early_stopping = EarlyStopping(monitor='val_loss', verbose = 1, patience=2)

print "training model..."
model.fit(X_train, Y_train, callbacks=[early_stopping], nb_epoch=25, verbose=1, batch_size=1000, 
         validation_split=0.1)

#Get test data
print "getting test data..."
X_test = numpy.load("X_dev_allFeatures.npy")
Y_test = numpy.load("Y_dev_allFeatures.npy")


#Get accurracy on test data
print "getting score on test..."
scores = model.evaluate(X_test, Y_test)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
