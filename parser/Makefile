#data = ../data/d6.dev.conll16
#data = ../data/d6.predicted_dev.conll16
#data = reduced_dev.conll16
data = ../data/d6.red_pred_train.conl116
ref = ../data/d6.dev.conll07

mcd = dimensions.mcd

fm = parser.fm

vocab = test.alpha

parse:
	maca_trans_parser_forrest -i $(data) -C $(mcd) -F $(fm) -V $(vocab)

eval:
	python conll162conll07.py parse hyp
	perl eval07.pl $(ref) hyp > res

clean:
	-rm mvt.txt
	-rm parse
	-rm hyp
	-rm res
