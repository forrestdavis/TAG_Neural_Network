from keras.models import Sequential, model_from_json
from keras.layers import Dense, Activation, Dropout, Merge
from keras.callbacks import EarlyStopping
import numpy
import sys

#Get train data
print "Getting A data ..."
X_train_A = numpy.load("./data_1000/X_train_A_1000.npy")
Y_train_A = numpy.load("./data_1000/Y_train_A_1000.npy")
X_test_A = numpy.load("./data_1000/X_test_A_1000.npy")
Y_test_A = numpy.load("./data_1000/Y_test_A_1000.npy")

print "Getting B data ..."
X_train_B = numpy.load("./data_1000/X_train_B_1000.npy")
Y_train_B = numpy.load("./data_1000/Y_train_B_1000.npy")
X_test_B = numpy.load("./data_1000/X_test_B_1000.npy")
Y_test_B = numpy.load("./data_1000/Y_test_B_1000.npy")

print "Getting C data ..."
X_train_C = numpy.load("./data_1000/X_train_C_1000.npy")
Y_train_C = numpy.load("./data_1000/Y_train_C_1000.npy")
X_test_C = numpy.load("./data_1000/X_test_C_1000.npy")
Y_test_C = numpy.load("./data_1000/Y_test_C_1000.npy")

print "Getting D data ..."
X_train_D = numpy.load("./data_1000/X_train_D_1000.npy")
Y_train_D = numpy.load("./data_1000/Y_train_D_1000.npy")
X_test_D = numpy.load("./data_1000/X_test_D_1000.npy")
Y_test_D = numpy.load("./data_1000/Y_test_D_1000.npy")

print "Getting E data ..."
X_train_E = numpy.load("./data_1000/X_train_E_1000.npy")
Y_train_E = numpy.load("./data_1000/Y_train_E_1000.npy")
X_test_E = numpy.load("./data_1000/X_test_E_1000.npy")
Y_test_E = numpy.load("./data_1000/Y_test_E_1000.npy")

'''
print "Getting F data ..."
X_train_F = numpy.load("./data_1000/X_train_F_1000.npy")
Y_train_F = numpy.load("./data_1000/Y_train_F_1000.npy")
X_test_F = numpy.load("./data_1000/X_test_F_1000.npy")
Y_test_F = numpy.load("./data_1000/Y_test_F_1000.npy")

print "Getting G data ..."
X_train_G = numpy.load("./data_1000/X_train_G_1000.npy")
Y_train_G = numpy.load("./data_1000/Y_train_G_1000.npy")
X_test_G = numpy.load("./data_1000/X_test_G_1000.npy")
Y_test_G = numpy.load("./data_1000/Y_test_G_1000.npy")
'''

print "Getting H data ..."
X_train_H = numpy.load("./data_1000/X_train_H_1000.npy")
Y_train_H = numpy.load("./data_1000/Y_train_H_1000.npy")
X_test_H = numpy.load("./data_1000/X_test_H_1000.npy")
Y_test_H = numpy.load("./data_1000/Y_test_H_1000.npy")

print "Getting I data ..."
X_train_I = numpy.load("./data_1000/X_train_I_1000.npy")
Y_train_I = numpy.load("./data_1000/Y_train_I_1000.npy")
X_test_I = numpy.load("./data_1000/X_test_I_1000.npy")
Y_test_I = numpy.load("./data_1000/Y_test_I_1000.npy")

print "Getting J data ..."
X_train_J = numpy.load("./data_1000/X_train_J_1000.npy")
Y_train_J = numpy.load("./data_1000/Y_train_J_1000.npy")
X_test_J = numpy.load("./data_1000/X_test_J_1000.npy")
Y_test_J = numpy.load("./data_1000/Y_test_J_1000.npy")

print "Getting K data ..."
X_train_K = numpy.load("./data_1000/X_train_K_1000.npy")
Y_train_K = numpy.load("./data_1000/Y_train_K_1000.npy")
X_test_K = numpy.load("./data_1000/X_test_K_1000.npy")
Y_test_K = numpy.load("./data_1000/Y_test_K_1000.npy")

print "Getting L data ..."
X_train_L = numpy.load("./data_1000/X_train_L_1000.npy")
Y_train_L = numpy.load("./data_1000/Y_train_L_1000.npy")
X_test_L = numpy.load("./data_1000/X_test_L_1000.npy")
Y_test_L = numpy.load("./data_1000/Y_test_L_1000.npy")

print "Getting M data ..."
X_train_M = numpy.load("./data_1000/X_train_M_1000.npy")
Y_train_M = numpy.load("./data_1000/Y_train_M_1000.npy")
X_test_M = numpy.load("./data_1000/X_test_M_1000.npy")
Y_test_M = numpy.load("./data_1000/Y_test_M_1000.npy")

print "Getting N data ..."
X_train_N = numpy.load("./data_1000/X_train_N_1000.npy")
Y_train_N = numpy.load("./data_1000/Y_train_N_1000.npy")
X_test_N = numpy.load("./data_1000/X_test_N_1000.npy")
Y_test_N = numpy.load("./data_1000/Y_test_N_1000.npy")

print "Getting O data ..."
X_train_O = numpy.load("./data_1000/X_train_O_1000.npy")
Y_train_O = numpy.load("./data_1000/Y_train_O_1000.npy")
X_test_O = numpy.load("./data_1000/X_test_O_1000.npy")
Y_test_O = numpy.load("./data_1000/Y_test_O_1000.npy")

print "Getting P data ..."
X_train_P = numpy.load("./data_1000/X_train_P_1000.npy")
Y_train_P = numpy.load("./data_1000/Y_train_P_1000.npy")
X_test_P = numpy.load("./data_1000/X_test_P_1000.npy")
Y_test_P = numpy.load("./data_1000/Y_test_P_1000.npy")

print "Getting Q data ..."
X_train_Q = numpy.load("./data_1000/X_train_Q_1000.npy")
Y_train_Q = numpy.load("./data_1000/Y_train_Q_1000.npy")
X_test_Q = numpy.load("./data_1000/X_test_Q_1000.npy")
Y_test_Q = numpy.load("./data_1000/Y_test_Q_1000.npy")

print "Getting R data ..."
X_train_R = numpy.load("./data_1000/X_train_R_1000.npy")
Y_train_R = numpy.load("./data_1000/Y_train_R_1000.npy")
X_test_R = numpy.load("./data_1000/X_test_R_1000.npy")
Y_test_R = numpy.load("./data_1000/Y_test_R_1000.npy")

print "Getting S data ..."
X_train_S = numpy.load("./data_1000/X_train_S_1000.npy")
Y_train_S = numpy.load("./data_1000/Y_train_S_1000.npy")
X_test_S = numpy.load("./data_1000/X_test_S_1000.npy")
Y_test_S = numpy.load("./data_1000/Y_test_S_1000.npy")

print "Getting T data ..."
X_train_T = numpy.load("./data_1000/X_train_T_1000.npy")
Y_train_T = numpy.load("./data_1000/Y_train_T_1000.npy")
X_test_T = numpy.load("./data_1000/X_test_T_1000.npy")
Y_test_T = numpy.load("./data_1000/Y_test_T_1000.npy")

print "Getting U data ..."
X_train_U = numpy.load("./data_1000/X_train_U_1000.npy")
Y_train_U = numpy.load("./data_1000/Y_train_U_1000.npy")
X_test_U = numpy.load("./data_1000/X_test_U_1000.npy")
Y_test_U = numpy.load("./data_1000/Y_test_U_1000.npy")

print "Getting pos data ..."
X_train_pos = numpy.load("./data_1000/X_train_pos_1000.npy")
Y_train_pos = numpy.load("./data_1000/Y_train_pos_1000.npy")
X_test_pos = numpy.load("./data_1000/X_test_pos_1000.npy")
Y_test_pos = numpy.load("./data_1000/Y_test_pos_1000.npy")

print "Getting form data ..."
X_train_form = numpy.load("./data_1000/X_train_form_1000.npy")
Y_train_form = numpy.load("./data_1000/Y_train_form_1000.npy")
X_test_form = numpy.load("./data_1000/X_test_form_1000.npy")
Y_test_form = numpy.load("./data_1000/Y_test_form_1000.npy")

model = model_from_json(open('trained_model.json').read())
model.load_weights('trained_model_weights.h5')

model.compile(loss='categorical_crossentropy', 
        optimizer='adam', metrics=['accuracy'])

print "getting score on test..."
scores = model.evaluate([X_test_A, X_test_B, X_test_C, X_test_D, X_test_E, X_test_H,
X_test_I, X_test_J, X_test_K, X_test_L, X_test_M, X_test_N, X_test_O, X_test_P, X_test_Q, X_test_R, 
X_test_S, X_test_T, X_test_U, X_test_pos, X_test_form], Y_test_A)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
