train = d6.train.conll07
dev = d6.dev.conll07
test = d6.test.conll07
predicted_train = d6.predicted_train.conll07
predicted_dev = d6.predicted_dev.conll07
treeproperties = d6.treeproperties

all: d6.treeproperties d6.dev.conll16 d6.train.conll16 d6.predicted_train.conll16 d6.predicted_dev.conll16

d6.treeproperties: ./tools/feature_extractor.py
	python ./tools/feature_extractor.py d6.grammar.str d6.treeproperties

d6.dev.conll16: ./tools/create_conll16.py $(treeproperties)
	python ./tools/create_conll16.py $(treeproperties) $(dev) $@

d6.train.conll16: ./tools/create_conll16.py $(treeproperties)
	python ./tools/create_conll16.py $(treeproperties) $(train) $@

d6.predicted_train.conll16: ./tools/create_conll16.py $(treeproperties)
	python ./tools/create_conll16.py $(treeproperties) $(predicted_train) $@

d6.predicted_dev.conll16: ./tools/create_conll16.py $(treeproperties)
	python ./tools/create_conll16.py $(treeproperties) $(predicted_dev) $@

clean:
	- rm *.conll16
	- rm d6.treeproperties
