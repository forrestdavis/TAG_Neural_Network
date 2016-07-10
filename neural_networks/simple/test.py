from keras.models import Sequential
from keras.layers import Dense
import numpy
import transform_fann

#Fix random to ensure consistent results during testing
seed = 7
numpy.random.seed(seed)

#Transform fann file into numpy arrays for input and output 
input_dimensions, output_dimensions, X, Y = transform_fann.transform_fann('../../data/train.fann')

test_input_dimensions, test_output_dimensions, test_X, test_Y = transform_fann.transform_fann('../../data/test.fann')
#Create model
model = Sequential()
model.add(Dense(400, input_dim=input_dimensions, init='uniform', activation='relu'))
model.add(Dense(250, input_dim=input_dimensions, activation='relu'))
model.add(Dense(200, input_dim=input_dimensions, activation='relu'))
model.add(Dense(150, input_dim=input_dimensions, activation='relu'))
model.add(Dense(output_dimensions, input_dim=input_dimensions, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, Y, nb_epoch=50, batch_size=10)

scores = model.evaluate(test_X, test_Y)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
'''
dataset = numpy.loadtxt("pima-indians-diabetes.data.csv", delimiter=",")
# split into input (X) and output (Y)
X = dataset[:,0:8]
Y = dataset[:,8] 

#create model
model = Sequential()
model.add(Dense(12, input_dim=8, init='uniform', activation='relu'))
model.add(Dense(8, init='uniform', activation='relu'))
model.add(Dense(1, init='uniform', activation='sigmoid'))

#compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

#fit the model
model.fit(X, Y, nb_epoch=150, batch_size=10)

#evaluate the model
scores = model.evaluate(X, Y)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
'''
