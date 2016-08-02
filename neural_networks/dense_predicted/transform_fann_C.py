import numpy
import sys

def transform_fann(input_train_file, X_train_file, Y_train_file):
    train_fann = open(input_train_file, 'r')

    info = train_fann.readline().split()
    train_output_dimensions = int(info[2])
    #Extract train
    x = []
    y = [] 
    x_tmp = [] 
    isInput = 1
    sys.stderr.write("Getting lines...\n")
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
    
    print X_train
    print Y_train

    #Save output
    sys.stderr.write("Saving information...\n")
    numpy.save(X_train_file, X_train)
    numpy.save(Y_train_file, Y_train)

    #Close files
    train_fann.close()
    return info[1], info[2]

if __name__ == "__main__":
    sys.stderr.write("starting example train data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/A_train.fann"
    X_train_file = "X_train_example.npy"
    Y_train_file = "Y_train_example.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "example train", input_dim, output_dim
    sys.stderr.write("starting example test data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/A_dev.fann"
    X_train_file = "X_test_example.npy"
    Y_train_file = "Y_test_example.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "example test", input_dim, output_dim
