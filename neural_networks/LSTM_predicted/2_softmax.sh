#!/bin/bash

echo "50 softmax"
python allFeatures_model.py 2 50 softmax 

echo "100 softmax"
python allFeatures_model.py 2 100 softmax 

echo "150 softmax"
python allFeatures_model.py 2 150 softmax 

echo "200 softmax"
python allFeatures_model.py 2 200 softmax 

echo "300 softmax"
python allFeatures_model.py 2 300 softmax 

echo "400 softmax"
python allFeatures_model.py 2 400 softmax 
