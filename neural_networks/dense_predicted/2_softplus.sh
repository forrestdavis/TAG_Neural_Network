#!/bin/bash

echo "50 softplus"
python allFeatures_model.py 2 50 softplus 

echo "100 softplus"
python allFeatures_model.py 2 100 softplus 

echo "150 softplus"
python allFeatures_model.py 2 150 softplus

echo "200 softplus"
python allFeatures_model.py 2 200 softplus

echo "300 softplus"
python allFeatures_model.py 2 300 softplus

echo "400 softplus"
python allFeatures_model.py 2 400 softplus
