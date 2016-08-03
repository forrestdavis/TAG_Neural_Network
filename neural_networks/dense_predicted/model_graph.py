from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout, Merge
from keras.models import model_from_json
from keras.utils.visualize_util import plot

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
model = Sequential() 

model_A.add(Dense(50, input_dim = 100, init='uniform'))
model_A.add(Activation('relu'))
model_A.add(Dropout(0.50))
model_A.add(Dense(50))
model_A.add(Activation('relu'))
model_A.add(Dropout(0.50))

model_B.add(Dense(50, input_dim = 100, init='uniform'))
model_B.add(Activation('relu'))
model_B.add(Dropout(0.50))
model_B.add(Dense(50))
model_B.add(Activation('relu'))
model_B.add(Dropout(0.50))

model_C.add(Dense(50, input_dim = 100, init='uniform'))
model_C.add(Activation('relu'))
model_C.add(Dropout(0.50))
model_C.add(Dense(50))
model_C.add(Activation('relu'))
model_C.add(Dropout(0.50))

model_D.add(Dense(50, input_dim = 100, init='uniform'))
model_D.add(Activation('relu'))
model_D.add(Dropout(0.50))
model_D.add(Dense(50))
model_D.add(Activation('relu'))
model_D.add(Dropout(0.50))

model_E.add(Dense(50, input_dim = 100, init='uniform'))
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
model_H.add(Dense(50, input_dim = 100, init='uniform'))
model_H.add(Activation('relu'))
model_H.add(Dropout(0.50))
model_H.add(Dense(50))
model_H.add(Activation('relu'))
model_H.add(Dropout(0.50))

model_I.add(Dense(50, input_dim = 100, init='uniform'))
model_I.add(Activation('relu'))
model_I.add(Dropout(0.50))
model_I.add(Dense(50))
model_I.add(Activation('relu'))
model_I.add(Dropout(0.50))

model_J.add(Dense(50, input_dim = 100, init='uniform'))
model_J.add(Activation('relu'))
model_J.add(Dropout(0.50))
model_J.add(Dense(50))
model_J.add(Activation('relu'))
model_J.add(Dropout(0.50))

model_K.add(Dense(50, input_dim = 100, init='uniform'))
model_K.add(Activation('relu'))
model_K.add(Dropout(0.50))
model_K.add(Dense(50))
model_K.add(Activation('relu'))
model_K.add(Dropout(0.50))

model_L.add(Dense(50, input_dim = 100, init='uniform'))
model_L.add(Activation('relu'))
model_L.add(Dropout(0.50))
model_L.add(Dense(50))
model_L.add(Activation('relu'))
model_L.add(Dropout(0.50))

model_M.add(Dense(50, input_dim = 100, init='uniform'))
model_M.add(Activation('relu'))
model_M.add(Dropout(0.50))
model_M.add(Dense(50))
model_M.add(Activation('relu'))
model_M.add(Dropout(0.50))

model_N.add(Dense(50, input_dim = 100, init='uniform'))
model_N.add(Activation('relu'))
model_N.add(Dropout(0.50))
model_N.add(Dense(50))
model_N.add(Activation('relu'))
model_N.add(Dropout(0.50))

model_O.add(Dense(50, input_dim = 100, init='uniform'))
model_O.add(Activation('relu'))
model_O.add(Dropout(0.50))
model_O.add(Dense(50))
model_O.add(Activation('relu'))
model_O.add(Dropout(0.50))

model_P.add(Dense(50, input_dim = 100, init='uniform'))
model_P.add(Activation('relu'))
model_P.add(Dropout(0.50))
model_P.add(Dense(50))
model_P.add(Activation('relu'))
model_P.add(Dropout(0.50))

model_Q.add(Dense(50, input_dim = 100, init='uniform'))
model_Q.add(Activation('relu'))
model_Q.add(Dropout(0.50))
model_Q.add(Dense(50))
model_Q.add(Activation('relu'))
model_Q.add(Dropout(0.50))

model_R.add(Dense(50, input_dim = 100, init='uniform'))
model_R.add(Activation('relu'))
model_R.add(Dropout(0.50))
model_R.add(Dense(50))
model_R.add(Activation('relu'))
model_R.add(Dropout(0.50))

model_S.add(Dense(50, input_dim = 100, init='uniform'))
model_S.add(Activation('relu'))
model_S.add(Dropout(0.50))
model_S.add(Dense(50))
model_S.add(Activation('relu'))
model_S.add(Dropout(0.50))

model_T.add(Dense(50, input_dim = 100, init='uniform'))
model_T.add(Activation('relu'))
model_T.add(Dropout(0.50))
model_T.add(Dense(50))
model_T.add(Activation('relu'))
model_T.add(Dropout(0.50))

model_U.add(Dense(50, input_dim = 100, init='uniform'))
model_U.add(Activation('relu'))
model_U.add(Dropout(0.50))
model_U.add(Dense(50))
model_U.add(Activation('relu'))
model_U.add(Dropout(0.50))

model.add(Merge([model_A, model_B, model_C, model_D, model_E, model_H, model_I, model_J, model_K, model_L, 
model_M, model_N, model_O, model_P, model_Q, model_R, model_S, model_T, model_U], mode ='concat'))
model.add(Dense(17))
model.add(Activation('softmax'))

#Compile model
model.compile(loss='categorical_crossentropy', 
        optimizer='adam', metrics=['accuracy'])

plot(model, to_file='model.png', show_shapes=True)
