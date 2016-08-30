import numpy
import os
import sys

#Takes as input a feature, dataType, input filename,
#output filename, info filename and io filename 
###########################################################
#dataType is TRAIN or TEST
#input and output files are binary fann files
#info file describes the binary file and is in the format:
#feature_type number_of_examples    input_dimensions output_dimensions
#io filename is a file describing the dimensions of the data
#and is used for error checking data and by the keras model
#############################################
#Saves numpy arrays to X_dataType_feat.npy
#and Y_dataType.npy
def loadBin(dataType, input_filename,
        output_filename, info_filename, io_filename):

    sys.stderr.write("loading binary fann file...\n")
    info = open(info_filename, "r")
    io = info.readline().strip("\n").split()
    info.close()
    feat = io[0]
    nb_examples = int(io[1])
    input_dim = io[2]
    output = "output"
    output_dim = io[3]
    
    #Either set data dimensions or check for errors
    if dataType == "TRAIN":
        set_io_file(io_filename, feat, input_dim)
        set_io_file(io_filename, output, output_dim)
    if dataType == "TEST":
        check_io_file(io_filename, feat, input_dim)
        check_io_file(io_filename, output, output_dim)


    in_array = numpy.fromfile(input_filename, dtype=numpy.uint8)
    out_array = numpy.fromfile(output_filename, dtype=numpy.uint8)

    #Reshape into an array for every example
    mod_in = numpy.reshape(in_array, (nb_examples, -1))
    mod_out = numpy.reshape(out_array, (nb_examples, -1))

    #Save files
    numpy.save("numpy_arrays/X_"+dataType.lower()+"_"+feat+".npy", mod_in)
    numpy.save("numpy_arrays/Y_"+dataType.lower()+".npy", mod_out)

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

if __name__=="__main__":
    if len(sys.argv)!=6:
        sys.stderr.write("Usage: <TRAIN or TEST>"+
                " <input_data_filename> <output_data_filename> " +
                "<binary_info_filename> <io_info_filename>\n")
        sys.exit(1)
    dataType = sys.argv[1]
    input_filename = sys.argv[2]
    output_filename = sys.argv[3]
    info_filename = sys.argv[4]
    io_filename = sys.argv[5]
    loadBin(dataType,input_filename,output_filename,info_filename,
            io_filename)
