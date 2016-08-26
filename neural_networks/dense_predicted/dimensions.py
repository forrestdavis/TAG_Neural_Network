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

def getTrainData(data_directory):

    #Get the file names for all train files in the data directory
    #Assumes that the files are in the format X_train_? where
    #? is a feature. Also assumes that the output data is Y_train
    data_files = []
    feats = []
    for filename in os.listdir(data_directory):
        if "train" in filename:
            data_files.append(filename)
            filename = filename.split(".")[0].split("_")
            if filename[0] == "Y":
                feats.append("output")
            else:
                feats.append(filename[2])
    #Get train data
    data = []
    Y_train = []
    for x in xrange(len(data_files)):
        if feats[x] == "output":
            sys.stderr.write("Getting "+feats[x]+" train data ...\n")
            Y_train = numpy.load(data_directory+"/"+data_files[x])
        else:
            sys.stderr.write("Getting "+feats[x]+" train data ...\n")
            array = numpy.load(data_directory+"/"+data_files[x])
            data.append(array)
    #There must be output information
    assert len(Y_train)!=0, "There must be output information to train the model"
    
    return data, Y_train, feats

def getTestData(data_directory):
    #Get the file names for all test files in the data directory
    #Assumes that the files are in the format X_test_? where
    #? is a feature. Also assumes that the output data is Y_test
    data_files = []
    feats = []
    for filename in os.listdir(data_directory):
        if "test" in filename:
            data_files.append(filename)
            filename = filename.split(".")[0].split("_")
            if filename[0] == "Y":
                feats.append("output")
            else:
                feats.append(filename[2])
    #Get test data
    data = []
    Y_test = []
    for x in xrange(len(data_files)):
        if feats[x] == "output":
            sys.stderr.write("Getting "+feats[x]+" test data ...\n")
            Y_test = numpy.load(data_directory+"/"+data_files[x])
        else:
            sys.stderr.write("Getting "+feats[x]+" test data ...\n")
            array = numpy.load(data_directory+"/"+data_files[x])
            data.append(array)
    #There must be output information
    assert len(Y_test)!=0, "There must be output information to test the model"
    
    return data, Y_test, feats

def createModel(dimensions_dictionary, feats):

    sys.stderr.write("creating model...\n")
    model_total = Sequential()

    models = []

    for feat in feats:
        if feat == "output":
            pass
        else:
            model = Sequential()
            model.add(Dense(50, 
                input_dim=dimensions_dictionary[feat], init='uniform'))
            model.add(Activation('relu'))
            model.add(Dropout(0.50))
            model.add(Dense(50))
            model.add(Activation('relu'))
            model.add(Dropout(0.50))
            models.append(model)

    feat = 'output'
    model_total.add(Merge(models, mode='concat'))
    model_total.add(Dense(dimensions_dictionary[feat]))
    model_total.add(Activation('softmax'))
    
    #Compile model
    model_total.compile(loss='categorical_crossentropy', 
            optimizer='adam', metrics=['accuracy'])

    return model_total
