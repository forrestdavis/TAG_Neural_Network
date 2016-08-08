all: A-F G-N O-U pos form model

1000: A-F_1000 G-N_1000 O_U_1000 pos_1000 form_1000 model_1000

data: A-F G-N O-U

io_file = ./data/io_dimensions.txt

io_file_1000 = ./data_1000/io_dimensions_1000.txt

A-F: 
	python transform_fann_A-F.py > $(io_file)

G-N: 
	python transform_fann_G-N.py >> $(io_file)

O-U: 
	python transform_fann_O-U.py >> $(io_file)
	
pos: 
	python transform_fann_pos.py >> $(io_file)

form: 
	python transform_fann_form.py >> $(io_file)

A-F_1000: 
	python 1000_transform_fann_A-F.py > $(io_file_1000)

G-N_1000: 
	python 1000_transform_fann_G-N.py >> $(io_file_1000)

O-U_1000: 
	python 1000_transform_fann_O-U.py >> $(io_file_1000)

pos_1000: 
	python 1000_transform_fann_pos.py >> $(io_file_1000)

form_1000: 
	python 1000_transform_fann_form.py >> $(io_file_1000)

model:
	python model_total.py

model_1000:
	python model_total_1000.py

clean:
	-rm ./data/io_dimensions.txt
	-rm ./data_1000/io_dimensions_1000.txt
	-rm ./data/*.npy
	-rm ./data_1000/*.npy
