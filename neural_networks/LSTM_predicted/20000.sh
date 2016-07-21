#!/bin/bash

echo "Creating data..."

python transform_fann_20000.py > io_dimensions_train_20000.txt

echo "Creating model..."

echo "20000"

python model_total_20000.py
