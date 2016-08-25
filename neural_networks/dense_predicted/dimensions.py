import numpy
import sys
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout, Merge
#############################################################################
#Functions for getting and error checking dimensions from output file of INSERT GET DATA FUNCTION
#
#
#Forrest Davis
#August 11, 2016
#############################################################################

#Gets dimensions information from io file output of INSERT GET DATA
#Returns a dictionary of dictionaries where each element is formated:
# {X: {test or train: (input dimensions, output dimensions)} where X is
# a feature
def get_dimensions(dimensions_filename):

    dimensions_file = open(dimensions_filename, "r")
    d = {}

    for line in dimensions_file:
        line = line.strip('\n')
        line = line.split()
        feat = line[0]
        type_data = line[1]
        input_value_data = int(line[2])
        output_value_data = int(line[3])
        if feat not in d:
            d[feat] = {}
            d[feat][type_data] = (input_value_data, output_value_data)
        else:
            d[feat][type_data] = (input_value_data, output_value_data)
    dimensions_file.close()
    return d

#Ensures that data dimensions is same for test and train
def error_check_dimensions(dimensions_dictionary):
    d = dimensions_dictionary
    for key in d:
        input_values = [] 
        output_values = []
        for subkey in d[key]:
            input_values.append(d[key][subkey][0])
            output_values.append(d[key][subkey][1])
        assert input_values[0] == input_values[1], ( 
        "There is a mismatch in %s train and test data input dimensions" % key)
        assert output_values[0] == output_values[1], ( 
        "There is a mismatch in %s train and test data output dimensions" % key)

def getTrainData(data_directory):
    #Get train data
    sys.stderr.write("Getting A train data ...\n")
    X_train_A = numpy.load(data_directory + "/X_train_A.npy")
    #Only need to load one Y set of data because the movements
    #are the same for any feature 
    Y_train = numpy.load(data_directory + "/Y_train_A.npy")

    sys.stderr.write("Getting B train data ...\n")
    X_train_B = numpy.load(data_directory + "/X_train_B.npy")

    sys.stderr.write("Getting C train data ...\n")
    X_train_C = numpy.load(data_directory + "/X_train_C.npy")

    sys.stderr.write("Getting D train data ...\n")
    X_train_D = numpy.load(data_directory + "/X_train_D.npy")

    sys.stderr.write("Getting E train data ...\n")
    X_train_E = numpy.load(data_directory + "/X_train_E.npy")

    sys.stderr.write("Getting F train data ...\n")
    X_train_F = numpy.load(data_directory + "/X_train_F.npy")

    sys.stderr.write("Getting G train data ...\n")
    X_train_G = numpy.load(data_directory + "/X_train_G.npy")

    sys.stderr.write("Getting H train data ...\n")
    X_train_H = numpy.load(data_directory + "/X_train_H.npy")

    sys.stderr.write("Getting I train data ...\n")
    X_train_I = numpy.load(data_directory + "/X_train_I.npy")

    sys.stderr.write("Getting J train data ...\n")
    X_train_J = numpy.load(data_directory + "/X_train_J.npy")

    sys.stderr.write("Getting K train data ...\n")
    X_train_K = numpy.load(data_directory + "/X_train_K.npy")

    sys.stderr.write("Getting L train data ...\n")
    X_train_L = numpy.load(data_directory + "/X_train_L.npy")

    sys.stderr.write("Getting M train data ...\n")
    X_train_M = numpy.load(data_directory + "/X_train_M.npy")

    sys.stderr.write("Getting N train data ...\n")
    X_train_N = numpy.load(data_directory + "/X_train_N.npy")

    sys.stderr.write("Getting O train data ...\n")
    X_train_O = numpy.load(data_directory + "/X_train_O.npy")

    sys.stderr.write("Getting P train data ...\n")
    X_train_P = numpy.load(data_directory + "/X_train_P.npy")

    sys.stderr.write("Getting Q train data ...\n")
    X_train_Q = numpy.load(data_directory + "/X_train_Q.npy")

    sys.stderr.write("Getting R train data ...\n")
    X_train_R = numpy.load(data_directory + "/X_train_R.npy")

    sys.stderr.write("Getting S train data ...\n")
    X_train_S = numpy.load(data_directory + "/X_train_S.npy")

    sys.stderr.write("Getting T train data ...\n")
    X_train_T = numpy.load(data_directory + "/X_train_T.npy")

    sys.stderr.write("Getting U train data ...\n")
    X_train_U = numpy.load(data_directory + "/X_train_U.npy")

    '''
    sys.stderr.write("Getting pos train data ...\n")
    X_train_pos = numpy.load(data_directory + "/X_train_pos.npy")

    sys.stderr.write("Getting form train data ...\n")
    X_train_form = numpy.load(data_directory + "/X_train_form.npy")
    '''

    return [X_train_A, X_train_B, X_train_C, X_train_D, X_train_E, X_train_F, 
            X_train_G, X_train_H, X_train_I, X_train_J, X_train_K, X_train_L, 
            X_train_M, X_train_N, X_train_O, X_train_P, X_train_Q, X_train_R,
            X_train_S, X_train_T, X_train_U, 
            #X_train_form, X_train_pos
            Y_train]

def getTestData(data_directory):
    #Get test data
    sys.stderr.write("Getting A test data ...\n")
    X_test_A = numpy.load(data_directory + "/X_test_A.npy")

    #Only need to load one Y set of data because the movements
    #are the same for any feature 
    Y_test = numpy.load(data_directory + "/Y_test_A.npy")

    sys.stderr.write("Getting B test data ...\n")
    X_test_B = numpy.load(data_directory + "/X_test_B.npy")

    sys.stderr.write("Getting C test data ...\n")
    X_test_C = numpy.load(data_directory + "/X_test_C.npy")

    sys.stderr.write("Getting D test data ...\n")
    X_test_D = numpy.load(data_directory + "/X_test_D.npy")

    sys.stderr.write("Getting E test data ...\n")
    X_test_E = numpy.load(data_directory + "/X_test_E.npy")

    sys.stderr.write("Getting F test data ...\n")
    X_test_F = numpy.load(data_directory + "/X_test_F.npy")

    sys.stderr.write("Getting G test data ...\n")
    X_test_G = numpy.load(data_directory + "/X_test_G.npy")

    sys.stderr.write("Getting H test data ...\n")
    X_test_H = numpy.load(data_directory + "/X_test_H.npy")

    sys.stderr.write("Getting I test data ...\n")
    X_test_I = numpy.load(data_directory + "/X_test_I.npy")

    sys.stderr.write("Getting J test data ...\n")
    X_test_J = numpy.load(data_directory + "/X_test_J.npy")

    sys.stderr.write("Getting K test data ...\n")
    X_test_K = numpy.load(data_directory + "/X_test_K.npy")

    sys.stderr.write("Getting L test data ...\n")
    X_test_L = numpy.load(data_directory + "/X_test_L.npy")

    sys.stderr.write("Getting M test data ...\n")
    X_test_M = numpy.load(data_directory + "/X_test_M.npy")

    sys.stderr.write("Getting N test data ...\n")
    X_test_N = numpy.load(data_directory + "/X_test_N.npy")

    sys.stderr.write("Getting O test data ...\n")
    X_test_O = numpy.load(data_directory + "/X_test_O.npy")

    sys.stderr.write("Getting P test data ...\n")
    X_test_P = numpy.load(data_directory + "/X_test_P.npy")

    sys.stderr.write("Getting Q test data ...\n")
    X_test_Q = numpy.load(data_directory + "/X_test_Q.npy")

    sys.stderr.write("Getting R test data ...\n")
    X_test_R = numpy.load(data_directory + "/X_test_R.npy")

    sys.stderr.write("Getting S test data ...\n")
    X_test_S = numpy.load(data_directory + "/X_test_S.npy")

    sys.stderr.write("Getting T test data ...\n")
    X_test_T = numpy.load(data_directory + "/X_test_T.npy")

    sys.stderr.write("Getting U test data ...\n")
    X_test_U = numpy.load(data_directory + "/X_test_U.npy")

    '''
    sys.stderr.write("Getting pos test data ...\n")
    X_test_pos = numpy.load(data_directory + "/X_test_pos.npy")

    sys.stderr.write("Getting form test data ...\n")
    X_test_form = numpy.load(data_directory + "/X_test_form.npy")
    '''

    return [X_test_A, X_test_B, X_test_C, X_test_D, X_test_E, X_test_F, 
            X_test_G, X_test_H, X_test_I, X_test_J, X_test_K, X_test_L, 
            X_test_M, X_test_N, X_test_O, X_test_P, X_test_Q, X_test_R,
            X_test_S, X_test_T, X_test_U, 
            #X_test_form, X_test_pos
            Y_test]

def createModel(dimensions_dictionary):

    sys.stderr.write("creating model...\n")
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

    feat = 'A'
    model_A.add(Dense(50, input_dim = dimensions_dictionary[feat]['train'][0], init='uniform'))
    model_A.add(Activation('relu'))
    model_A.add(Dropout(0.50))
    model_A.add(Dense(50))
    model_A.add(Activation('relu'))
    model_A.add(Dropout(0.50))

    feat = 'B'
    model_B.add(Dense(50, input_dim = dimensions_dictionary[feat]['train'][0], init='uniform'))
    model_B.add(Activation('relu'))
    model_B.add(Dropout(0.50))
    model_B.add(Dense(50))
    model_B.add(Activation('relu'))
    model_B.add(Dropout(0.50))

    feat = 'C'
    model_C.add(Dense(50, input_dim = dimensions_dictionary[feat]['train'][0], init='uniform'))
    model_C.add(Activation('relu'))
    model_C.add(Dropout(0.50))
    model_C.add(Dense(50))
    model_C.add(Activation('relu'))
    model_C.add(Dropout(0.50))

    feat = 'D'
    model_D.add(Dense(50, input_dim = dimensions_dictionary[feat]['train'][0], init='uniform'))
    model_D.add(Activation('relu'))
    model_D.add(Dropout(0.50))
    model_D.add(Dense(50))
    model_D.add(Activation('relu'))
    model_D.add(Dropout(0.50))

    feat = 'E'
    model_E.add(Dense(50, input_dim = dimensions_dictionary[feat]['train'][0], init='uniform'))
    model_E.add(Activation('relu'))
    model_E.add(Dropout(0.50))
    model_E.add(Dense(50))
    model_E.add(Activation('relu'))
    model_E.add(Dropout(0.50))

    feat = 'F'
    model_F.add(Dense(50, input_dim = dimensions_dictionary[feat]['train'][0], init='uniform'))
    model_F.add(Activation('relu'))
    model_F.add(Dropout(0.50))
    model_F.add(Dense(50))
    model_F.add(Activation('relu'))
    model_F.add(Dropout(0.50))

    feat = 'G'
    model_G.add(Dense(50, input_dim = dimensions_dictionary[feat]['train'][0], init='uniform'))
    model_G.add(Activation('relu'))
    model_G.add(Dropout(0.50))
    model_G.add(Dense(50))
    model_G.add(Activation('relu'))
    model_G.add(Dropout(0.50))

    feat = 'H'
    model_H.add(Dense(50, input_dim = dimensions_dictionary[feat]['train'][0], init='uniform'))
    model_H.add(Activation('relu'))
    model_H.add(Dropout(0.50))
    model_H.add(Dense(50))
    model_H.add(Activation('relu'))
    model_H.add(Dropout(0.50))

    feat = 'I'
    model_I.add(Dense(50, input_dim = dimensions_dictionary[feat]['train'][0], init='uniform'))
    model_I.add(Activation('relu'))
    model_I.add(Dropout(0.50))
    model_I.add(Dense(50))
    model_I.add(Activation('relu'))
    model_I.add(Dropout(0.50))

    feat = 'J'
    model_J.add(Dense(50, input_dim = dimensions_dictionary[feat]['train'][0], init='uniform'))
    model_J.add(Activation('relu'))
    model_J.add(Dropout(0.50))
    model_J.add(Dense(50))
    model_J.add(Activation('relu'))
    model_J.add(Dropout(0.50))

    feat = 'K'
    model_K.add(Dense(50, input_dim = dimensions_dictionary[feat]['train'][0], init='uniform'))
    model_K.add(Activation('relu'))
    model_K.add(Dropout(0.50))
    model_K.add(Dense(50))
    model_K.add(Activation('relu'))
    model_K.add(Dropout(0.50))

    feat = 'L'
    model_L.add(Dense(50, input_dim = dimensions_dictionary[feat]['train'][0], init='uniform'))
    model_L.add(Activation('relu'))
    model_L.add(Dropout(0.50))
    model_L.add(Dense(50))
    model_L.add(Activation('relu'))
    model_L.add(Dropout(0.50))

    feat = 'M'
    model_M.add(Dense(50, input_dim = dimensions_dictionary[feat]['train'][0], init='uniform'))
    model_M.add(Activation('relu'))
    model_M.add(Dropout(0.50))
    model_M.add(Dense(50))
    model_M.add(Activation('relu'))
    model_M.add(Dropout(0.50))

    feat = 'N'
    model_N.add(Dense(50, input_dim = dimensions_dictionary[feat]['train'][0], init='uniform'))
    model_N.add(Activation('relu'))
    model_N.add(Dropout(0.50))
    model_N.add(Dense(50))
    model_N.add(Activation('relu'))
    model_N.add(Dropout(0.50))

    feat = 'O'
    model_O.add(Dense(50, input_dim = dimensions_dictionary[feat]['train'][0], init='uniform'))
    model_O.add(Activation('relu'))
    model_O.add(Dropout(0.50))
    model_O.add(Dense(50))
    model_O.add(Activation('relu'))
    model_O.add(Dropout(0.50))

    feat = 'P'
    model_P.add(Dense(50, input_dim = dimensions_dictionary[feat]['train'][0], init='uniform'))
    model_P.add(Activation('relu'))
    model_P.add(Dropout(0.50))
    model_P.add(Dense(50))
    model_P.add(Activation('relu'))
    model_P.add(Dropout(0.50))

    feat = 'Q'
    model_Q.add(Dense(50, input_dim = dimensions_dictionary[feat]['train'][0], init='uniform'))
    model_Q.add(Activation('relu'))
    model_Q.add(Dropout(0.50))
    model_Q.add(Dense(50))
    model_Q.add(Activation('relu'))
    model_Q.add(Dropout(0.50))

    feat = 'R'
    model_R.add(Dense(50, input_dim = dimensions_dictionary[feat]['train'][0], init='uniform'))
    model_R.add(Activation('relu'))
    model_R.add(Dropout(0.50))
    model_R.add(Dense(50))
    model_R.add(Activation('relu'))
    model_R.add(Dropout(0.50))

    feat = 'S'
    model_S.add(Dense(50, input_dim = dimensions_dictionary[feat]['train'][0], init='uniform'))
    model_S.add(Activation('relu'))
    model_S.add(Dropout(0.50))
    model_S.add(Dense(50))
    model_S.add(Activation('relu'))
    model_S.add(Dropout(0.50))

    feat = 'T'
    model_T.add(Dense(50, input_dim = dimensions_dictionary[feat]['train'][0], init='uniform'))
    model_T.add(Activation('relu'))
    model_T.add(Dropout(0.50))
    model_T.add(Dense(50))
    model_T.add(Activation('relu'))
    model_T.add(Dropout(0.50))

    feat = 'U'
    model_U.add(Dense(50, input_dim = dimensions_dictionary[feat]['train'][0], init='uniform'))
    model_U.add(Activation('relu'))
    model_U.add(Dropout(0.50))
    model_U.add(Dense(50))
    model_U.add(Activation('relu'))
    model_U.add(Dropout(0.50))

    feat = 'A'
    model.add(Merge([model_A, model_B, model_C, model_D, model_E, model_F, model_G, model_H, model_I, model_J, model_K, model_L, 
    model_M, model_N, model_O, model_P, model_Q, model_R, model_S, model_T, model_U], mode ='concat'))
    model.add(Dense(dimensions_dictionary[feat]['train'][1]))
    model.add(Activation('softmax'))
    
    #Compile model
    model.compile(loss='categorical_crossentropy', 
            optimizer='adam', metrics=['accuracy'])

    return model
