from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout, Merge
from keras.callbacks import EarlyStopping
import dimensions as d
import numpy
import sys

#Get dimensions of data and check for errors
dimensions_dictionary = d.get_dimensions("data_1000/io_dimensions_1000.txt")
d.error_check_dimensions(dimensions_dictionary)

#Get train data
(X_train_A, X_train_B, X_train_C, X_train_D, X_train_E, X_train_F, 
X_train_G, X_train_H, X_train_I, X_train_J, X_train_K, X_train_L, 
X_train_M, X_train_N, X_train_O, X_train_P, X_train_Q, X_train_R,
X_train_S, X_train_T, X_train_U, 
            #X_train_form, X_train_pos
Y_train) = d.getTrainData("data_1000/numpy_arrays")

#Get test data
'''
(X_test_A, X_test_B, X_test_C, X_test_D, X_test_E, X_test_F, 
X_test_G, X_test_H, X_test_I, X_test_J, X_test_K, X_test_L, 
X_test_M, X_test_N, X_test_O, X_test_P, X_test_Q, X_test_R,
X_test_S, X_test_T, X_test_U, 
            #X_test_form, X_test_pos
Y_test) = d.getTestData("data_1000/numpy_arrays")
'''
test_data = d.getTestData("data_1000/numpy_arrays")
print len(test_data)
print type(test_data)
print test_data[0]
print test_data[:1][0]
X_test_data = test_data[:len(test_data)-1]
Y_test = test_data[len(test_data)-1]
print len(X_test_data)

model = d.createModel(dimensions_dictionary)

#Define early stopping 
early_stopping = EarlyStopping(monitor='val_loss', verbose = 1, patience=2)

print "fitting model..."
model.fit([X_train_A, X_train_B, X_train_C, X_train_D, X_train_E, X_train_F, X_train_G, X_train_H, X_train_I, X_train_J, 
X_train_K, X_train_L, X_train_M, X_train_N, X_train_O, X_train_P, X_train_Q, X_train_R, X_train_S, X_train_T, X_train_U], 
Y_train, callbacks=[early_stopping], nb_epoch=2, verbose=1, batch_size=1000, 
         validation_split=0.1)

#Get accurracy on test data
print "getting score on test..."
'''
scores = model.evaluate([X_test_A, X_test_B, X_test_C, X_test_D, X_test_E, X_test_F, X_test_G, X_test_H,
X_test_I, X_test_J, X_test_K, X_test_L, X_test_M, X_test_N, X_test_O, X_test_P, X_test_Q, X_test_R, 
X_test_S, X_test_T, X_test_U], Y_test)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
'''
scores = model.evaluate(X_test_data, Y_test)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
