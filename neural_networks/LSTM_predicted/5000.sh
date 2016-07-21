#!/bin/bash

echo "Creating data..."

python transform_fann_5000.py > io_dimensions_train_5000.txt

echo "Creating model..."

echo "5000"

python model_total_5000.py
