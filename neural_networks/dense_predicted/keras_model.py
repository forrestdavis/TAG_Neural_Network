from keras.models import Sequential, model_from_json
from keras.layers import Dense, Activation, Dropout, Merge
from keras.callbacks import EarlyStopping
import numpy
import sys
import dimensions as d

class KerasModel:
    def __init__(self, data_directory):
        self.model = Sequential()
        self.dim_file = data_directory + "/" + "io_dimensions_1000.txt"
        
    def train(self):
        #Get dimensions of data and check for errors
        dimensions_dictionary = d.get_dimensions(self.dim_file)
        d.error_check_dimensions(dimensions_dictionary)

        #Get train data
        (X_train_A, X_train_B, X_train_C, X_train_D, X_train_E, X_train_F, 
        X_train_G, X_train_H, X_train_I, X_train_J, X_train_K, X_train_L, 
        X_train_M, X_train_N, X_train_O, X_train_P, X_train_Q, X_train_R,
        X_train_S, X_train_T, X_train_U, 
                    #X_train_form, X_train_pos
        Y_train) = d.getTrainData("data_1000/numpy_arrays")
        self.model = d.createModel(dimensions_dictionary)
    
        early_stopping = EarlyStopping(monitor='val_loss', verbose = 1, patience=2)

        sys.stderr.write("fitting model...\n")
        self.model.fit([X_train_A, X_train_B, X_train_C, X_train_D, X_train_E,
            X_train_F, X_train_G, X_train_H, X_train_I, X_train_J, X_train_K, 
            X_train_L, X_train_M, X_train_N, X_train_O, X_train_P, X_train_Q, 
            X_train_R, X_train_S, X_train_T, X_train_U],
            Y_train, callbacks=[early_stopping], 
            nb_epoch=2, verbose=1, batch_size=1000, validation_split=0.1)
        
    def predict(self):
        sys.stderr.write("getting prediction from data...\n")
        (X_test_A, X_test_B, X_test_C, X_test_D, X_test_E, X_test_F, 
        X_test_G, X_test_H, X_test_I, X_test_J, X_test_K, X_test_L, 
        X_test_M, X_test_N, X_test_O, X_test_P, X_test_Q, X_test_R,
        X_test_S, X_test_T, X_test_U, 
                    #X_test_form, X_test_pos
        Y_test) = d.getTestData("data_1000/numpy_arrays")

        A_test = [X_test_A[0]]
        B_test = [X_test_B[0]]
        C_test = [X_test_C[0]]
        D_test = [X_test_D[0]]
        E_test = [X_test_E[0]]
        F_test = [X_test_F[0]]
        G_test = [X_test_G[0]]
        H_test = [X_test_H[0]]
        I_test = [X_test_I[0]]
        J_test = [X_test_J[0]]
        K_test = [X_test_K[0]]
        L_test = [X_test_L[0]]
        M_test = [X_test_M[0]]
        N_test = [X_test_N[0]]
        O_test = [X_test_O[0]]
        P_test = [X_test_P[0]]
        Q_test = [X_test_Q[0]]
        R_test = [X_test_R[0]]
        S_test = [X_test_S[0]]
        T_test = [X_test_T[0]]
        U_test = [X_test_U[0]]

        prediction = self.model.predict_on_batch([A_test, B_test, C_test, D_test, E_test, 
        F_test, G_test, H_test, I_test, J_test, K_test, L_test, M_test, N_test, O_test, P_test, 
        Q_test, R_test, S_test, T_test, U_test])

        #Transform prediction from one-hot to int
        max_pos = -1
        max_value = 0.0
        #Location with largest probability is 1 in one-hot encoding
        for i in xrange(len(prediction[0])):
            if max_value < float(prediction[0][i]):
                max_value = float(prediction[0][i])
                max_pos = i
        mvt = max_pos
        if mvt >= 0:
            return mvt
        else:
            return "ERROR"

    def save(self):
        sys.stderr.write("saving model...\n")
        model_json = self.model.to_json()
        with open("trained_model.json", "w") as json_file:
            json_file.write(model_json)
        self.model.save_weights("trained_model_weights.h5")

    def load(self):
        sys.stderr.write("loading model...\n")
        model_arch = "trained_model.json"
        model_weights = "trained_model_weights.h5"
        self.model = model_from_json(open(model_arch).read())
        self.model.load_weights(model_weights)
        self.model.compile(loss='categorical_crossentropy', 
                optimizer='adam', metrics=['accuracy'])

    def evaluate(self):
        sys.stderr.write("evaluating model on test data...\n")
        #Get test data
        (X_test_A, X_test_B, X_test_C, X_test_D, X_test_E, X_test_F, 
        X_test_G, X_test_H, X_test_I, X_test_J, X_test_K, X_test_L, 
        X_test_M, X_test_N, X_test_O, X_test_P, X_test_Q, X_test_R,
        X_test_S, X_test_T, X_test_U, 
                    #X_test_form, X_test_pos
        Y_test) = d.getTestData("data_1000/numpy_arrays")

        scores = self.model.evaluate([X_test_A, X_test_B, X_test_C, X_test_D,
            X_test_E, X_test_F, X_test_G, X_test_H, X_test_I, X_test_J,
            X_test_K, X_test_L, X_test_M, X_test_N, X_test_O, X_test_P, 
            X_test_Q, X_test_R, X_test_S, X_test_T, X_test_U], Y_test)
        print("%s: %.2f%%" % (self.model.metrics_names[1], scores[1]*100))

if __name__ == "__main__":
    model = KerasModel("data_1000")
    #model.train()
    #model.save()
    model.load()
    #model.evaluate()
    print model.predict()
