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
        if "_" in feat:
            feat = feat.split("_")
            feat = feat[1][0]+feat[1][1]+feat[0]
        dim = feat[2:]
        #If # at beginning of line skip
        if feat:
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
        needChange = 0
        if key=="D" or key=="E" or key=="F" or key=="G" or key=="O" or key=="P":
            needChange = 1

        s0=s1=s2=s3=b0=b1=b2=b3 = []
        for subkey in dictionary[key]:
            if "s0" in subkey:
                s0=dictionary[key][subkey]
                if needChange:
                    s0=changeList(key, s0)
            if "s1" in subkey:
                s1=dictionary[key][subkey]
                if needChange:
                    s1=changeList(key, s1)
            if "s2" in subkey:
                s2=dictionary[key][subkey]
                if needChange:
                    s2=changeList(key, s2)
            if "s3" in subkey:
                s3=dictionary[key][subkey]
                if needChange:
                    s3=changeList(key, s3)
            if "b0" in subkey:
                b0=dictionary[key][subkey]
                if needChange:
                    b0=changeList(key, b0)
            if "b1" in subkey:
                b1=dictionary[key][subkey]
                if needChange:
                    b1=changeList(key, b1)
            if "b2" in subkey:
                b2=dictionary[key][subkey]
                if needChange:
                    b2=changeList(key, b2)
            if "b3" in subkey:
                b3=dictionary[key][subkey]
                if needChange:
                    b3=changeList(key, b3)

        if key == "ldep" or key == "rdep" or key == "ndep":
            assert len(s0) != 0, "s0%s is necessary for model" %key
            assert len(b0) != 0, "b0%s is necessary for model" %key
            total = s0[0]+b0[0]
        elif key == "dist":
            assert len(s0) != 0, "s0%s is necessary for model" %key
            total = s0[0]
        else:
            assert len(s0) != 0, "s0%s is necessary for model" %key
            assert len(s1) != 0, "s1%s is necessary for model" %key
            assert len(s2) != 0, "s2%s is necessary for model" %key
            assert len(s3) != 0, "s3%s is necessary for model" %key
            assert len(b0) != 0, "b0%s is necessary for model" %key
            assert len(b1) != 0, "b1%s is necessary for model" %key
            assert len(b2) != 0, "b2%s is necessary for model" %key
            assert len(b3) != 0, "b3%s is necessary for model" %key
            total = s0[0]+s1[0]+s2[0]+s3[0]+b0[0]+b1[0]+b2[0]+b3[0]

        feat = key
        if key == "f":
            feat = "form"
        if key == "p":
            feat = "pos"

        #total = s0[0]+s1[0]+s2[0]+s3[0]+b0[0]+b1[0]+b2[0]+b3[0]
        dictionary[key]['total'] = total

        #Check that dimensions will work with model
        if key != "ldep" and key != "rdep" and key != "ndep" and key != "dist":
            check_io_file(io_file_name, feat, len(total))

        #Create numpy arrays from dictionary
        if key != "ldep" and key != "rdep" and key != "ndep" and key != "dist":
            data_types.append(feat)
            if key == "f":
                array = numpy.array([total], dtype=numpy.float)
            else:
                array = numpy.array([total], dtype=numpy.uint8)

            data.append(array)
    '''
    total = (dictionary["ldep"]["s0ldep"][0] +
    dictionary["rdep"]["s0rdep"][0] +
    dictionary["ldep"]["b0ldep"][0] +
    dictionary["rdep"]["b0rdep"][0] +
    dictionary["ndep"]["s0ndep"][0] +
    dictionary["ndep"]["b0ndep"][0] +
    dictionary["dist"]["s0dist"][0])
    feat = "dep"
    data_types.append(feat)
    check_io_file(io_file_name, feat, len(total))
    array = numpy.array([total], dtype=numpy.uint8)
    data.append(array)
    '''
    fann.close()
    fm.close()
    return data, data_types

def changeList(feat, in_data):

    in_data = in_data[0]
    data_type = getDataType(feat)
    vocab_file = open("test.alpha", "r")
    vocab = [] 

    isFeat = 0

    nb_type = 0
    for line in vocab_file:
        line = line.strip("\n")
        if line == feat:
            isFeat = 1
        elif isFeat:
            if line.isdigit():
                nb_type = int(line)
            isFeat = 0
        elif nb_type:
            vocab.append(line)
            nb_type -= 1

    vocab_file.close()

    if feat == "D" or feat == "E":
        nb = -1
        for x in xrange(len(in_data)):
            if in_data[x] == 1:
                nb = x
        if nb == -1:
            node  = [("nil")]
        else:
            node = vocab[nb]
            node = node.split("_")
            for x in xrange(len(node)):
                node[x] = tuple(node[x].split("#"))
        out = []
        for x in xrange(len(data_type)):
            hasElement = 0
            for element in node:
                if data_type[x] == element:
                    hasElement = 1
            if hasElement:
                out.append(1)
            else:
                out.append(0)
        return [out]

    if feat == "F" or feat == "G":
        nb = -1
        for x in xrange(len(in_data)):
            if in_data[x] == 1:
                nb = x
        if nb == -1:
            node  = [("nil")]
        else:
            node = vocab[nb]
            node = node.split("_")
        out = []
        for x in xrange(len(data_type)):
            hasElement = 0
            for element in node:
                if data_type[x] == element:
                    hasElement = 1
            if hasElement:
                out.append(1)
            else:
                out.append(0)
        return [out]

    if feat == "O" or feat == "P":
        nb = -1
        for x in xrange(len(in_data)):
            if in_data[x] == 1:
                nb = x
        if nb == -1:
            node  = [("nil")]
        else:
            node = vocab[nb]
            node = node.split("_")
            for x in xrange(len(node)):
                node[x] = tuple(node[x].split("#"))
        out = []
        for x in xrange(len(data_type)):
            hasElement = 0
            for element in node:
                if data_type[x] == element:
                    hasElement = 1
            if hasElement:
                out.append(1)
            else:
                out.append(0)
        return [out]

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

def getDataType(feat):

    lfront_nodes = [('PP', 's', '2'), ('NP', 's', '0'), ('AdvP', 's', 'X'), 
            ('VP', 's', 'X'), ('IN', 's', 'X'), ('PRT', 's', 'X'), 
            ('PP', 's', 'X'), ('NP', 's', 'X'), ('NP', 's', '1'), 
            ('S', 's', '1'), ('Punct', 's', 'X'), ('S', 's', '0'), 
            ('AP', 's', 'X'), ('VP', 's', '1'), 
            ('NP', 's', '2'), ('AdvP', 's', '2'), ('AdvP', 's', '1'), 
            ('PP', 's', '1'), ('AdvP', 's', '0'), ('S', 's', '2'), 
            ('S', 's', 'X'), ('AP', 's', '2'), ('AP', 's', '0'), 
            ('FRAG', 's', '1'), ('N', 's', 'X'), ('CC', 's', 'X'), 
            ('PP', 's', '0'), ('IN', 's', '0'), ('.', 's', 'X')]

    rfront_nodes = [('NP', 's', '1'), ('PP', 's', '2'), ('S', 's', '1'), 
            ('IN', 'c', 'X'),
    ('S', 's', 'X'), ('NP', 's', 'X'), ('N', 's', 'X'), ('RP', 'c', 'X'), 
    ('V', 's', '1'), ('AdvP', 's', 'X'), ('NP', 's', '2'), ('S', 's', '2'), 
    ('PP', 's', 'X'), ('PP', 's', '1'), ('IN', 's', 'X'), ('NP', 's', '0'), 
    ('FRAG', 's', '1'), ('Punct', 's', 'X'), ('CC', 's', 'X'), 
    ('AP', 's', '1'), ('.', 's', 'X'), ('Ad', 'c', 'X'), ('UCP', 's', '1'), 
    ('D', 's', '1'), ('AP', 's', '2'), ('NP', 's', '3'), ('S', 's', '3'),
    ('PRN', 's', 'X'), ('VP', 's', 'X'), ('Comp', 's', '1'), ('VP', 's', '1'), 
    ('PRN', 's', '1'), ('PRT', 's', 'X'), ('PP', 's', '0'), ('A', 'c', 'X'), 
    ('-RRB-', 's', '1'), ('X', 's', 'X'), ('CC', 's', '2'), ('-LRB-', 's', '1'), 
    ('AdvP', 's', '1'), ('N', 's', '1'), ('A', 's', 'X'), ('IN', 's', '1'), 
    ('A', 's', '1'), ('S', 's', '0'), ('Ad', 's', '1'), ('N', 'c', 'X'), 
    ('CC', 's', '1'), ('X', 's', '1'), ('UCP', 's', '2'), ('UH', 's', '1'), 
    ('AdvP', 's', '2'), ('-RRB-', 's', 'X'), ('Ad', 's', 'X'), ('S', 's', '4'), 
    ('-LRB-', 's', 'X'), ('AdvP', 's', '0'), ('AP', 's', 'X'), ('FW', 's', '1'),
     ('V', 'c', 'X'), ('INTJ', 's', 'X'), ('G', 's', '1'), ('PP', 's', '3'), 
    ('NPP', 's', '1'), ('CONJP', 's', 'X'), ('INTJ', 's', '1'), ('VP', 's', '2'), 
    ('RRC', 's', '1'), ('AP', 's', '3'), ('RP', 's', '1'), ('V', 's', 'X'), 
    ('MD', 's', '1'), ('NP', 's', '4'), ('PRN', 's', '2')]

    ladj_nodes = ['S', 'NP', 'VP', 'V', 'Ad', 'PRN', '-LRB-', 'EX', 'AdvP', 'CONJP', 
    'Punct', 'INTJ', 'UH', 'AP', 'POS', 'X', 'D', 'UCP', 'IN', 'A', 'N', 'PP', 
    '``', 'CC', "''", 'WP', '.', 'FRAG', 'TO', 'PDT', 'G', 'RRC', 'RP', 'NPP',
    'Comp', 'LST', 'QP', '$', 'FW', '-RRB-', 'SYM', 'MD', 'PRT', 'PRT|ADVP', 
    'WP$', '-HASHTAG-']

    radj_nodes = ['V', 'VP', 'S', 'PP', 'Ad', 'NP', '-LRB-', 'PRN', 'EX', 'AdvP', 
    'CONJP', 'PRT', 'Punct', 'UH', 'INTJ', 'AP', 'POS', 'D', 'X', 'UCP', 
    'IN', 'A', 'N', '``', 'CC', "''", 'WP', '.', 'FRAG', 'TO', 'PDT', 
    'G', 'RRC', 'RP', 'NPP', 'Comp', 'LST', 'QP', '$', 'FW', '-RRB-', 
    'SYM', 'MD', 'PRT|ADVP', 'WP$', '-HASHTAG-']

    dsub_nodes = [('NP', '0'), ('NP', '1'), ('PP', '2'), ('NP', '2'), ('VP', '1'),
            ('S', '1'), ('V', '1'), ('S', '2'), ('PP', '1'), ('FRAG', '1'), 
            ('AP', '1'), ('S', '0'), ('UCP', '1'), ('D', '1'), ('AP', '2'), 
            ('NP', '3'), ('S', '3'), ('Comp', '1'), ('PRN', '1'), ('AdvP', '2'), 
            ('AdvP', '1'), ('PP', '0'), ('-RRB-', '1'), ('CC', '2'), 
            ('-LRB-', '1'), ('AdvP', '0'), ('N', '1'), ('IN', '1'), 
            ('A', '1'), ('Ad', '1'), ('CC', '1'), ('X', '1'), ('UCP', '2'),
            ('UH', '1'), ('VP', '0'), ('AP', '0'), ('S', '4'), ('VP', '2'),
            ('FW', '1'), ('G', '1'), ('PP', '3'), ('NPP', '1'), ('INTJ', '1'), 
            ('IN', '0'), ('RRC', '1'), ('AP', '3'), ('RP', '1'), 
            ('MD', '1'), ('NP', '4'), ('PRN', '2')]

    dsub2_nodes = [('NP', '0'), ('NP', '1'), ('PP', '2'), ('NP', '2'), ('VP', '1'),
     ('S', '1'), ('NP', '1(P)'), ('S', '1(P)'), ('V', '1'), 
    ('NP', '2(P)'), ('S', '2'), ('PP', '1'), ('NP', '0(P)'), 
    ('FRAG', '1(P)'), ('S', '2(P)'), ('AP', '1(P)'), 
    ('S', '0'), ('UCP', '1(P)'), ('D', '1'), ('AP', '2(P)'), 
    ('D', '1(P)'), ('NP', '3(P)'), ('S', '3'), ('Comp', '1'), 
    ('PRN', '1(P)'), ('S', '3(P)'), ('AdvP', '2'), ('AdvP', '1'), 
    ('PP', '0'), ('AP', '1'), ('-RRB-', '1(P)'), ('CC', '2(P)'), 
    ('-LRB-', '1(P)'), ('VP', '1(P)'), ('AdvP', '0'), 
    ('AdvP', '1(P)'), ('N', '1(P)'), ('IN', '1(P)'), 
    ('IN', '1'), ('A', '1(P)'), ('Ad', '1(P)'), ('CC', '1(P)'), 
    ('X', '1'), ('N', '1'), ('UCP', '2(P)'), ('UH', '1'), ('VP', '0'), 
    ('AdvP', '2(P)'), ('NP', '3'), ('AP', '2'), ('X', '1(P)'),
     ('AP', '0'), ('S', '4(P)'), ('S', '4'), ('VP', '2'), 
    ('FW', '1'), ('G', '1'), ('FRAG', '1'), ('A', '1'), ('PP', '3'), 
    ('NPP', '1'), ('INTJ', '1'), ('Ad', '1'), ('VP', '2(P)'), 
    ('IN', '0'), ('RRC', '1'), ('AP', '3(P)'), ('RP', '1'), 
    ('G', '1(P)'), ('MD', '1'), ('NP', '4(P)'), ('PRN', '2(P)')]

    data = "NONE"
    if feat == "D":
        data = lfront_nodes
    if feat == "E":
        data = rfront_nodes
    if feat == "F":
        data = ladj_nodes
    if feat == "G":
        data = radj_nodes
    if feat == "O":
        data = dsub_nodes
    if feat == "P":
        data = dsub2_nodes

    return data
