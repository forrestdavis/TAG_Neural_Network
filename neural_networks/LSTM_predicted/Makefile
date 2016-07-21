train = ../../data/dense_predicted_fann/predicted_train_5000.fann

all: fann2csv_train model_total

fann2csv_train: $(train)
	perl fann2csv_train_5000.pl $(train)
	
model_total: $(fann2csv_train) $(fann2csv_test)
	python model_total.py

clean:
	-rm io_dimensions_*
	-rm *.csv
	-rm *.json
	-rm *.h5
