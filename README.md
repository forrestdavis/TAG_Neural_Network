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
cd ../neural_networks/dense/(gold_data, gold_data_1000, predicted_data, predicted_data_1000)
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
This will train and test a keras model on the smallest data set:
```
python main.py -D gold_data_1000 -M TRAIN TEST
```

# Additional Information
Work in progress...
