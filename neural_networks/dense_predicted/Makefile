
1000_files = data_1000/X_train_A_1000.npy

$(1000_files): %.npy: fanns_1000/A.fann
	python ./scripts/1000_transform_fann.py A 

fanns_1000/A.fann:
	./fann_scripts_1000/A_train_fann.sh
	./fann_scripts_1000/A_dev_fann.sh
		
clean:
	-rm ./data/io_dimensions.txt
	-rm ./data_1000/io_dimensions_1000.txt
	-rm ./data/*.npy
	-rm ./data_1000/*.npy
