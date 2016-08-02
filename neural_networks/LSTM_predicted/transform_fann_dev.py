import numpy
from collections import deque
import sys

def transform_fann(input_train_file, X_train_file, Y_train_file):
    train_fann = open(input_train_file, 'r')

    info = train_fann.readline().split()
    train_output_dimensions = int(info[2])
    input_length = int(info[1])
    output_length = int(info[2])

    #Extract train

    #Set maximum length of transitions to 167
    #This captures all but 14 sentences in the data
    MAX_LENGTH = 167

    x = deque()
    y = deque() 
    x_tmp = []
    isInput = 1
    inSentence = 0
    sentence_x = deque()
    nb_mvts = 0
    nb_samples = 0
    sys.stderr.write("Getting lines...\n")
    for line in train_fann:
        if "start sentence" in line:
            inSentence = 1
	    sentence_x = deque()
        elif "end sentence" in line:
            nb_samples +=1
            if nb_mvts <= MAX_LENGTH:
                pad_number = MAX_LENGTH - nb_mvts
                pad_x = [0]*input_length
                pad_y = [0]*output_length
                for z in xrange(pad_number):
                    sentence_x.appendleft(pad_x)
                    y.appendleft(pad_y)
                x.append(sentence_x)
            nb_mvts = 0
            inSentence = 0
        elif inSentence:
            line = line.split()
            line = map(float, line)
            if len(line) != train_output_dimensions and len(line) != 0:
                x_tmp += line
            elif len(line) == train_output_dimensions:
		nb_mvts += 1
		y.append(line)
		sentence_x.append(x_tmp)
		x_tmp = [] 
            
    X_train = numpy.array(x)
    Y_train = numpy.array(y)

    #Save output
    sys.stderr.write("Saving information...\n")
    numpy.save(X_train_file, X_train)
    numpy.save(Y_train_file, Y_train)

    print nb_samples, MAX_LENGTH, input_length

    #Close files
    train_fann.close()

if __name__ == "__main__":
    input_train_file = "../../data/LSTM_predicted_fann/lstm_dev.fann"
    X_train_file = "X_train_dev.npy"
    Y_train_file = "Y_train_dev.npy"
    transform_fann(input_train_file, X_train_file, Y_train_file)

