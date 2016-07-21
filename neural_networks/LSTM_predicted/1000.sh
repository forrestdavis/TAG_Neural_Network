#!/bin/bash

echo "Creating data..."

python transform_fann_1000.py > io_dimensions_train_1000.txt

echo "Creating model..."

echo "1000"

python model_total_1000.py
