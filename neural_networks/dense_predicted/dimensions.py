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
    model_total = Sequential()

    feats = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
            'U']
    models = []

    for feat in feats:
        model = Sequential()
        model.add(Dense(50, input_dim=dimensions_dictionary[feat]['train'][0], init='uniform'))
        model.add(Activation('relu'))
        model.add(Dropout(0.50))
        model.add(Dense(50))
        model.add(Activation('relu'))
        model.add(Dropout(0.50))
        models.append(model)

    feat = 'A'
    model_total.add(Merge(models, mode='concat'))
    model_total.add(Dense(dimensions_dictionary[feat]['train'][1]))
    model_total.add(Activation('softmax'))
    
    #Compile model
    model_total.compile(loss='categorical_crossentropy', 
            optimizer='adam', metrics=['accuracy'])

    return model_total
