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

io_info_train = open("io_dimensions_train.txt", "r")
io_info_test = open("io_dimensions_dev.txt", "r")
one = io_info_train.readline().split()
two = io_info_test.readline().split()

train_nb_samples = int(one[0])
train_sentence_size = int(one[1])
train_input_dim = int(one[2])

test_nb_samples = int(two[0])
test_sentence_size = int(two[1])
test_input_dim = int(two[2])

#Ensure test and train data have same form
if train_input_dim!= test_input_dim:
    sys.stderr.write("There is a mismatch in input dimensions\n")
    sys.exit(1)

#Get train data
print "Getting train data ..."
X_train = numpy.load("X_train_lstm.npy")
Y_train = numpy.load("Y_train_lstm.npy")
print X_train[0]

#Create model
print "creating model ..."

model = Sequential()
model.add(LSTM(32, input_shape = (test_nb_samples, train_sentence_size, train_input_dim), return_sequences = True))

#Compile model
model.compile(optimizer='adam',loss='binary_crossentropy') 

#Define early stopping 
early_stopping = EarlyStopping(monitor='val_loss', verbose = 1, patience=2)

print "training model..."
model.fit(X_train, Y_train, callbacks=[early_stopping], nb_epoch=25, verbose=1, batch_size=1000, 
         validation_split=0.1)

#Get test data
print "getting test data..."
X_test = numpy.load("X_dev_lstm.npy")
Y_test = numpy.load("Y_dev_lstm.npy")


#Get accurracy on test data
print "getting score on test..."
scores = model.evaluate(X_test, Y_test)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
