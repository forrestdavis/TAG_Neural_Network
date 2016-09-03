import numpy
import sys
import os
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
# {X: dimensions} where X is a feature including output as its own feature
def get_dimensions(dimensions_filename):

    dimensions_file = open(dimensions_filename, "r")
    d = {}

    for line in dimensions_file:
        line = line.strip('\n')
        line = line.split()
        feat = line[0]
        input_value_data = int(line[1])
        d[feat] = input_value_data
    dimensions_file.close()
    return d

def getTrainData(data_directory, verbose, find_feats=None):
    #Get the file names for all train files in the data directory
    #Assumes that the files are in the format X_train_? where
    #? is a feature. Also assumes that the output data is Y_train
    data_files = []
    feats = []
    output_filename = ""
    for filename in os.listdir(data_directory):
        if "train" in filename:
            if filename[0] == "Y":
                output_filename = filename
            else:
                if find_feats:
                    mod_filename = filename.split(".")[0].split("_")
                    if mod_filename[2] in find_feats:
                        data_files.append(filename)
                        feats.append(mod_filename[2])
                else:
                    data_files.append(filename)
                    filename = filename.split(".")[0].split("_")
                    feats.append(filename[2])
    #Get train data
    error = "There was no data found. Either you specified features that do "
    error += "not exist or you did not enter make in the desired data "
    error += "directory."
    assert len(data_files)>0, error
    data = []
    Y_train = []
    for x in xrange(len(data_files)):
        if verbose:
            sys.stderr.write("Getting "+feats[x]+" train data ...\n")
        array = numpy.load(data_directory+"/"+data_files[x])
        data.append(array)
    if len(output_filename)>0:
        if verbose:
            sys.stderr.write("Getting output train data ...\n")
        Y_train = numpy.load(data_directory+"/"+ output_filename)

    #There must be output information
    assert len(Y_train)!=0, "There must be output information to train the model"
    
    return data, Y_train, feats

def getTestData(data_directory, verbose):
    #Get the file names for all test files in the data directory
    #Assumes that the files are in the format X_test_? where
    #? is a feature. Also assumes that the output data is Y_test
    data_files = []
    feats = []
    output_filename = ""
    for filename in os.listdir(data_directory):
        if "test" in filename:
            if filename[0] == "Y":
                output_filename = filename
            else:
                data_files.append(filename)
                filename = filename.split(".")[0].split("_")
                feats.append(filename[2])
    #Get test data
    data = []
    Y_test = []
    for x in xrange(len(data_files)):
        if verbose:
            sys.stderr.write("Getting "+feats[x]+" test data ...\n")
        array = numpy.load(data_directory+"/"+data_files[x])
        data.append(array)
    if len(output_filename)>0:
        if verbose:
            sys.stderr.write("Getting output test data ...\n")
        Y_test = numpy.load(data_directory+"/"+ output_filename)

    #There must be output information
    assert len(Y_test)!=0, "There must be output information to test the model"
    
    return data, Y_test, feats

def getPredictionData(fann_file, fm_file, io_file_name, verbose):
    fann = open(fann_file, "r")
    fm = open(fm_file, "r")
    dictionary = {}
    feats = []
    output = []
    data = []
    data_types = []

    #Create a list of features from the fm file
    for feat in fm:
        feat = feat.strip('\n')
        dim = feat[2:]
        #If # at beginning of line skip
        if feat[0] == "#":
            pass
        else:
            feats.append(feat)
            if dim not in dictionary:
                dictionary[dim] = {}
                dictionary[dim][feat] = []
            else:
                dictionary[dim][feat] = []

    #Iterate through fann file and return a dictionary of the form
    #{X: {exact feature(i.e s0A): one hot encodings}} where X is a feature
    feat_num = 0
    num_feats = len(feats)
    if verbose:
        sys.stderr.write("Reading fann file...\n")
    for line in fann:
        line = line.strip('\n')
        if line:
            if feat_num == num_feats:
                line = map(int, line.split())
                output.append(line)
                feat_num = 0 
            else:
                feat = feats[feat_num]
                dim = feat[2:]
                #If word embedding need to map to float not int
                if dim == "f":
                    line = map(float, line.split())
                else:
                    line = map(int, line.split())
                fv = dictionary[dim][feat]
                if not fv:
                    dictionary[dim][feat] = [line]
                else:
                    fv.append(line)
                    dictionary[dim][feat] = fv
                feat_num += 1

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

        assert len(s0) != 0, "s0%s is necessary for model" %key
        assert len(s1) != 0, "s1%s is necessary for model" %key
        assert len(s2) != 0, "s2%s is necessary for model" %key
        assert len(s3) != 0, "s3%s is necessary for model" %key
        assert len(b0) != 0, "b0%s is necessary for model" %key
        assert len(b1) != 0, "b1%s is necessary for model" %key
        assert len(b2) != 0, "b2%s is necessary for model" %key
        assert len(b3) != 0, "b3%s is necessary for model" %key

        feat = key
        if key == "f":
            feat = "form"
        if key == "p":
            feat = "pos"

        total = [[] for i in xrange(len(s0))]
        for x in xrange(len(s0)):
            total[x] = s0[x]+s1[x]+s2[x]+s3[x]+b0[x]+b1[x]+b2[x]+b3[x]
        dictionary[key]['total'] = total

        #Check that dimensions will work with model
        check_io_file(io_file_name, feat, len(total[0]))

        #Create numpy arrays from dictionary
        data_types.append(feat)
        if key == "f":
            array = numpy.array(total, dtype=numpy.float)
        else:
            array = numpy.array(total, dtype=numpy.uint8)

        data.append(array)

    fann.close()
    fm.close()
    return data, data_types

def arrangeData(test_data, train_feats, test_feats):
    modified_test_data = []
    missing_test_feats = []
    for x in xrange(len(train_feats)):
        train_feat = train_feats[x]
        hasFeat = 0
        for y in xrange(len(test_feats)):
            test_feat = test_feats[y]
            if test_feat == train_feat:
                modified_test_data.append(test_data[y])
                hasFeat = 1
        if not hasFeat:
            missing_test_feats.append(train_feat)

    error_message = "You are missing the following test features"
    assert not missing_test_feats, error_message+"%r" %missing_test_feats

    return modified_test_data

#Check that feature and dimension are the same as the one
#in the io_file
def check_io_file(io_file_name, feat, dim):
    if os.path.isfile(io_file_name):
        dim = str(dim)
        io_file = open(io_file_name, "r")
        sameDim = 0
        for line in io_file:
            line = line.split()
            if feat == line[0]:
                if dim == line[1]:
                    sameDim = 1
        io_file.close()
        assert sameDim, "There is a dimension mismatch with %s" %feat
    else:
        sys.stderr.write("io dimension file not found. Needed for checking " +
                "evaluation or prediction data dimensions\n")
        sys.exit(1)

def saveFeats(train_feats, filename):
    output = open(filename, "w")
    for feat in train_feats:
        output.write(feat+"\n")
    output.close()

def loadFeats(filename):
    feat_file = open(filename, "r")
    train_feats=[]
    for line in feat_file:
        line = line.strip("\n")
        train_feats.append(line)
    feat_file.close()
    return train_feats

def createModel(dimensions_dictionary, feats, verbose, 
        nb_layers, activation_functs, nodes, 
        merge_nb_layers, 
        merge_activation_functs, merge_nodes):

    if verbose:
        sys.stderr.write("creating model...\n")
    model_total = Sequential()

    models = []

    for feat in feats:
        if feat == "output":
            pass
        else:
            HasMultiAct = False
            if len(activation_functs)>1:
                error = "number of layers and number of activation functions "
                error += "must be the same if you are specifying multiple "
                error += "functions"
                assert len(activation_functs)==nb_layers, error
                HasMultiAct = True

            HasMultiNode = 0
            if len(nodes)>1:
                error = "number of layers and number of nodes "
                error += "must be the same if you are specifying multiple "
                error += "node sizes"
                assert len(nodes)==nb_layers, error
                HasMultiNode = True

            a = 0
            n = 0

            model = Sequential(name=feat)
            for i in xrange(nb_layers):
                if i == 0:
                    model.add(Dense(nodes[n], 
                        input_dim=dimensions_dictionary[feat], 
                        init='uniform'))
                    model.add(Activation(activation_functs[a]))
                    model.add(Dropout(0.50))
                else:
                    model.add(Dense(nodes[n]))
                    model.add(Activation(activation_functs[a]))
                    model.add(Dropout(0.50))

                if HasMultiNode:
                    n += 1
                if HasMultiAct:
                    a += 1

            models.append(model)


    feat = 'output'

    model_total.add(Merge(models, mode='concat', name="total"))

    HasMultiAct = False
    if len(merge_activation_functs)>1:
        error = "number of layers and number of activation functions "
        error += "must be the same if you are specifying multiple "
        error += "functions for after the merge"
        assert len(merge_activation_functs)==merge_nb_layers, error
        HasMultiAct = True

    HasMultiNode = 0
    if len(merge_nodes)>1:
        error = "number of layers and number of nodes "
        error += "must be the same if you are specifying multiple "
        error += "node sizes for after the merge"
        assert len(merge_nodes)==merge_nb_layers, error
        HasMultiNode = True

    a = 0
    n = 0

    for i in xrange(merge_nb_layers):
        model_total.add(Dense(nodes[n]))
        model_total.add(Activation(activation_functs[a]))
        model_total.add(Dropout(0.50))

        if HasMultiNode:
            n += 1
        if HasMultiAct:
            a += 1
    
    model_total.add(Dense(dimensions_dictionary[feat]))
    model_total.add(Activation('softmax'))

    #Compile model
    model_total.compile(loss='categorical_crossentropy', 
            optimizer='adam', metrics=['accuracy'])

    return model_total
