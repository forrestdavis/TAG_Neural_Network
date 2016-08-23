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
(X_test_A, X_test_B, X_test_C, X_test_D, X_test_E, X_test_F, 
X_test_G, X_test_H, X_test_I, X_test_J, X_test_K, X_test_L, 
X_test_M, X_test_N, X_test_O, X_test_P, X_test_Q, X_test_R,
X_test_S, X_test_T, X_test_U, 
            #X_test_form, X_test_pos
Y_test) = d.getTestData("data_1000/numpy_arrays")

model = d.createModel(dimensions_dictionary)
#Create model
'''
print "creating model ..."
model_A = Sequential()
model_B = Sequential()
model_C = Sequential()
model_D = Sequential()
model_E = Sequential()
model_F = Sequential()
model_G = Sequential()
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
#model_pos = Sequential()
#model_form = Sequential()
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

model.add(Merge([model_A, model_B, model_C, model_D, model_E, model_F, model_G, model_H, model_I, model_J, model_K, model_L, 
model_M, model_N, model_O, model_P, model_Q, model_R, model_S, model_T, model_U], mode ='concat'))
model.add(Dense(A_train_output_dim))
model.add(Activation('softmax'))

#Compile model
model.compile(loss='categorical_crossentropy', 
        optimizer='adam', metrics=['accuracy'])

#Define early stopping 
early_stopping = EarlyStopping(monitor='val_loss', verbose = 1, patience=2)

print "fitting model..."
model.fit([X_train_A, X_train_B, X_train_C, X_train_D, X_train_E, X_train_F, X_train_G, X_train_H, X_train_I, X_train_J, 
X_train_K, X_train_L, X_train_M, X_train_N, X_train_O, X_train_P, X_train_Q, X_train_R, X_train_S, X_train_T, X_train_U], 
Y_train, callbacks=[early_stopping], nb_epoch=50, verbose=1, batch_size=1000, 
         validation_split=0.1)

#Get accurracy on test data
print "getting score on test..."
scores = model.evaluate([X_test_A, X_test_B, X_test_C, X_test_D, X_test_E, X_train_F, X_train_G, X_test_H,
X_test_I, X_test_J, X_test_K, X_test_L, X_test_M, X_test_N, X_test_O, X_test_P, X_test_Q, X_test_R, 
X_test_S, X_test_T, X_test_U], Y_test)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
'''
