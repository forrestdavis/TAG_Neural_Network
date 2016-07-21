#!/bin/bash

echo "50 sigmoid"
python allFeatures_model.py 2 50 sigmoid 

echo "100 sigmoid"
python allFeatures_model.py 2 100 sigmoid 

echo "150 sigmoid"
python allFeatures_model.py 2 150 sigmoid

echo "200 sigmoid"
python allFeatures_model.py 2 200 sigmoid

echo "300 sigmoid"
python allFeatures_model.py 2 300 sigmoid

echo "400 sigmoid"
python allFeatures_model.py 2 400 sigmoid
