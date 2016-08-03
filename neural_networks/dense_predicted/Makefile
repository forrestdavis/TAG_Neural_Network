all: A-F G-N O-U model

1000: A-F_1000 G-N_1000 model_1000

data: A-F G-N O-U

A-F: 
	python transform_fann_A-F.py > io_dimensions.txt

G-N: 
	python transform_fann_G-N.py >> io_dimensions.txt

O-U: 
	python transform_fann_O-U.py >> io_dimensions.txt
	
A-F_1000: 
	python 1000_transform_fann_A-F.py > io_dimensions_1000.txt

G-N_1000: 
	python 1000_transform_fann_G-N.py >> io_dimensions_1000.txt

O-U_1000: 
	python 1000_transform_fann_O-U.py >> io_dimensions_1000.txt

model:
	python model_total.py

model_1000:
	python model_total_1000.py

clean:
	-rm io_dimensions.txt
	-rm io_dimensions_1000.txt
	-rm *.npy
	-rm *.json
	-rm *.h5
