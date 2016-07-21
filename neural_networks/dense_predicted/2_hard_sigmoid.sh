#!/bin/bash

echo "50 hard_sigmoid"
python allFeatures_model.py 2 50 hard_sigmoid 

echo "100 hard_sigmoid"
python allFeatures_model.py 2 100 hard_sigmoid 

echo "150 hard_sigmoid"
python allFeatures_model.py 2 150 hard_sigmoid

echo "200 hard_sigmoid"
python allFeatures_model.py 2 200 hard_sigmoid

echo "300 hard_sigmoid"
python allFeatures_model.py 2 300 hard_sigmoid

echo "400 hard_sigmoid"
python allFeatures_model.py 2 400 hard_sigmoid
