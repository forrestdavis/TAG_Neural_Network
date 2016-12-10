import sys
import os
import numpy


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
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: python dep2numpy.py"+
                " <TRAIN or TEST>\n")
        sys.exit(1)
    if sys.argv[1] == "TRAIN":
        input_filename = "fanns/dep_train.fann"
        output_filename = "numpy_arrays/X_train_dep.npy"

    elif sys.argv[1] == "TEST":
        input_filename = "fanns/dep_dev.fann"
        output_filename = "numpy_arrays/X_test_dep.npy"
    else:
        sys.stderr.write("Options are TRAIN or TEST\n")
        sys.exit(1)

    io_file = "io_dimensions.txt"

    train = open(input_filename, "r")

    info = train.readline().strip("\n").split()

    X = []
    Y = []
    x = []
    for line in train:
        line = line.strip("\n").split()
        if line:
            if len(line) == 17:
                Y.append(map(int, line))
                X.append(x)
                x = []
            else:
                x += map(int, line)

    if sys.argv[1] == "TRAIN":
        set_io_file(io_file, "dep", X[0])
     
    if sys.argv[1] == "TEST":
        check_io_file(io_file, "dep", X[0])
        

    X_numpy = numpy.array(X, dtype=numpy.uint8)
    #Y_numpy = numpy.array(Y, dtype=numpy.uint8)

    numpy.save(output_filename, X_numpy)
    #numpy.save("Y_dep", Y_numpy)
