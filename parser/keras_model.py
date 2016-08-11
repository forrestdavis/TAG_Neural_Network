from keras.models import Sequential, model_from_json
from keras.layers import Dense, Activation, Dropout, Merge
from keras.callbacks import EarlyStopping
import numpy
import sys

def fann2numpy(fm_file, fann_file):
    fann = open(fann_file, "r")
    fm = open(fm_file, "r")
    dictionary = {}

    for feature in fm:
        feature = feature.strip('\n')
        if feature[0] == "#":
            pass
        else:
            fv = fann.readline().strip('\n')
            dim = feature[2:]
            if dim not in dictionary:
                if dim == "f":
                    dictionary[dim] = {}
                    dictionary[dim][feature] = map(float, fv.split())
                else:
                    dictionary[dim] = {}
                    dictionary[dim][feature] = map(int, fv.split())
            else:
                if dim == "f":
                    fv = map(float, fv.split())
                    dictionary[dim][feature] = fv
                else:
                    fv = map(int, fv.split())
                    dictionary[dim][feature] = fv

    for key in dictionary:
        s0=s1=s2=s3=b0=b1=b2=b3 = []
        for subkey in dictionary[key]:
            if "s0" in subkey:
                s0=dictionary[key][subkey]
            if "s1" in subkey:
                s1=dictionary[key][subkey]
            if "s2" in subkey:
                s2=dictionary[key][subkey]
            if "s3" in subkey:
                s3=dictionary[key][subkey]
            if "b0" in subkey:
                b0=dictionary[key][subkey]
            if "b1" in subkey:
                b1=dictionary[key][subkey]
            if "b2" in subkey:
                b2=dictionary[key][subkey]
            if "b3" in subkey:
                b3=dictionary[key][subkey]

        #Ensure test data has same parameters as model
        assert len(s0) != 0, "s0% was not found" % key
        assert len(s1) != 0, "s1% was not found" % key
        assert len(s2) != 0, "s2% was not found" % key
        assert len(s3) != 0, "s3% was not found" % key
        assert len(b0) != 0, "b0% was not found" % key
        assert len(b1) != 0, "b1% was not found" % key
        assert len(b2) != 0, "b2% was not found" % key
        assert len(b3) != 0, "b3% was not found" % key

        s0 += s1+s2+s3+b0+b1+b2+b3
        if key == "A":
            A_test = numpy.array([s0], dtype=numpy.uint8)
        if key == "B":
            B_test = numpy.array([s0], dtype=numpy.uint8)
        if key == "C":
            C_test = numpy.array([s0], dtype=numpy.uint8)
        if key == "D":
            D_test = numpy.array([s0], dtype=numpy.uint8)
        if key == "E":
            E_test = numpy.array([s0], dtype=numpy.uint8)
        if key == "H":
            H_test = numpy.array([s0], dtype=numpy.uint8)
        if key == "I":
            I_test = numpy.array([s0], dtype=numpy.uint8)
        if key == "J":
            J_test = numpy.array([s0], dtype=numpy.uint8)
        if key == "K":
            K_test = numpy.array([s0], dtype=numpy.uint8)
        if key == "L":
            L_test = numpy.array([s0], dtype=numpy.uint8)
        if key == "M":
            M_test = numpy.array([s0], dtype=numpy.uint8)
        if key == "N":
            N_test = numpy.array([s0], dtype=numpy.uint8)
        if key == "O":
            O_test = numpy.array([s0], dtype=numpy.uint8)
        if key == "P":
            P_test = numpy.array([s0], dtype=numpy.uint8)
        if key == "Q":
            Q_test = numpy.array([s0], dtype=numpy.uint8)
        if key == "R":
            R_test = numpy.array([s0], dtype=numpy.uint8)
        if key == "S":
            S_test = numpy.array([s0], dtype=numpy.uint8)
        if key == "T":
            T_test = numpy.array([s0], dtype=numpy.uint8)
        if key == "U":
            U_test = numpy.array([s0], dtype=numpy.uint8)
        if key == "f":
            form_test = numpy.array([s0], dtype=numpy.uint8)
        if key == "p":
            pos_test = numpy.array([s0], dtype=numpy.uint8)
    fann.close()
    fm.close()
    return (A_test, B_test, C_test, D_test, E_test, H_test, I_test, J_test, 
            K_test, L_test, M_test, N_test, O_test, P_test, Q_test, R_test, S_test,
            T_test, U_test, form_test, pos_test)

def createModel(model_arch, model_weights):
    model = model_from_json(open(model_arch).read())
    model.load_weights(model_weights)
    model.compile(loss='categorical_crossentropy', 
            optimizer='adam', metrics=['accuracy'])
    return model

class KerasModel:
    def __init__(self, model_arch, model_weights):
        self.model = createModel(model_arch, model_weights)

    def predict(self, fm_file, fann_file):
        (A_test, B_test, C_test, D_test, E_test, H_test, I_test, J_test, 
                K_test, L_test, M_test, N_test, O_test, P_test, Q_test, 
                R_test, S_test, T_test, U_test, 
                form_test, pos_test) = fann2numpy(fm_file, fann_file) 

        prediction = self.model.predict_on_batch([A_test, B_test, C_test, D_test, E_test, 
        H_test, I_test, J_test, K_test, L_test, M_test, N_test, O_test, P_test, 
        Q_test, R_test, S_test, T_test, U_test, pos_test, form_test])

        #Transform prediction from one-hot to int
        max_pos = -1
        max_value = 0.0
        for i in xrange(len(prediction[0])):
            if max_value < float(prediction[0][i]):
                max_value = float(prediction[0][i])
                max_pos = i
        mvt = max_pos
        if mvt >= 0:
            return mvt
        else:
            return "ERROR"
