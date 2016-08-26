mode=$1
fann=$2
alpha=$3
fm=$4
mcd=$5

(maca_trans_parser_conll2fann -M $mode -i ../../../data/d6.predicted_train.conll16 -f $fann -V $alpha -F $fm -C $mcd)
