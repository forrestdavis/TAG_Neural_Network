#!/bin/bash

echo "Creating data..."

python transform_fann_10000.py > io_dimensions_train_10000.txt

echo "Creating model..."

echo "10000"

python model_total_10000.py
