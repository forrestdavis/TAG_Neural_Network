from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout, Merge
from keras.callbacks import EarlyStopping
import model_dimensions as md
import numpy
import sys

dimensions_dictionary = md.get_dimensions("data/io_dimensions.txt")
md.error_check_dimensions(dimensions_dictionary)

#Get train data
print "Getting A data ..."
X_train_A = numpy.load("X_train_A.npy")
Y_train_A = numpy.load("Y_train_A.npy")
X_test_A = numpy.load("X_test_A.npy")
Y_test_A = numpy.load("Y_test_A.npy")

print "Getting B data ..."
X_train_B = numpy.load("X_train_B.npy")
Y_train_B = numpy.load("Y_train_B.npy")
X_test_B = numpy.load("X_test_B.npy")
Y_test_B = numpy.load("Y_test_B.npy")

print "Getting C data ..."
X_train_C = numpy.load("X_train_C.npy")
Y_train_C = numpy.load("Y_train_C.npy")
X_test_C = numpy.load("X_test_C.npy")
Y_test_C = numpy.load("Y_test_C.npy")

print "Getting D data ..."
X_train_D = numpy.load("X_train_D.npy")
Y_train_D = numpy.load("Y_train_D.npy")
X_test_D = numpy.load("X_test_D.npy")
Y_test_D = numpy.load("Y_test_D.npy")

print "Getting E data ..."
X_train_E = numpy.load("X_train_E.npy")
Y_train_E = numpy.load("Y_train_E.npy")
X_test_E = numpy.load("X_test_E.npy")
Y_test_E = numpy.load("Y_test_E.npy")

'''
print "Getting F data ..."
X_train_F = numpy.load("X_train_F.npy")
Y_train_F = numpy.load("Y_train_F.npy")
X_test_F = numpy.load("X_test_F.npy")
Y_test_F = numpy.load("Y_test_F.npy")

print "Getting G data ..."
X_train_G = numpy.load("X_train_G.npy")
Y_train_G = numpy.load("Y_train_G.npy")
X_test_G = numpy.load("X_test_G.npy")
Y_test_G = numpy.load("Y_test_G.npy")
'''

print "Getting H data ..."
X_train_H = numpy.load("X_train_H.npy")
Y_train_H = numpy.load("Y_train_H.npy")
X_test_H = numpy.load("X_test_H.npy")
Y_test_H = numpy.load("Y_test_H.npy")

print "Getting I data ..."
X_train_I = numpy.load("X_train_I.npy")
Y_train_I = numpy.load("Y_train_I.npy")
X_test_I = numpy.load("X_test_I.npy")
Y_test_I = numpy.load("Y_test_I.npy")

print "Getting J data ..."
X_train_J = numpy.load("X_train_J.npy")
Y_train_J = numpy.load("Y_train_J.npy")
X_test_J = numpy.load("X_test_J.npy")
Y_test_J = numpy.load("Y_test_J.npy")

print "Getting K data ..."
X_train_K = numpy.load("X_train_K.npy")
Y_train_K = numpy.load("Y_train_K.npy")
X_test_K = numpy.load("X_test_K.npy")
Y_test_K = numpy.load("Y_test_K.npy")

print "Getting L data ..."
X_train_L = numpy.load("X_train_L.npy")
Y_train_L = numpy.load("Y_train_L.npy")
X_test_L = numpy.load("X_test_L.npy")
Y_test_L = numpy.load("Y_test_L.npy")

print "Getting M data ..."
X_train_M = numpy.load("X_train_M.npy")
Y_train_M = numpy.load("Y_train_M.npy")
X_test_M = numpy.load("X_test_M.npy")
Y_test_M = numpy.load("Y_test_M.npy")

print "Getting N data ..."
X_train_N = numpy.load("X_train_N.npy")
Y_train_N = numpy.load("Y_train_N.npy")
X_test_N = numpy.load("X_test_N.npy")
Y_test_N = numpy.load("Y_test_N.npy")

print "Getting O data ..."
X_train_O = numpy.load("X_train_O.npy")
Y_train_O = numpy.load("Y_train_O.npy")
X_test_O = numpy.load("X_test_O.npy")
Y_test_O = numpy.load("Y_test_O.npy")

print "Getting P data ..."
X_train_P = numpy.load("X_train_P.npy")
Y_train_P = numpy.load("Y_train_P.npy")
X_test_P = numpy.load("X_test_P.npy")
Y_test_P = numpy.load("Y_test_P.npy")

print "Getting Q data ..."
X_train_Q = numpy.load("X_train_Q.npy")
Y_train_Q = numpy.load("Y_train_Q.npy")
X_test_Q = numpy.load("X_test_Q.npy")
Y_test_Q = numpy.load("Y_test_Q.npy")

print "Getting R data ..."
X_train_R = numpy.load("X_train_R.npy")
Y_train_R = numpy.load("Y_train_R.npy")
X_test_R = numpy.load("X_test_R.npy")
Y_test_R = numpy.load("Y_test_R.npy")

print "Getting S data ..."
X_train_S = numpy.load("X_train_S.npy")
Y_train_S = numpy.load("Y_train_S.npy")
X_test_S = numpy.load("X_test_S.npy")
Y_test_S = numpy.load("Y_test_S.npy")

print "Getting T data ..."
X_train_T = numpy.load("X_train_T.npy")
Y_train_T = numpy.load("Y_train_T.npy")
X_test_T = numpy.load("X_test_T.npy")
Y_test_T = numpy.load("Y_test_T.npy")

print "Getting U data ..."
X_train_U = numpy.load("X_train_U.npy")
Y_train_U = numpy.load("Y_train_U.npy")
X_test_U = numpy.load("X_test_U.npy")
Y_test_U = numpy.load("Y_test_U.npy")

print "Getting pos data ..."
X_train_U = numpy.load("X_train_pos.npy")
Y_train_U = numpy.load("Y_train_pos.npy")
X_test_U = numpy.load("X_test_pos.npy")
Y_test_U = numpy.load("Y_test_pos.npy")

print "Getting form data ..."
X_train_U = numpy.load("X_train_form.npy")
Y_train_U = numpy.load("Y_train_form.npy")
X_test_U = numpy.load("X_test_form.npy")
Y_test_U = numpy.load("Y_test_form.npy")

#Create model
print "creating model ..."
model_A = Sequential()
model_B = Sequential()
model_C = Sequential()
model_D = Sequential()
model_E = Sequential()
#model_F = Sequential()
#model_G = Sequential()
model_H = Sequential()
model_I = Sequential()
model_J = Sequential()
model_K = Sequential()
model_L = Sequential()
model_M = Sequential()
model_N = Sequential()
model_O = Sequential()
model_P = Sequential()
model_Q = Sequential()
model_R = Sequential()
model_S = Sequential()
model_T = Sequential()
model_U = Sequential()
model_pos = Sequential()
model_form = Sequential()
model = Sequential() 

model_A.add(Dense(50, input_dim = A_train_input_dim, init='uniform'))
model_A.add(Activation('relu'))
model_A.add(Dropout(0.50))
model_A.add(Dense(50))
model_A.add(Activation('relu'))
model_A.add(Dropout(0.50))
model_A.add(Dense(A_train_output_dim))
model_A.add(Activation('softmax'))

model_B.add(Dense(50, input_dim = B_train_input_dim, init='uniform'))
model_B.add(Activation('relu'))
model_B.add(Dropout(0.50))
model_B.add(Dense(50))
model_B.add(Activation('relu'))
model_B.add(Dropout(0.50))

model_C.add(Dense(50, input_dim = C_train_input_dim, init='uniform'))
model_C.add(Activation('relu'))
model_C.add(Dropout(0.50))
model_C.add(Dense(50))
model_C.add(Activation('relu'))
model_C.add(Dropout(0.50))

model_D.add(Dense(50, input_dim = D_train_input_dim, init='uniform'))
model_D.add(Activation('relu'))
model_D.add(Dropout(0.50))
model_D.add(Dense(50))
model_D.add(Activation('relu'))
model_D.add(Dropout(0.50))

model_E.add(Dense(50, input_dim = E_train_input_dim, init='uniform'))
model_E.add(Activation('relu'))
model_E.add(Dropout(0.50))
model_E.add(Dense(50))
model_E.add(Activation('relu'))
model_E.add(Dropout(0.50))

'''
model_F.add(Dense(50, input_dim = F_train_input_dim, init='uniform'))
model_F.add(Activation('relu'))
model_F.add(Dropout(0.50))
model_F.add(Dense(50))
model_F.add(Activation('relu'))
model_F.add(Dropout(0.50))

model_G.add(Dense(50, input_dim = G_train_input_dim, init='uniform'))
model_G.add(Activation('relu'))
model_G.add(Dropout(0.50))
model_G.add(Dense(50))
model_G.add(Activation('relu'))
model_G.add(Dropout(0.50))

'''
model_H.add(Dense(50, input_dim = H_train_input_dim, init='uniform'))
model_H.add(Activation('relu'))
model_H.add(Dropout(0.50))
model_H.add(Dense(50))
model_H.add(Activation('relu'))
model_H.add(Dropout(0.50))

model_I.add(Dense(50, input_dim = I_train_input_dim, init='uniform'))
model_I.add(Activation('relu'))
model_I.add(Dropout(0.50))
model_I.add(Dense(50))
model_I.add(Activation('relu'))
model_I.add(Dropout(0.50))

model_J.add(Dense(50, input_dim = J_train_input_dim, init='uniform'))
model_J.add(Activation('relu'))
model_J.add(Dropout(0.50))
model_J.add(Dense(50))
model_J.add(Activation('relu'))
model_J.add(Dropout(0.50))

model_K.add(Dense(50, input_dim = K_train_input_dim, init='uniform'))
model_K.add(Activation('relu'))
model_K.add(Dropout(0.50))
model_K.add(Dense(50))
model_K.add(Activation('relu'))
model_K.add(Dropout(0.50))

model_L.add(Dense(50, input_dim = L_train_input_dim, init='uniform'))
model_L.add(Activation('relu'))
model_L.add(Dropout(0.50))
model_L.add(Dense(50))
model_L.add(Activation('relu'))
model_L.add(Dropout(0.50))

model_M.add(Dense(50, input_dim = M_train_input_dim, init='uniform'))
model_M.add(Activation('relu'))
model_M.add(Dropout(0.50))
model_M.add(Dense(50))
model_M.add(Activation('relu'))
model_M.add(Dropout(0.50))

model_N.add(Dense(50, input_dim = N_train_input_dim, init='uniform'))
model_N.add(Activation('relu'))
model_N.add(Dropout(0.50))
model_N.add(Dense(50))
model_N.add(Activation('relu'))
model_N.add(Dropout(0.50))

model_O.add(Dense(50, input_dim = O_train_input_dim, init='uniform'))
model_O.add(Activation('relu'))
model_O.add(Dropout(0.50))
model_O.add(Dense(50))
model_O.add(Activation('relu'))
model_O.add(Dropout(0.50))

model_P.add(Dense(50, input_dim = P_train_input_dim, init='uniform'))
model_P.add(Activation('relu'))
model_P.add(Dropout(0.50))
model_P.add(Dense(50))
model_P.add(Activation('relu'))
model_P.add(Dropout(0.50))

model_Q.add(Dense(50, input_dim = Q_train_input_dim, init='uniform'))
model_Q.add(Activation('relu'))
model_Q.add(Dropout(0.50))
model_Q.add(Dense(50))
model_Q.add(Activation('relu'))
model_Q.add(Dropout(0.50))

model_R.add(Dense(50, input_dim = R_train_input_dim, init='uniform'))
model_R.add(Activation('relu'))
model_R.add(Dropout(0.50))
model_R.add(Dense(50))
model_R.add(Activation('relu'))
model_R.add(Dropout(0.50))

model_S.add(Dense(50, input_dim = S_train_input_dim, init='uniform'))
model_S.add(Activation('relu'))
model_S.add(Dropout(0.50))
model_S.add(Dense(50))
model_S.add(Activation('relu'))
model_S.add(Dropout(0.50))

model_T.add(Dense(50, input_dim = T_train_input_dim, init='uniform'))
model_T.add(Activation('relu'))
model_T.add(Dropout(0.50))
model_T.add(Dense(50))
model_T.add(Activation('relu'))
model_T.add(Dropout(0.50))

model_U.add(Dense(50, input_dim = U_train_input_dim, init='uniform'))
model_U.add(Activation('relu'))
model_U.add(Dropout(0.50))
model_U.add(Dense(50))
model_U.add(Activation('relu'))
model_U.add(Dropout(0.50))

model_pos.add(Dense(50, input_dim = pos_train_input_dim, init='uniform'))
model_pos.add(Activation('relu'))
model_pos.add(Dropout(0.50))
model_pos.add(Dense(50))
model_pos.add(Activation('relu'))
model_pos.add(Dropout(0.50))

model_form.add(Dense(50, input_dim = form_train_input_dim, init='uniform'))
model_form.add(Activation('relu'))
model_form.add(Dropout(0.50))
model_form.add(Dense(50))
model_form.add(Activation('relu'))
model_form.add(Dropout(0.50))

model.add(Merge([model_A, model_B, model_C, model_D, model_E, model_H, model_I, model_J, model_K, model_L, 
model_M, model_N, model_O, model_P, model_Q, model_R, model_S, model_T, model_U, model_pos], mode ='concat'))
model.add(Dense(A_train_output_dim))
model.add(Activation('softmax'))

#Compile model
model.compile(loss='categorical_crossentropy', 
        optimizer='adam', metrics=['accuracy'])

#Define early stopping 
early_stopping = EarlyStopping(monitor='val_loss', verbose = 1, patience=2)

print "fitting model..."
model.fit([X_train_A, X_train_B, X_train_C, X_train_D, X_train_E, X_train_H, X_train_I, X_train_J, 
X_train_K, X_train_L, X_train_M, X_train_N, X_train_O, X_train_P, X_train_Q, X_train_R, X_train_S, X_train_T, X_train_U, X_train_pos], 
Y_train_A, callbacks=[early_stopping], nb_epoch=50, verbose=1, batch_size=1000, 
         validation_split=0.1)

#Get accurracy on test data
print "getting score on test..."
scores = model.evaluate([X_test_A, X_test_B, X_test_C, X_test_D, X_test_E, X_test_H,
X_test_I, X_test_J, X_test_K, X_test_L, X_test_M, X_test_N, X_test_O, X_test_P, X_test_Q, X_test_R, 
X_test_S, X_test_T, X_test_U, X_test_pos], Y_test_A)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
