import numpy
import sys
import os
##########################################################################
# Class for getting a prediction for depedency parser movement given input
# data and a trained model
#
# Forrest Davis
# August 11, 2016
##########################################################################

#Set io file so that the file is in the form:
#feature dimensions_of_input
def set_io_file(io_filename, feat, dim):
    dim = str(dim)
    #If file exists check for feature and dimension
    if os.path.isfile(io_filename):
        hasFeature = 0
        lines = []
        io_file = open(io_filename, "r")
        #Iterate through file, either finding the feature and 
        #changing the dimension if there is a difference or adding 
        #it if the feature is not in the file
        for line in io_file:
            line = line.strip('\n')
            line = line.split()
            if feat == line[0]:
                hasFeature = 1
                if dim != line[1]:
                    line[1] = dim
            output_line = ""
            for element in line:
                output_line += element + " "
            output_line += "\n"
            lines.append(output_line)
        if not hasFeature:
            output_line = feat + " " + dim +"\n"
            lines.append(output_line)
        io_file.close()
        output = open(io_filename, "w")
        for line in lines:
            output.write(line)
        output.close()
    #If io_file does not exisit create file and write feature to file
    else:
        output_line = feat + " " + dim + "\n"
        output = open(io_filename, "w")
        output.write(output_line)
        output.close()

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

#Function for transfom fann file into output
#fm and fann file must contain (in any order):
#s0X s1X s2X s3X b0X b1X b2X b3X where X is a feature from the fm file
def fann2numpy(fann_file, fm_file, io_file_name, dataType):
    fann = open(fann_file, "r")
    fm = open(fm_file, "r")
    dictionary = {}
    feats = []
    output = []
    data = []
    data_types = []
    #Get input/output info for model
    if dataType != "PREDICTION":
        fann.readline()

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

        if dataType == "TRAIN":
            set_io_file(io_file_name, feat, len(total[0]))
        else:
            check_io_file(io_file_name, feat, len(total[0]))

        #Create numpy arrays from dictionary
        data_types.append(feat)
        if key == "f":
            array = numpy.array(total, dtype=numpy.float)
        else:
            array = numpy.array(total, dtype=numpy.uint8)

        if dataType == "TRAIN":
            saved_file_name = "numpy_arrays/X_train_" + feat + ".npy"
            numpy.save(saved_file_name, array)

        if dataType == "TEST":
            saved_file_name = "numpy_arrays/X_test_" + feat + ".npy"
            numpy.save(saved_file_name, array)

        data.append(array)

    if output:
        key = "output"
        if dataType == "TRAIN":
            set_io_file(io_file_name, key, len(output[0]))
        if dataType == "TEST":
            check_io_file(io_file_name, key, len(output[0]))
        data_types.append(key)
        array = numpy.array(output, dtype=numpy.uint8)
        if dataType == "TRAIN":
            saved_file_name = "numpy_arrays/Y_train.npy"
            numpy.save(saved_file_name, array)
        if dataType == "TEST":
            saved_file_name = "numpy_arrays/Y_test.npy"
            numpy.save(saved_file_name, array)
    
    fann.close()
    fm.close()
    if dataType == "PREDICTION":
        return data, data_types

if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.stderr.write("Usage: python general.py "+
                "<TRAIN, TEST, or PREDCITION data> <fann_file_name> " +
                "<fm_file_name> <io_file_name>\n")
        sys.exit(1)
    dataType = sys.argv[1]
    fann_file = sys.argv[2]
    fm_file = sys.argv[3]
    io_file = sys.argv[4]
    if dataType == "PREDICTION":
        data, data_types = fann2numpy(fann_file, fm_file, io_file, dataType)
    else:
        fann2numpy(fann_file, fm_file, io_file, dataType)
