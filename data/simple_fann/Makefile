all: test.fann dev.fann

test.fann:
	./test_fann.sh

dev.fann: test.fann
	./dev_fann.sh

clean:
	rm *.fann
	rm *.alpha
