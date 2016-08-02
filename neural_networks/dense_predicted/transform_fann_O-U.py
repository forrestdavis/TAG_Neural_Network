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

    #Save output
    sys.stderr.write("Saving information...\n")
    numpy.save(X_train_file, X_train)
    numpy.save(Y_train_file, Y_train)

    #Close files
    train_fann.close()
    return info[1], info[2]

if __name__ == "__main__":

    sys.stderr.write("starting O train data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/O_train.fann"
    X_train_file = "X_train_O.npy"
    Y_train_file = "Y_train_O.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "O train", input_dim, output_dim
    sys.stderr.write("starting O test data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/O_dev.fann"
    X_train_file = "X_test_O.npy"
    Y_train_file = "Y_test_O.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "O test", input_dim, output_dim

    sys.stderr.write("starting P train data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/P_train.fann"
    X_train_file = "X_train_P.npy"
    Y_train_file = "Y_train_P.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "P train", input_dim, output_dim
    sys.stderr.write("starting P test data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/P_dev.fann"
    X_train_file = "X_test_P.npy"
    Y_train_file = "Y_test_P.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "P test", input_dim, output_dim

    sys.stderr.write("starting Q train data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/Q_train.fann"
    X_train_file = "X_train_Q.npy"
    Y_train_file = "Y_train_Q.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "Q train", input_dim, output_dim
    sys.stderr.write("starting Q test data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/Q_dev.fann"
    X_train_file = "X_test_Q.npy"
    Y_train_file = "Y_test_Q.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "Q test", input_dim, output_dim

    sys.stderr.write("starting R train data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/R_train.fann"
    X_train_file = "X_train_R.npy"
    Y_train_file = "Y_train_R.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "R train", input_dim, output_dim
    sys.stderr.write("starting R test data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/R_dev.fann"
    X_train_file = "X_test_R.npy"
    Y_train_file = "Y_test_R.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "R test", input_dim, output_dim

    sys.stderr.write("starting S train data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/S_train.fann"
    X_train_file = "X_train_S.npy"
    Y_train_file = "Y_train_S.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "S train", input_dim, output_dim
    sys.stderr.write("starting S test data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/S_dev.fann"
    X_train_file = "X_test_S.npy"
    Y_train_file = "Y_test_S.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "S test", input_dim, output_dim

    sys.stderr.write("starting T train data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/T_train.fann"
    X_train_file = "X_train_T.npy"
    Y_train_file = "Y_train_T.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "T train", input_dim, output_dim
    sys.stderr.write("starting T test data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/T_dev.fann"
    X_train_file = "X_test_T.npy"
    Y_train_file = "Y_test_T.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "T test", input_dim, output_dim

    sys.stderr.write("starting U train data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/U_train.fann"
    X_train_file = "X_train_U.npy"
    Y_train_file = "Y_train_U.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "U train", input_dim, output_dim
    sys.stderr.write("starting U test data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/U_dev.fann"
    X_train_file = "X_test_U.npy"
    Y_train_file = "Y_test_U.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "U test", input_dim, output_dim
