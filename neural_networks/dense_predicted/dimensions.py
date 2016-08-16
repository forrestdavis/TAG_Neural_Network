import numpy
import sys
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

def getData(data_directory):
    #Get train data
    sys.stderr.write("Getting A data ...")
    X_train_A = numpy.load("./data/X_train_A.npy")
    Y_train_A = numpy.load("./data/Y_train_A.npy")
    X_test_A = numpy.load("./data/X_test_A.npy")
    Y_test_A = numpy.load("./data/Y_test_A.npy")

    sys.stderr.write("Getting B data ...")
    X_train_B = numpy.load("./data/X_train_B.npy")
    Y_train_B = numpy.load("./data/Y_train_B.npy")
    X_test_B = numpy.load("./data/X_test_B.npy")
    Y_test_B = numpy.load("./data/Y_test_B.npy")

    sys.stderr.write("Getting C data ...")
    X_train_C = numpy.load("./data/X_train_C.npy")
    Y_train_C = numpy.load("./data/Y_train_C.npy")
    X_test_C = numpy.load("./data/X_test_C.npy")
    Y_test_C = numpy.load("./data/Y_test_C.npy")

    sys.stderr.write("Getting D data ...")
    X_train_D = numpy.load("./data/X_train_D.npy")
    Y_train_D = numpy.load("./data/Y_train_D.npy")
    X_test_D = numpy.load("./data/X_test_D.npy")
    Y_test_D = numpy.load("./data/Y_test_D.npy")

    sys.stderr.write("Getting E data ...")
    X_train_E = numpy.load("./data/X_train_E.npy")
    Y_train_E = numpy.load("./data/Y_train_E.npy")
    X_test_E = numpy.load("./data/X_test_E.npy")
    Y_test_E = numpy.load("./data/Y_test_E.npy")

    sys.stderr.write("Getting F data ...")
    X_train_F = numpy.load("./data/X_train_F.npy")
    Y_train_F = numpy.load("./data/Y_train_F.npy")
    X_test_F = numpy.load("./data/X_test_F.npy")
    Y_test_F = numpy.load("./data/Y_test_F.npy")

    sys.stderr.write("Getting G data ...")
    X_train_G = numpy.load("./data/X_train_G.npy")
    Y_train_G = numpy.load("./data/Y_train_G.npy")
    X_test_G = numpy.load("./data/X_test_G.npy")
    Y_test_G = numpy.load("./data/Y_test_G.npy")

    sys.stderr.write("Getting H data ..."
    X_train_H = numpy.load("./data/X_train_H.npy")
    Y_train_H = numpy.load("./data/Y_train_H.npy")
    X_test_H = numpy.load("./data/X_test_H.npy")
    Y_test_H = numpy.load("./data/Y_test_H.npy")

    sys.stderr.write("Getting I data ...")
    X_train_I = numpy.load("./data/X_train_I.npy")
    Y_train_I = numpy.load("./data/Y_train_I.npy")
    X_test_I = numpy.load("./data/X_test_I.npy")
    Y_test_I = numpy.load("./data/Y_test_I.npy")

    sys.stderr.write("Getting J data ...")
    X_train_J = numpy.load("./data/X_train_J.npy")
    Y_train_J = numpy.load("./data/Y_train_J.npy")
    X_test_J = numpy.load("./data/X_test_J.npy")
    Y_test_J = numpy.load("./data/Y_test_J.npy")

    sys.stderr.write("Getting K data ...")
    X_train_K = numpy.load("./data/X_train_K.npy")
    Y_train_K = numpy.load("./data/Y_train_K.npy")
    X_test_K = numpy.load("./data/X_test_K.npy")
    Y_test_K = numpy.load("./data/Y_test_K.npy")

    sys.stderr.write("Getting L data ...")
    X_train_L = numpy.load("./data/X_train_L.npy")
    Y_train_L = numpy.load("./data/Y_train_L.npy")
    X_test_L = numpy.load("./data/X_test_L.npy")
    Y_test_L = numpy.load("./data/Y_test_L.npy")

    sys.stderr.write("Getting M data ...")
    X_train_M = numpy.load("./data/X_train_M.npy")
    Y_train_M = numpy.load("./data/Y_train_M.npy")
    X_test_M = numpy.load("./data/X_test_M.npy")
    Y_test_M = numpy.load("./data/Y_test_M.npy")

    sys.stderr.write("Getting N data ...")
    X_train_N = numpy.load("./data/X_train_N.npy")
    Y_train_N = numpy.load("./data/Y_train_N.npy")
    X_test_N = numpy.load("./data/X_test_N.npy")
    Y_test_N = numpy.load("./data/Y_test_N.npy")

    sys.stderr.write("Getting O data ...")
    X_train_O = numpy.load("./data/X_train_O.npy")
    Y_train_O = numpy.load("./data/Y_train_O.npy")
    X_test_O = numpy.load("./data/X_test_O.npy")
    Y_test_O = numpy.load("./data/Y_test_O.npy")

    sys.stderr.write("Getting P data ...")
    X_train_P = numpy.load("./data/X_train_P.npy")
    Y_train_P = numpy.load("./data/Y_train_P.npy")
    X_test_P = numpy.load("./data/X_test_P.npy")
    Y_test_P = numpy.load("./data/Y_test_P.npy")

    sys.stderr.write("Getting Q data ...")
    X_train_Q = numpy.load("./data/X_train_Q.npy")
    Y_train_Q = numpy.load("./data/Y_train_Q.npy")
    X_test_Q = numpy.load("./data/X_test_Q.npy")
    Y_test_Q = numpy.load("./data/Y_test_Q.npy")

    sys.stderr.write("Getting R data ...")
    X_train_R = numpy.load("./data/X_train_R.npy")
    Y_train_R = numpy.load("./data/Y_train_R.npy")
    X_test_R = numpy.load("./data/X_test_R.npy")
    Y_test_R = numpy.load("./data/Y_test_R.npy")

    sys.stderr.write("Getting S data ...")
    X_train_S = numpy.load("./data/X_train_S.npy")
    Y_train_S = numpy.load("./data/Y_train_S.npy")
    X_test_S = numpy.load("./data/X_test_S.npy")
    Y_test_S = numpy.load("./data/Y_test_S.npy")

    sys.stderr.write("Getting T data ...")
    X_train_T = numpy.load("./data/X_train_T.npy")
    Y_train_T = numpy.load("./data/Y_train_T.npy")
    X_test_T = numpy.load("./data/X_test_T.npy")
    Y_test_T = numpy.load("./data/Y_test_T.npy")

    sys.stderr.write("Getting U data ...")
    X_train_U = numpy.load("./data/X_train_U.npy")
    Y_train_U = numpy.load("./data/Y_train_U.npy")
    X_test_U = numpy.load("./data/X_test_U.npy")
    Y_test_U = numpy.load("./data/Y_test_U.npy")

    sys.stderr.write("Getting pos data ...")
    X_train_pos = numpy.load("./data/X_train_pos.npy")
    Y_train_pos = numpy.load("./data/Y_train_pos.npy")
    X_test_pos = numpy.load("./data/X_test_pos.npy")
    Y_test_pos = numpy.load("./data/Y_test_pos.npy")

    sys.stderr.write("Getting form data ...")
    X_train_form = numpy.load("./data/X_train_form.npy")
    Y_train_form = numpy.load("./data/Y_train_form.npy")
    X_test_form = numpy.load("./data/X_test_form.npy")
    Y_test_form = numpy.load("./data/Y_test_form.npy")

    return data
