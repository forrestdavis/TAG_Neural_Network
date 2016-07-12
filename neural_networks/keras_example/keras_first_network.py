from keras.models import Sequential
from keras.layers import Dense
import numpy

# fix random
seed = 7
numpy.random.seed(seed)

# load dataset
dataset = numpy.loadtxt("pima-indians-diabetes.data.csv", delimiter=",")
# split into input (X) and output (Y)
X = dataset[:,0:8]
Y = dataset[:,8] 
print Y[0]

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
