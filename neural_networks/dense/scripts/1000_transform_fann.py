import numpy
import sys

def transform_fann(feature_type, 
        input_train_file, X_train_file, Y_train_file):
    train_fann = open(input_train_file, 'r')

    info = train_fann.readline().split()
    train_output_dimensions = int(info[2])
    #Extract train
    x = []
    y = [] 
    x_tmp = [] 
    isInput = 1
    sys.stderr.write("Getting lines...\n")
    if feature_type == "form":
        for line in train_fann:
            line = line.split()
            line = map(float, line)
            if len(line) != train_output_dimensions and len(line) != 0:
                x_tmp += line
            elif len(line) == train_output_dimensions:
                y.append(line)
                x.append(x_tmp)
                x_tmp = []
            
        X_train = numpy.array(x, dtype=numpy.float)
        Y_train = numpy.array(y, dtype=numpy.float)

    else:
        for line in train_fann:
            line = line.split()
            line = map(int, line)
            if len(line) != train_output_dimensions and len(line) != 0:
                x_tmp += line
            elif len(line) == train_output_dimensions:
                y.append(line)
                x.append(x_tmp)
                x_tmp = []
                
        X_train = numpy.array(x, dtype=numpy.uint8)
        Y_train = numpy.array(y, dtype=numpy.uint8)

    #Save output
    sys.stderr.write("Saving information...\n")
    numpy.save(X_train_file, X_train)
    numpy.save(Y_train_file, Y_train)

    #Close files
    train_fann.close()
    return info

def set_io_file(io_info, io_file_name, feature_type, data_type):
    io_file = open(io_file_name, "r")
    data_type = data_type.lower()
    lines = [] 
    hasFeature = 0
    #Iterate through file looking for any updates to dimensions
    for line in io_file:
        line = line.split()
        if feature_type == line[0] and data_type == line[1]:
            if io_info[1] != line[2]:
                line[2] = io_info[1]
            if io_info[2] != line[3]:
                line[3] = io_info[2]
        output_line = ""
        for element in line:
            output_line += element + " "
        output_line += "\n"
        lines.append(output_line)
    io_file.close()
    output = open(io_file_name, "w")
    #Write any updates back to file
    for line in lines:
        output.write(line)
    output.close()

if __name__ == "__main__":
    
    if len(sys.argv) != 4:
        sys.stderr.write("Usage: python transform_fann.py <feature_type> "+
                "<TRAIN or TEST data> <io_dimensions_file>\n")
        sys.exit(2)

    fann_file_location = "./fanns/"

    io_file = sys.argv[3]
    
    feature_type = sys.argv[1]

    train_fann_file = fann_file_location + feature_type + "_train.fann"
    test_fann_file = fann_file_location + feature_type + "_dev.fann"

    X_train_file = "./numpy_arrays/X_train_" + feature_type + ".npy"
    Y_train_file = "./numpy_arrays/Y_train_" + feature_type + ".npy"

    X_test_file = "./numpy_arrays/X_test_" + feature_type + ".npy"
    Y_test_file = "./numpy_arrays/Y_test_" + feature_type + ".npy"

    if sys.argv[2] == "TRAIN":
        sys.stderr.write("starting " + feature_type + " train data...\n")
        io_info = transform_fann(feature_type, 
                train_fann_file, X_train_file, Y_train_file)
        set_io_file(io_info, sys.argv[3], feature_type, sys.argv[2])

    elif sys.argv[2] == "TEST":
        sys.stderr.write("starting " + feature_type + " test data...\n")
        io_info = transform_fann(feature_type, 
                test_fann_file, X_test_file, Y_test_file)
        set_io_file(io_info, sys.argv[3], feature_type, sys.argv[2])

    else:
        sys.stderr.write("Must specify if data is TEST or TRAIN\n")
        sys.exit(1)

