from keras.models import Sequential, model_from_json
from keras.layers import Dense, Activation, Dropout, Merge
from keras.callbacks import EarlyStopping
from keras.utils.visualize_util import plot
import numpy
import sys
import argparse
import os
import model_framework as mf 

class KerasModel:
    def __init__(self, data_directory, verbose=False):
        #Get io file
        dim_file = ""
        if data_directory[len(data_directory)-1] != "/":
            data_directory = data_directory+"/"
            
        for filename in os.listdir(data_directory):
            if "io_" in filename:
                dim_file = data_directory+filename
        if not dim_file:
            sys.stderr.write("There must be a file with the dimensions "
                    +"of the data, file name must contain 'io'\n")
            sys.exit(1)

        self.model = Sequential()
        self.dim_file = dim_file
        self.data_dir = data_directory
        self.v = verbose
        
    def train(self, find_feats, nb_layers=None, activation_functs=None,
            nodes=None, merge_nb_layers=None,
            merge_activation_functs=None, merge_nodes=None,
            nb_epochs=None, early_stop=False):
        #Train model on data
        #Get dimensions of data
        dimensions_dictionary = mf.get_dimensions(self.dim_file)
        array_location = self.data_dir+"numpy_arrays"

        #set defaults
        if nb_layers==None:
            nb_layers=2
        if activation_functs==None:
            activation_functs=['relu']
        if nodes==None:
            nodes=[50]

        if merge_nb_layers==None:
            merge_nb_layers=0
        if merge_activation_functs==None:
            merge_activation_functs=['relu']
        if merge_nodes==None:
            merge_nodes=[50]

        if nb_epochs == None:
            nb_epochs = 50

        #Get train data
        if find_feats:
            train_data, Y_train, feats = mf.getTrainData(
                    array_location, self.v, find_feats)
        else:
            train_data, Y_train, feats = mf.getTrainData(
                    array_location, self.v)
        
        self.feats = feats

        self.model = mf.createModel(dimensions_dictionary, feats, self.v,
                nb_layers, activation_functs, nodes, merge_nb_layers,
                merge_activation_functs, merge_nodes)
    
        early_stopping = EarlyStopping(monitor='val_loss', 
                verbose = 1, patience=2)

        if self.v:
            sys.stderr.write("fitting model...\n")
        
        if early_stop:
            self.model.fit(train_data, Y_train, callbacks=[early_stopping], 
                nb_epoch=nb_epochs, verbose=self.v, batch_size=1000, validation_split=0.1)
        else:
            self.model.fit(train_data, Y_train, 
                nb_epoch=nb_epochs, verbose=self.v, batch_size=1000, validation_split=0.1)
        
    #Need to update predict
    def predict(self, fann_file, fm_file):
        if self.v:
            sys.stderr.write("getting prediction from data...\n")

        #Get prediction data
        prediction_data, feats = mf.getPredictionData(fann_file, 
                fm_file, self.dim_file, self.v)

        #need to arrange prediction_data to fit train data form
        prediction_data = mf.arrangeData(prediction_data, 
                self.feats, feats)

        prediction = self.model.predict_on_batch(prediction_data)

        #Transform prediction from one-hot to int
        max_pos = -1
        max_value = 0.0
        #Location with largest probability is 1 in one-hot encoding
        for i in xrange(len(prediction[0])):
            if max_value < float(prediction[0][i]):
                max_value = float(prediction[0][i])
                max_pos = i
        mvt = max_pos
        if mvt >= 0:
            return mvt
        else:
            return "ERROR"

    def save(self, filename):
        if self.v:
            sys.stderr.write("saving model...\n")
        saved_directory = "saved_models/"
        if not filename:
            filename = "trained_model"
        saved_file = saved_directory+filename
        model_json = self.model.to_json()
        with open(saved_file+".json", "w") as json_file:
            json_file.write(model_json)
        self.model.save_weights(saved_file+"_weights.h5", 
                overwrite=True)
        mf.saveFeats(self.feats, saved_file+"_feats.txt")

    def load(self, filename):
        #Load model from saved arch, weights, and features used
        if self.v:
            sys.stderr.write("loading model...\n")
        saved_directory = "./"
        if not filename:
            filename="trained_model"
        saved_file = saved_directory+filename
        model_arch = saved_file+".json"
        model_weights = saved_file+"_weights.h5"
        self.feats = mf.loadFeats(saved_file+"_feats.txt")
        self.model = model_from_json(open(model_arch).read())
        self.model.load_weights(model_weights)
        self.model.compile(loss='categorical_crossentropy', 
                optimizer='adam', metrics=['accuracy'])

    def evaluate(self):
        #Evaluate test data on model
        if self.v:
            sys.stderr.write("evaluating model on test data...\n")
        #Get test data
        array_location = self.data_dir+"numpy_arrays"
        test_data, Y_test, feats = mf.getTestData(array_location, self.v)

        #need to arrange test_data to fit train data form
        test_data = mf.arrangeData(test_data, self.feats, feats)

        scores = self.model.evaluate(test_data, Y_test, verbose=self.v)
        print("%s: %.2f%%" % (self.model.metrics_names[1], scores[1]*100))

    def graph(self, filename):
        if not filename:
            filename = "graph_model.png"
        if self.v:
            sys.stderr.write("graphing model...\n")
        plot(self.model, filename, show_shapes=True)
