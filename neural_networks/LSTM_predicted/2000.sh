#!/bin/bash

echo "Creating data..."

python transform_fann_2000.py > io_dimensions_train_2000.txt

echo "Creating model..."

echo "2000"

python model_total_2000.py
