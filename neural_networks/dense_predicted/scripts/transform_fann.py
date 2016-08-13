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
    return info[1], info[2]

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: python transform_fann.py <feature_type>\n")
        sys.exit(2)

    fann_file_location = "../../data/dense_predicted_fann/fanns/"
    
    feature_type = sys.argv[1]

    train_fann_file = fann_file_location + feature_type + "_train.fann"
    test_fann_file = fann_file_location + feature_type + "_dev.fann"

    X_train_file = "./data/X_train_" + feature_type + ".npy"
    Y_train_file = "./data/Y_train_" + feature_type + ".npy"
    X_test_file = "./data/X_test_" + feature_type + ".npy"
    Y_test_file = "./data/Y_test_" + feature_type + ".npy"

    sys.stderr.write("starting " + feature_type + " train data...\n")
    input_dim, output_dim = transform_fann(feature_type, 
            train_fann_file, X_train_file, Y_train_file)
    print "%s train" % feature_type, input_dim, output_dim

    sys.stderr.write("starting " + feature_type + " test data...\n")
    input_dim, output_dim = transform_fann(feature_type, 
            test_fann_file, X_test_file, Y_test_file)
    print "%s test" % feature_type, input_dim, output_dim

