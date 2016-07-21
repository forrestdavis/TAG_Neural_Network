#!/bin/bash

echo "Creating data..."

python transform_fann_all.py > io_dimensions_train_all.txt

echo "Creating model..."

echo "all"

python model_total_all.py
