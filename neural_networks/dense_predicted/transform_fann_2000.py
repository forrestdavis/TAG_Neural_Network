import numpy
import sys

def transform_fann(input_train_file, X_train_file, Y_train_file):
    train_fann = open(input_train_file, 'r')

    info = train_fann.readline().split()
    train_output_dimensions = int(info[2])
    print info[1], info[2]
    #Extract train
    x = []
    y = [] 
    x_tmp = [] 
    isInput = 1
    print "Getting lines..."
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

    #Save output
    print "Saving information..."
    numpy.save(X_train_file, X_train)
    numpy.save(Y_train_file, Y_train)

    #Close files
    train_fann.close()

if __name__ == "__main__":
    input_train_file = "../../data/dense_predicted_fann/2000.fann"
    X_train_file = "X_train_2000.npy"
    Y_train_file = "Y_train_2000.npy"
    transform_fann(input_train_file, X_train_file, Y_train_file)

