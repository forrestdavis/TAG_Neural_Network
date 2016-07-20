from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
from keras.utils.visualize_util import plot

model = model_from_json(open('150_model_architecture.json').read())
model.load_weights('150_model_weights.h5')

model.compile(loss='categorical_crossentropy', 
        optimizer='adam', metrics=['accuracy'])

plot(model, to_file='model.png', show_shapes=True)
