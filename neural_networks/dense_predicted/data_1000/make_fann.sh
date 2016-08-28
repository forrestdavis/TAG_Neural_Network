#!/bin/bash
# This script takes 7 command line inputs that correspond to flags for maca_trans_parser_conll2fann. 
# The first is for TRAIN or TEST mode. 
# The second is the data file. 
# The third is the name of the fann file for output. 
# The fourth is the vocab file name. 
# The fifth is the featurn model file name.
# The sixth is the mulit column description file name. 
# The seventh is the number of sentences from the data, with 'all' corresponding to the whole data set.

mode=$1
data=$2
fann=$3
alpha=$4
fm=$5
mcd=$6
numSent=$7
echo numSent

if [ $numSent = 'all' ]; then 

    maca_trans_parser_conll2fann -M $mode -i $data -f $fann -V $alpha -F $fm -C $mcd

else

    maca_trans_parser_conll2fann -M $mode -i $data -f $fann -V $alpha -F $fm -C $mcd -s $numSent

fi
