import numpy

def transform_fann(file_name):
    fann = open(file_name, 'r')

    info = fann.readline().split()
    input_dimensions = int(info[1])
    output_dimensions = int(info[2])

    x = []
    y = [] 
    x_tmp = [] 
    isInput = 1
    for line in fann:
        line = line.split()
        line = map(float, line)
        if len(line) != output_dimensions and len(line) != 0:
            x_tmp += line
        elif len(line) == output_dimensions:
            y.append(line)
            x.append(x_tmp)
            x_tmp = []
            
    X = numpy.array(x)
    Y = numpy.array(y)

    fann.close()
    return input_dimensions, output_dimensions, X, Y

