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
    
    fann.close()
    return (A_test, B_test, C_test, D_test, E_test, H_test, I_test, J_test, 
            K_test, L_test, M_test, N_test, O_test, P_test, Q_test, R_test, S_test,
            T_test, U_test, form_test, pos_test)

def predict(fann_file, model_arch, model_weights):
    (A_test, B_test, C_test, D_test, E_test, H_test, I_test, J_test, 
            K_test, L_test, M_test, N_test, O_test, P_test, Q_test, 
            R_test, S_test, T_test, U_test, 
            form_test, pos_test) = fann2numpy(fann_file) 
    model = model_from_json(open(model_arch).read())
    model.load_weights(model_weights)
    
    model.compile(loss='categorical_crossentropy', 
            optimizer='adam', metrics=['accuracy'])

    prediction = model.predict_on_batch([A_test, B_test, C_test, D_test, E_test, 
    H_test, I_test, J_test, K_test, L_test, M_test, N_test, O_test, P_test, 
    Q_test, R_test, S_test, T_test, U_test, pos_test, form_test])
    
    prediction = model.predict_on_batch([A_test, B_test, C_test, D_test, E_test, 
    H_test, I_test, J_test, K_test, L_test, M_test, N_test, O_test, P_test, 
    Q_test, R_test, S_test, T_test, U_test, pos_test, form_test])
    #Transform prediction from one-hot to int
    mvt = 0
    for x in xrange(len(prediction[0])):
        if int(round(prediction[0][x])) == 1:
            mvt = x
            return mvt
    return mvt

if __name__ == "__main__":
    model_arch = sys.argv[3]
    model_weights = sys.argv[4]
    fann_file = sys.argv[1]
    mvt = predict(fann_file, model_arch, model_weights)
    output = open(sys.argv[2], "w")
    output.write(str(mvt))
    output.close()
