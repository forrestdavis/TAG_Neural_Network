#############################################################################
#Functions for getting and error checking dimensions from output file of INSERT GET DATA FUNCTION
#
#
#Forrest Davis
#August 11, 2016
#############################################################################

#Gets dimensions information from io file output of INSERT GET DATA
#Returns a dictionary of dictionaries where each element is formated:
# {X: {test or train: (input dimensions, output dimensions)} where X is
# a feature
def get_dimensions(dimensions_filename):

    dimensions_file = open(dimensions_filename, "r")
    d = {}

    for line in dimensions_file:
        line = line.strip('\n')
        line = line.split()
        feat = line[0]
        type_data = line[1]
        input_value_data = int(line[2])
        output_value_data = int(line[3])
        if feat not in d:
            d[feat] = {}
            d[feat][type_data] = (input_value_data, output_value_data)
        else:
            d[feat][type_data] = (input_value_data, output_value_data)
    dimensions_file.close()
    return d

#Ensures that data dimensions is same for test and train
def error_check_dimensions(dimensions_dictionary):
    d = dimensions_dictionary
    for key in d:
        input_values = [] 
        output_values = []
        for subkey in d[key]:
            input_values.append(d[key][subkey][0])
            output_values.append(d[key][subkey][1])
        assert input_values[0] == input_values[1], ( 
        "There is a mismatch in %s train and test data input dimensions" % key)
        assert output_values[0] == output_values[1], ( 
        "There is a mismatch in %s train and test data output dimensions" % key)
