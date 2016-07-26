all: predicted_train.fann predicted_dev.fann

predicted_train.fann: new.fm new.mcd predicted_train_fann.sh
	./predicted_train_fann.sh

predicted_dev.fann: predicted_train.fann
	./predicted_dev_fann.sh

clean:
	rm *.fann
	rm *.alpha
