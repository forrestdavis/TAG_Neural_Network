from keras.models import Sequential, model_from_json
from keras.layers import Dense, Activation, Dropout, Merge
from keras.callbacks import EarlyStopping
import numpy
import sys
import dimensions as d

class KerasModel:
    def __init__(self, data_directory):
        self.model = Sequential()
        self.dim_file = data_directory + "/" + "io_dimensions_1000.txt"
        
    def train(self):
        #Train model on data
        #Get dimensions of data
        dimensions_dictionary = d.get_dimensions(self.dim_file)

        #Get train data
        train_data, Y_train, feats = d.getTrainData("data_1000/numpy_arrays")
        
        self.feats = feats

        self.model = d.createModel(dimensions_dictionary, feats)
    
        early_stopping = EarlyStopping(monitor='val_loss', 
                verbose = 1, patience=2)

        sys.stderr.write("fitting model...\n")
        self.model.fit(train_data, Y_train, callbacks=[early_stopping], 
            nb_epoch=2, verbose=1, batch_size=1000, validation_split=0.1)
        
    #Need to update predict
    def predict(self, fann_file, fm_file):
        sys.stderr.write("getting prediction from data...\n")

        prediction = self.model.predict_on_batch([A_test, B_test, C_test, D_test, E_test, 
        F_test, G_test, H_test, I_test, J_test, K_test, L_test, M_test, N_test, O_test, P_test, 
        Q_test, R_test, S_test, T_test, U_test])

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

    def save(self):
        sys.stderr.write("saving model...\n")
        model_json = self.model.to_json()
        with open("trained_model.json", "w") as json_file:
            json_file.write(model_json)
        self.model.save_weights("trained_model_weights.h5")
        d.saveFeats(self.feats, "trained_model_feats.txt")

    def load(self):
        #Load model from saved arch, weights, and features used
        sys.stderr.write("loading model...\n")
        model_arch = "trained_model.json"
        model_weights = "trained_model_weights.h5"
        self.feats = d.loadFeats("trained_model_feats.txt")
        self.model = model_from_json(open(model_arch).read())
        self.model.load_weights(model_weights)
        self.model.compile(loss='categorical_crossentropy', 
                optimizer='adam', metrics=['accuracy'])

    def evaluate(self):
        #Evaluate test data on model
        sys.stderr.write("evaluating model on test data...\n")
        #Get test data
        test_data, Y_test, feats = d.getTestData("data_1000/numpy_arrays")

        #need to arrange test_data to fit train data form
        test_data = d.arrangeData(test_data, self.feats, feats)

        scores = self.model.evaluate(test_data, Y_test)
        print("%s: %.2f%%" % (self.model.metrics_names[1], scores[1]*100))

if __name__ == "__main__":
    model = KerasModel("data_1000")
    #model.train()
    #model.save()
    model.load()
    model.evaluate()
