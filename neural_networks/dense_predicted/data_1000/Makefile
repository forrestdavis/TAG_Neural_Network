CC = gcc

CFLAGS = -g -Wall

all: train test

train: all_fann_train all_numpy_train

test: all_fann_dev all_numpy_test

all_numpy_train: numpy_arrays/X_train_A.npy numpy_arrays/X_train_B.npy numpy_arrays/X_train_C.npy numpy_arrays/X_train_D.npy numpy_arrays/X_train_E.npy numpy_arrays/X_train_F.npy numpy_arrays/X_train_G.npy numpy_arrays/X_train_H.npy numpy_arrays/X_train_I.npy numpy_arrays/X_train_J.npy numpy_arrays/X_train_K.npy numpy_arrays/X_train_L.npy numpy_arrays/X_train_M.npy numpy_arrays/X_train_N.npy numpy_arrays/X_train_O.npy numpy_arrays/X_train_P.npy numpy_arrays/X_train_Q.npy numpy_arrays/X_train_R.npy numpy_arrays/X_train_S.npy numpy_arrays/X_train_T.npy numpy_arrays/X_train_U.npy

#Deleted F and G need to readd
all_numpy_test: numpy_arrays/X_test_A.npy numpy_arrays/X_test_B.npy numpy_arrays/X_test_C.npy numpy_arrays/X_test_D.npy numpy_arrays/X_test_E.npy numpy_arrays/X_test_H.npy numpy_arrays/X_test_I.npy numpy_arrays/X_test_J.npy numpy_arrays/X_test_K.npy numpy_arrays/X_test_L.npy numpy_arrays/X_test_M.npy numpy_arrays/X_test_N.npy numpy_arrays/X_test_O.npy numpy_arrays/X_test_P.npy numpy_arrays/X_test_Q.npy numpy_arrays/X_test_R.npy numpy_arrays/X_test_S.npy numpy_arrays/X_test_T.npy numpy_arrays/X_test_U.npy

all_fann_train: fanns/A_train.fann fanns/B_train.fann fanns/C_train.fann fanns/D_train.fann fanns/E_train.fann fanns/F_train.fann fanns/G_train.fann fanns/H_train.fann fanns/I_train.fann fanns/J_train.fann fanns/K_train.fann fanns/L_train.fann fanns/M_train.fann fanns/N_train.fann fanns/O_train.fann fanns/P_train.fann fanns/Q_train.fann fanns/R_train.fann fanns/S_train.fann fanns/T_train.fann fanns/U_train.fann

all_fann_dev: fanns/A_dev.fann fanns/B_dev.fann fanns/C_dev.fann fanns/D_dev.fann fanns/E_dev.fann fanns/F_dev.fann fanns/G_dev.fann fanns/H_dev.fann fanns/I_dev.fann fanns/J_dev.fann fanns/K_dev.fann fanns/L_dev.fann fanns/M_dev.fann fanns/N_dev.fann fanns/O_dev.fann fanns/P_dev.fann fanns/Q_dev.fann fanns/R_dev.fann fanns/S_dev.fann fanns/T_dev.fann fanns/U_dev.fann

train_data = ../../../data/d6.predicted_train.conll16

dev_data = ../../../data/d6.predicted_dev.conll16

#Makefile commands for generating fann2binary exe
fann2binary: fann2binary.o

fann2binary.o: fann2binary.c

#Need to fix io file to a set io file thing
binary_fanns/U_train_input.bin: fann2binary fanns/U_train.fann
	./fann2binary fanns/U_train.fann fms/U.fm binary_fanns/U_train_input.bin binary_fanns/U_train_output.bin io.txt

numpy_arrays/X_train_U.npy: load_fann_bin.py binary_fanns/U_train_input.bin binary_fanns/U_train_output.bin
	python load_fann_bin.py U TRAIN io.txt binary_fanns/U_train_input.bin binary_fanns/U_train_output.bin

binary_fanns/U_test_input.bin: fann2binary fanns/U_dev.fann
	./fann2binary fanns/U_dev.fann fms/U.fm binary_fanns/U_test_input.bin binary_fanns/U_test_output.bin io.txt

numpy_arrays/X_test_U.npy: load_fann_bin.py binary_fanns/U_test_input.bin binary_fanns/U_test_output.bin
	python load_fann_bin.py U TEST io.txt binary_fanns/U_test_input.bin binary_fanns/U_test_output.bin

#Makefile commands for generating fann files from train fann files
numpy_arrays/X_train_A.npy: fanns/A_train.fann
	python ../scripts/general.py TRAIN fanns/A_train.fann fms/A.fm io_dimensions_1000.txt 

numpy_arrays/X_train_B.npy: fanns/B_train.fann
	python ../scripts/general.py TRAIN fanns/B_train.fann fms/B.fm io_dimensions_1000.txt 

numpy_arrays/X_train_C.npy: fanns/C_train.fann
	python ../scripts/general.py TRAIN fanns/C_train.fann fms/C.fm io_dimensions_1000.txt 

numpy_arrays/X_train_D.npy: fanns/D_train.fann
	python ../scripts/general.py TRAIN fanns/D_train.fann fms/D.fm io_dimensions_1000.txt 

numpy_arrays/X_train_E.npy: fanns/E_train.fann
	python ../scripts/general.py TRAIN fanns/E_train.fann fms/E.fm io_dimensions_1000.txt 

numpy_arrays/X_train_F.npy: fanns/F_train.fann
	python ../scripts/general.py TRAIN fanns/F_train.fann fms/F.fm io_dimensions_1000.txt 

numpy_arrays/X_train_G.npy: fanns/G_train.fann
	python ../scripts/general.py TRAIN fanns/G_train.fann fms/G.fm io_dimensions_1000.txt 

numpy_arrays/X_train_H.npy: fanns/H_train.fann
	python ../scripts/general.py TRAIN fanns/H_train.fann fms/H.fm io_dimensions_1000.txt 

numpy_arrays/X_train_I.npy: fanns/I_train.fann
	python ../scripts/general.py TRAIN fanns/I_train.fann fms/I.fm io_dimensions_1000.txt 

numpy_arrays/X_train_J.npy: fanns/J_train.fann
	python ../scripts/general.py TRAIN fanns/J_train.fann fms/J.fm io_dimensions_1000.txt 

numpy_arrays/X_train_K.npy: fanns/K_train.fann
	python ../scripts/general.py TRAIN fanns/K_train.fann fms/K.fm io_dimensions_1000.txt 

numpy_arrays/X_train_L.npy: fanns/L_train.fann
	python ../scripts/general.py TRAIN fanns/L_train.fann fms/L.fm io_dimensions_1000.txt 

numpy_arrays/X_train_M.npy: fanns/M_train.fann
	python ../scripts/general.py TRAIN fanns/M_train.fann fms/M.fm io_dimensions_1000.txt 

numpy_arrays/X_train_N.npy: fanns/N_train.fann
	python ../scripts/general.py TRAIN fanns/N_train.fann fms/N.fm io_dimensions_1000.txt 

numpy_arrays/X_train_O.npy: fanns/O_train.fann
	python ../scripts/general.py TRAIN fanns/O_train.fann fms/O.fm io_dimensions_1000.txt 

numpy_arrays/X_train_P.npy: fanns/P_train.fann
	python ../scripts/general.py TRAIN fanns/P_train.fann fms/P.fm io_dimensions_1000.txt 

numpy_arrays/X_train_Q.npy: fanns/Q_train.fann
	python ../scripts/general.py TRAIN fanns/Q_train.fann fms/Q.fm io_dimensions_1000.txt 

numpy_arrays/X_train_R.npy: fanns/R_train.fann
	python ../scripts/general.py TRAIN fanns/R_train.fann fms/R.fm io_dimensions_1000.txt 

numpy_arrays/X_train_S.npy: fanns/S_train.fann
	python ../scripts/general.py TRAIN fanns/S_train.fann fms/S.fm io_dimensions_1000.txt 

numpy_arrays/X_train_T.npy: fanns/T_train.fann
	python ../scripts/general.py TRAIN fanns/T_train.fann fms/T.fm io_dimensions_1000.txt 

#numpy_arrays/X_train_U.npy: fanns/U_train.fann fann2binary
	#python ../scripts/general.py TRAIN fanns/U_train.fann fms/U.fm io_dimensions_1000.txt 

#Makefile commands for generating fann files from dev fann files
numpy_arrays/X_test_A.npy: fanns/A_dev.fann
	python ../scripts/general.py TEST fanns/A_dev.fann fms/A.fm io_dimensions_1000.txt

numpy_arrays/X_test_B.npy: fanns/B_dev.fann
	python ../scripts/general.py TEST fanns/B_dev.fann fms/B.fm io_dimensions_1000.txt

numpy_arrays/X_test_C.npy: fanns/C_dev.fann
	python ../scripts/general.py TEST fanns/C_dev.fann fms/C.fm io_dimensions_1000.txt

numpy_arrays/X_test_D.npy: fanns/D_dev.fann
	python ../scripts/general.py TEST fanns/D_dev.fann fms/D.fm io_dimensions_1000.txt

numpy_arrays/X_test_E.npy: fanns/E_dev.fann
	python ../scripts/general.py TEST fanns/E_dev.fann fms/E.fm io_dimensions_1000.txt

numpy_arrays/X_test_F.npy: fanns/F_dev.fann
	python ../scripts/general.py TEST fanns/F_dev.fann fms/F.fm io_dimensions_1000.txt

numpy_arrays/X_test_G.npy: fanns/G_dev.fann
	python ../scripts/general.py TEST fanns/G_dev.fann fms/G.fm io_dimensions_1000.txt

numpy_arrays/X_test_H.npy: fanns/H_dev.fann
	python ../scripts/general.py TEST fanns/H_dev.fann fms/H.fm io_dimensions_1000.txt

numpy_arrays/X_test_I.npy: fanns/I_dev.fann
	python ../scripts/general.py TEST fanns/I_dev.fann fms/I.fm io_dimensions_1000.txt

numpy_arrays/X_test_J.npy: fanns/J_dev.fann
	python ../scripts/general.py TEST fanns/J_dev.fann fms/J.fm io_dimensions_1000.txt

numpy_arrays/X_test_K.npy: fanns/K_dev.fann
	python ../scripts/general.py TEST fanns/K_dev.fann fms/K.fm io_dimensions_1000.txt

numpy_arrays/X_test_L.npy: fanns/L_dev.fann
	python ../scripts/general.py TEST fanns/L_dev.fann fms/L.fm io_dimensions_1000.txt

numpy_arrays/X_test_M.npy: fanns/M_dev.fann
	python ../scripts/general.py TEST fanns/M_dev.fann fms/M.fm io_dimensions_1000.txt

numpy_arrays/X_test_N.npy: fanns/N_dev.fann
	python ../scripts/general.py TEST fanns/N_dev.fann fms/N.fm io_dimensions_1000.txt

numpy_arrays/X_test_O.npy: fanns/O_dev.fann
	python ../scripts/general.py TEST fanns/O_dev.fann fms/O.fm io_dimensions_1000.txt

numpy_arrays/X_test_P.npy: fanns/P_dev.fann
	python ../scripts/general.py TEST fanns/P_dev.fann fms/P.fm io_dimensions_1000.txt

numpy_arrays/X_test_Q.npy: fanns/Q_dev.fann
	python ../scripts/general.py TEST fanns/Q_dev.fann fms/Q.fm io_dimensions_1000.txt

numpy_arrays/X_test_R.npy: fanns/R_dev.fann
	python ../scripts/general.py TEST fanns/R_dev.fann fms/R.fm io_dimensions_1000.txt

numpy_arrays/X_test_S.npy: fanns/S_dev.fann
	python ../scripts/general.py TEST fanns/S_dev.fann fms/S.fm io_dimensions_1000.txt

numpy_arrays/X_test_T.npy: fanns/T_dev.fann
	python ../scripts/general.py TEST fanns/T_dev.fann fms/T.fm io_dimensions_1000.txt

#numpy_arrays/X_test_U.npy: fanns/U_dev.fann
	#python ../scripts/general.py TEST fanns/U_dev.fann fms/U.fm io_dimensions_1000.txt

#Makefile for generating fann train files
fanns/A_train.fann: fms/A.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/A_train.fann ./alphas/A.alpha ./fms/A.fm dimensions.mcd 1000

fanns/B_train.fann: fms/B.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/B_train.fann ./alphas/B.alpha ./fms/B.fm dimensions.mcd 1000

fanns/C_train.fann: fms/C.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/C_train.fann ./alphas/C.alpha ./fms/C.fm dimensions.mcd 1000

fanns/D_train.fann: fms/D.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/D_train.fann ./alphas/D.alpha ./fms/D.fm dimensions.mcd 1000

fanns/E_train.fann: fms/E.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/E_train.fann ./alphas/E.alpha ./fms/E.fm dimensions.mcd 1000

fanns/F_train.fann: fms/F.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/F_train.fann ./alphas/F.alpha ./fms/F.fm dimensions.mcd 1000

fanns/G_train.fann: fms/G.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/G_train.fann ./alphas/G.alpha ./fms/G.fm dimensions.mcd 1000

fanns/H_train.fann: fms/H.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/H_train.fann ./alphas/H.alpha ./fms/H.fm dimensions.mcd 1000

fanns/I_train.fann: fms/I.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/I_train.fann ./alphas/I.alpha ./fms/I.fm dimensions.mcd 1000

fanns/J_train.fann: fms/J.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/J_train.fann ./alphas/J.alpha ./fms/J.fm dimensions.mcd 1000

fanns/K_train.fann: fms/K.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/K_train.fann ./alphas/K.alpha ./fms/K.fm dimensions.mcd 1000

fanns/L_train.fann: fms/L.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/L_train.fann ./alphas/L.alpha ./fms/L.fm dimensions.mcd 1000

fanns/M_train.fann: fms/M.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/M_train.fann ./alphas/M.alpha ./fms/M.fm dimensions.mcd 1000

fanns/N_train.fann: fms/N.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/N_train.fann ./alphas/N.alpha ./fms/N.fm dimensions.mcd 1000

fanns/O_train.fann: fms/O.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/O_train.fann ./alphas/O.alpha ./fms/O.fm dimensions.mcd 1000

fanns/P_train.fann: fms/P.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/P_train.fann ./alphas/P.alpha ./fms/P.fm dimensions.mcd 1000

fanns/Q_train.fann: fms/Q.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/Q_train.fann ./alphas/Q.alpha ./fms/Q.fm dimensions.mcd 1000

fanns/R_train.fann: fms/R.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/R_train.fann ./alphas/R.alpha ./fms/R.fm dimensions.mcd 1000

fanns/S_train.fann: fms/S.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/S_train.fann ./alphas/S.alpha ./fms/S.fm dimensions.mcd 1000

fanns/T_train.fann: fms/T.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/T_train.fann ./alphas/T.alpha ./fms/T.fm dimensions.mcd 1000

fanns/U_train.fann: fms/U.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/U_train.fann ./alphas/U.alpha ./fms/U.fm dimensions.mcd 1000

#Makefile for generating fann test files
fanns/A_dev.fann: fms/A.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/A_dev.fann ./alphas/A.alpha ./fms/A.fm dimensions.mcd all

fanns/B_dev.fann: fms/B.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/B_dev.fann ./alphas/B.alpha ./fms/B.fm dimensions.mcd all

fanns/C_dev.fann: fms/C.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/C_dev.fann ./alphas/C.alpha ./fms/C.fm dimensions.mcd all

fanns/D_dev.fann: fms/D.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/D_dev.fann ./alphas/D.alpha ./fms/D.fm dimensions.mcd all

fanns/E_dev.fann: fms/E.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/E_dev.fann ./alphas/E.alpha ./fms/E.fm dimensions.mcd all

fanns/F_dev.fann: fms/F.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/F_dev.fann ./alphas/F.alpha ./fms/F.fm dimensions.mcd all

fanns/G_dev.fann: fms/G.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/G_dev.fann ./alphas/G.alpha ./fms/G.fm dimensions.mcd all

fanns/H_dev.fann: fms/H.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/H_dev.fann ./alphas/H.alpha ./fms/H.fm dimensions.mcd all

fanns/I_dev.fann: fms/I.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/I_dev.fann ./alphas/I.alpha ./fms/I.fm dimensions.mcd all

fanns/J_dev.fann: fms/J.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/J_dev.fann ./alphas/J.alpha ./fms/J.fm dimensions.mcd all

fanns/K_dev.fann: fms/K.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/K_dev.fann ./alphas/K.alpha ./fms/K.fm dimensions.mcd all

fanns/L_dev.fann: fms/L.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/L_dev.fann ./alphas/L.alpha ./fms/L.fm dimensions.mcd all

fanns/M_dev.fann: fms/M.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/M_dev.fann ./alphas/M.alpha ./fms/M.fm dimensions.mcd all

fanns/N_dev.fann: fms/N.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/N_dev.fann ./alphas/N.alpha ./fms/N.fm dimensions.mcd all

fanns/O_dev.fann: fms/O.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/O_dev.fann ./alphas/O.alpha ./fms/O.fm dimensions.mcd all

fanns/P_dev.fann: fms/P.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/P_dev.fann ./alphas/P.alpha ./fms/P.fm dimensions.mcd all

fanns/Q_dev.fann: fms/Q.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/Q_dev.fann ./alphas/Q.alpha ./fms/Q.fm dimensions.mcd all

fanns/R_dev.fann: fms/R.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/R_dev.fann ./alphas/R.alpha ./fms/R.fm dimensions.mcd all

fanns/S_dev.fann: fms/S.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/S_dev.fann ./alphas/S.alpha ./fms/S.fm dimensions.mcd all

fanns/T_dev.fann: fms/T.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/T_dev.fann ./alphas/T.alpha ./fms/T.fm dimensions.mcd all

fanns/U_dev.fann: fms/U.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/U_dev.fann ./alphas/U.alpha ./fms/U.fm dimensions.mcd all

.PHONY: clean
clean:
	- rm ./fanns/*.fann
	- rm ./numpy_arrays/*.npy
	- rm io_dimensions*
	- rm -f *.o a.out core fann2binary 
