all: A-F G-N O-U model_total

data: A-F G-N O-U

A-F: 
	python transform_fann_A-F.py > io_dimensions.txt

G-N: 
	python transform_fann_G-N.py >> io_dimensions.txt

O-U: 
	python transform_fann_O-U.py >> io_dimensions.txt
	
model_total:
	python model_total_A.py

clean:
	-rm io_dimensions.txt
	-rm *.npy
	-rm *.json
	-rm *.h5
