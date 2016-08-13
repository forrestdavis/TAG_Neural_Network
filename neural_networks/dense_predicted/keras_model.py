from keras.models import Sequential, model_from_json
from keras.layers import Dense, Activation, Dropout, Merge
from keras.callbacks import EarlyStopping
import numpy
import sys
import dimensions as d

class KerasModel:
    def __init__(self, data_directory):
        dimensions_filename = data_directory + "/" + "io_dimensions.txt"
        dimensions_dictionary = d.get_dimensions(
                dimensions_filename)
        d.error_check_dimensions(dimensions_dictionary)
        print dimensions_dictionary
        

    '''
    def train():
        tri
    
    def predict():
        fj

    def save():
        fjf

    def load():
        fjfj

    def evaluate():
        alal
    
    '''


if __name__ == "__main__":
    model = KerasModel("data")
