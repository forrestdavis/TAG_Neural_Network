data = d6.predicted_dev.conll16
#data = reduced_dev.conll16

mcd = dimensions.mcd

fm = parser.fm

vocab = vocab.alpha

parse:
	maca_trans_parser_forrest -i $(data) -C $(mcd) -F $(fm) -V $(vocab)

clean:
	-rm output.txt
	-rm mvt.txt
