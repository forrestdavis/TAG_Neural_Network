all: train.fann dev.fann 

train.fann: new.fm new.mcd train_fann.sh
	./train_fann.sh

dev.fann: train.fann
	./dev_fann.sh

clean:
	rm *.fann
	rm *.alpha
