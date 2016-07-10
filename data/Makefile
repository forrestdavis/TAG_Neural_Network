train = d6.train.conll07
dev = d6.dev.conll07
treeproperties = d6.treeproperties

all: d6.treeproperties d6.dev.conll16 d6.train.conll16

d6.treeproperties:
	python ../tools/feature_extractor.py d6.grammar.str d6.treeproperties

d6.dev.conll16:
	python ../tools/create_conll16.py $(treeproperties) $(dev) $@

d6.train.conll16:
	python ../tools/create_conll16.py $(treeproperties) $(train) $@

clean:
	- rm d6.dev.conll16
	- rm d6.train.conll16
	- rm d6.treeproperties
