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

    '''
    sys.stderr.write("starting G train data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/G_train.fann"
    X_train_file = "X_train_G.npy"
    Y_train_file = "Y_train_G.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "G train", input_dim, output_dim
    sys.stderr.write("starting G test data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/G_dev.fann"
    X_train_file = "X_test_G.npy"
    Y_train_file = "Y_test_G.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "G test", input_dim, output_dim

    '''
    sys.stderr.write("starting H train data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/H_train.fann"
    X_train_file = "./data/X_train_H.npy"
    Y_train_file = "./data/Y_train_H.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "H train", input_dim, output_dim
    sys.stderr.write("starting H test data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/H_dev.fann"
    X_train_file = "./data/X_test_H.npy"
    Y_train_file = "./data/Y_test_H.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "H test", input_dim, output_dim

    sys.stderr.write("starting I train data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/I_train.fann"
    X_train_file = "./data/X_train_I.npy"
    Y_train_file = "./data/Y_train_I.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "I train", input_dim, output_dim
    sys.stderr.write("starting I test data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/I_dev.fann"
    X_train_file = "./data/X_test_I.npy"
    Y_train_file = "./data/Y_test_I.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "I test", input_dim, output_dim

    sys.stderr.write("starting J train data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/J_train.fann"
    X_train_file = "./data/X_train_J.npy"
    Y_train_file = "./data/Y_train_J.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "J train", input_dim, output_dim
    sys.stderr.write("starting J test data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/J_dev.fann"
    X_train_file = "./data/X_test_J.npy"
    Y_train_file = "./data/Y_test_J.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "J test", input_dim, output_dim

    sys.stderr.write("starting K train data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/K_train.fann"
    X_train_file = "./data/X_train_K.npy"
    Y_train_file = "./data/Y_train_K.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "K train", input_dim, output_dim
    sys.stderr.write("starting K test data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/K_dev.fann"
    X_train_file = "./data/X_test_K.npy"
    Y_train_file = "./data/Y_test_K.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "K test", input_dim, output_dim

    sys.stderr.write("starting L train data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/L_train.fann"
    X_train_file = "./data/X_train_L.npy"
    Y_train_file = "./data/Y_train_L.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "L train", input_dim, output_dim
    sys.stderr.write("starting L test data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/L_dev.fann"
    X_train_file = "./data/X_test_L.npy"
    Y_train_file = "./data/Y_test_L.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "L test", input_dim, output_dim

    sys.stderr.write("starting M train data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/M_train.fann"
    X_train_file = "./data/X_train_M.npy"
    Y_train_file = "./data/Y_train_M.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "M train", input_dim, output_dim
    sys.stderr.write("starting M test data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/M_dev.fann"
    X_train_file = "./data/X_test_M.npy"
    Y_train_file = "./data/Y_test_M.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "M test", input_dim, output_dim

    sys.stderr.write("starting N train data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/N_train.fann"
    X_train_file = "./data/X_train_N.npy"
    Y_train_file = "./data/Y_train_N.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "N train", input_dim, output_dim
    sys.stderr.write("starting N test data...\n")
    input_train_file = "../../data/dense_predicted_fann/fanns/N_dev.fann"
    X_train_file = "./data/X_test_N.npy"
    Y_train_file = "./data/Y_test_N.npy"
    input_dim, output_dim = transform_fann(input_train_file, X_train_file, Y_train_file)
    print "N test", input_dim, output_dim

