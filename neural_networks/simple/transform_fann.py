import numpy
import sys

def transform_fann(input_train_file, X_train_file, Y_train_file,
        input_test_file, X_test_file, Y_test_file):
    train_fann = open(input_train_file, 'r')
    test_fann = open(input_test_file, 'r')

    #Get train information on input and output size
    info = train_fann.readline().split()
    train_input_dimensions = int(info[1])
    train_output_dimensions = int(info[2])

    #Get test information on input and output size
    info = test_fann.readline().split()
    test_input_dimensions = int(info[1])
    test_output_dimensions = int(info[2])

    diff_i_train_test = train_input_dimensions-test_input_dimensions
    diff_o_train_test = train_output_dimensions-test_output_dimensions
    print "train", train_input_dimensions, train_output_dimensions
    print "test", test_input_dimensions, test_output_dimensions

    if diff_i_train_test != 0:
        sys.stderr("Error: train.fann and test.fann do not have same " +
                "input dimensions")
        sys.exit(1)
    if diff_o_train_test != 0:
        sys.stderr("Error: train.fann and test.fann do not have same " +
                "output dimensions")
        sys.exit(1)

    #Extract train
    x = []
    y = [] 
    x_tmp = [] 
    isInput = 1
    for line in train_fann:
        line = line.split()
        line = map(float, line)
        if len(line) != train_output_dimensions and len(line) != 0:
            x_tmp += line
        elif len(line) == train_output_dimensions:
            y.append(line)
            x.append(x_tmp)
            x_tmp = []
            
    X_train = numpy.array(x)
    Y_train = numpy.array(y)

    #Extract test
    x = []
    y = [] 
    x_tmp = [] 
    isInput = 1
    for line in test_fann:
        line = line.split()
        line = map(float, line)
        if len(line) != test_output_dimensions and len(line) != 0:
            x_tmp += line
        elif len(line) == test_output_dimensions:
            y.append(line)
            x.append(x_tmp)
            x_tmp = []
            
    X_test = numpy.array(x)
    Y_test = numpy.array(y)

    #Save output
    numpy.save(X_train_file, X_train)
    numpy.save(Y_train_file, Y_train)
    numpy.save(X_test_file, X_test)
    numpy.save(Y_test_file, Y_test)

    #Close files
    train_fann.close()
    test_fann.close()

if __name__ == "__main__":
    input_train_file = "../../data/simple_fann/train.fann"
    X_train_file = "X_train.npy"
    Y_train_file = "Y_train.npy"
    input_test_file = "../../data/simple_fann/dev.fann"
    X_test_file = "X_dev.npy"
    Y_test_file = "Y_dev.npy"
    transform_fann(input_train_file, X_train_file, Y_train_file,
            input_test_file, X_test_file, Y_test_file)

