from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
import numpy
#import transform_fann

#Fix random to ensure consistent results during testing
seed = 4
numpy.random.seed(seed)

X_test = numpy.load("X_test.npy")
Y_test = numpy.load("Y_test.npy")

model = model_from_json(open('first_model_architecture.json').read())
model.load_weights('first_model_weights.h5')

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
#hist = model.fit(X_train, Y_train, nb_epoch=50, batch_size=10)

scores = model.evaluate(X_test, Y_test)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
