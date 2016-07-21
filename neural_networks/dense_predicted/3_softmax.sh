#!/bin/bash

echo "50 softmax"
python allFeatures_model.py 3 50 softmax 

echo "100 softmax"
python allFeatures_model.py 3 100 softmax 

echo "150 softmax"
python allFeatures_model.py 3 150 softmax 

echo "200 softmax"
python allFeatures_model.py 3 200 softmax 

echo "300 softmax"
python allFeatures_model.py 3 300 softmax 

echo "400 softmax"
python allFeatures_model.py 3 400 softmax 
