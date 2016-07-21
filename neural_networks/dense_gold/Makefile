train = ../../data/dense_gold_fann/gold_train.fann
dev = ../../data/dense_gold_fann/gold_dev.fann

all: fann2csv_train fann2csv_test model_total

fann2csv_train: $(train)
	perl fann2csv_train.pl $(train) > io_dimensions_train.txt
	
fann2csv_test: 
	perl fann2csv_test.pl $(dev) > io_dimensions_test.txt

model_total: $(fann2csv_train) $(fann2csv_test)
	python model_total.py

clean:
	-rm io_dimensions_*
	-rm *.csv
	-rm *.json
	-rm *.h5
