#!/bin/bash

echo "50 relu"
python allFeatures_model.py 2 50 relu

echo "100 relu"
python allFeatures_model.py 2 100 relu

echo "150 relu"
python allFeatures_model.py 2 150 relu

echo "200 relu"
python allFeatures_model.py 2 200 relu

echo "300 relu"
python allFeatures_model.py 2 300 relu

echo "400 relu"
python allFeatures_model.py 2 400 relu
