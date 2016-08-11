from keras.models import Sequential, model_from_json
from keras.layers import Dense, Activation, Dropout, Merge
from keras.callbacks import EarlyStopping
import numpy
import sys

def fann2numpy(fann_file):

    fann = open(fann_file, "r")

    count = 0
    nb_features = 21

    total_list = [[] for i in xrange(nb_features)]

    for line in fann:
        if count == nb_features:
            count = 0
        line = line.split()
        for element in line:
            if count == 0:
                total_list[count].append(float(element))
            else:
                total_list[count].append(int(element))
        count += 1

    form_test = numpy.array([total_list[0]], dtype=numpy.float)
    pos_test = numpy.array([total_list[1]], dtype=numpy.uint8)
    A_test = numpy.array([total_list[2]], dtype=numpy.uint8)
    B_test = numpy.array([total_list[3]], dtype=numpy.uint8)
    C_test = numpy.array([total_list[4]], dtype=numpy.uint8)
    D_test = numpy.array([total_list[5]], dtype=numpy.uint8)
    E_test = numpy.array([total_list[6]], dtype=numpy.uint8)
    H_test = numpy.array([total_list[7]], dtype=numpy.uint8)
    I_test = numpy.array([total_list[8]], dtype=numpy.uint8)
    J_test = numpy.array([total_list[9]], dtype=numpy.uint8)
    K_test = numpy.array([total_list[10]], dtype=numpy.uint8)
    L_test = numpy.array([total_list[11]], dtype=numpy.uint8)
    M_test = numpy.array([total_list[12]], dtype=numpy.uint8)
    N_test = numpy.array([total_list[13]], dtype=numpy.uint8)
    O_test = numpy.array([total_list[14]], dtype=numpy.uint8)
    P_test = numpy.array([total_list[15]], dtype=numpy.uint8)
    Q_test = numpy.array([total_list[16]], dtype=numpy.uint8)
    R_test = numpy.array([total_list[17]], dtype=numpy.uint8)
    S_test = numpy.array([total_list[18]], dtype=numpy.uint8)
    T_test = numpy.array([total_list[19]], dtype=numpy.uint8)
    U_test = numpy.array([total_list[20]], dtype=numpy.uint8)
    print A_test[0]
    
    fann.close()
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

    def predict(self, fann_file):
        (A_test, B_test, C_test, D_test, E_test, H_test, I_test, J_test, 
                K_test, L_test, M_test, N_test, O_test, P_test, Q_test, 
                R_test, S_test, T_test, U_test, 
                form_test, pos_test) = fann2numpy(fann_file) 

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

#if __name__ == "__main__":
    #model_arch = sys.argv[3]
    #model_weights = sys.argv[4]
    #fann_file = sys.argv[1]
    #fann_file_2 = sys.argv[5]
    #output_file = sys.argv[2]
    #mvt = predict(fann_file, model_arch, model_weights)
    #model = KerasModel()
    #model.createModel("trained_model.json", "trained_model_weights.h5")
    #print model.predict("fv.txt")
