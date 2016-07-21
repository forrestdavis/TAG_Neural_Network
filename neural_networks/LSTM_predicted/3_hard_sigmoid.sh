#!/bin/bash

echo "50 hard_sigmoid"
python allFeatures_model.py 3 50 hard_sigmoid 

echo "100 hard_sigmoid"
python allFeatures_model.py 3 100 hard_sigmoid 

echo "150 hard_sigmoid"
python allFeatures_model.py 3 150 hard_sigmoid

echo "200 hard_sigmoid"
python allFeatures_model.py 3 200 hard_sigmoid

echo "300 hard_sigmoid"
python allFeatures_model.py 3 300 hard_sigmoid

echo "400 hard_sigmoid"
python allFeatures_model.py 3 400 hard_sigmoid
