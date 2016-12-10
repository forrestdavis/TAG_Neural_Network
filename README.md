# TAG_neural_network

This is a Neural Network classifier for a dependency parser using trees from 
a tree adjoining grammar. The goal is to more accurately predict which
transition for a dependency parser to take, using supertag information as well as 
particualar lingusitic properties of the trees. 

The Neural Networks used are created using Keras, a python library for 
easy implementation of Neural Networks, run with Theano backend.

# Install
First clone repo:
```
git clone https://github.com/forrestdavis/TAG_Neural_Network.git
```
Then create data with supertags:
```
cd data/
make
```
Then create fann files and numpy arrays:
```
cd ../neural_networks/dense/(gold_data, predicted_data)
make
```

# Usage
The model used for the dependency parser was written to be as customizable as possible. 
There are a variety of flags available for main.py that can be seen by running:
```
python main.py -h
```
or 
```
python main.py --help
```

# Example
This will train and test a keras model on gold data with default values:
```
python main.py -D gold_data -M TRAIN TEST
```

# Additional Information
The parser directory does contain a makefile that will run a parse. However the code for the parse is not public domain at this moment so I am not able to include it. 

# Thanks
I would like to thank Dr. Owen Rambow and Dr. Alexis Nasr for allowing me to work with them on this project. 
