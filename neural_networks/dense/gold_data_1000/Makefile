all: train test

numpy: all_numpy_train all_numpy_test

train: all_fann_train all_numpy_train

test: all_fann_dev all_numpy_test

CC = gcc

CFLAGS = -g -Wall

train_data = ../../../data/d6.train.conll16

dev_data = ../../../data/d6.dev.conll16

bin = binary_fanns

bin_info = binary_fanns_info

io = io_dimensions.txt

np = numpy_arrays

train_nb_sents = 1000

test_nb_sents = all

all_numpy_train: $(np)/X_train_A.npy $(np)/X_train_B.npy $(np)/X_train_C.npy $(np)/X_train_D.npy $(np)/X_train_E.npy $(np)/X_train_F.npy $(np)/X_train_G.npy $(np)/X_train_H.npy $(np)/X_train_I.npy $(np)/X_train_J.npy $(np)/X_train_K.npy $(np)/X_train_L.npy $(np)/X_train_M.npy $(np)/X_train_N.npy $(np)/X_train_O.npy $(np)/X_train_P.npy $(np)/X_train_Q.npy $(np)/X_train_R.npy $(np)/X_train_S.npy $(np)/X_train_T.npy $(np)/X_train_U.npy $(np)/X_train_form.npy $(np)/X_train_pos.npy

all_numpy_test: $(np)/X_test_A.npy $(np)/X_test_B.npy $(np)/X_test_C.npy $(np)/X_test_D.npy $(np)/X_test_E.npy $(np)/X_test_F.npy $(np)/X_test_G.npy $(np)/X_test_H.npy $(np)/X_test_I.npy $(np)/X_test_J.npy $(np)/X_test_K.npy $(np)/X_test_L.npy $(np)/X_test_M.npy $(np)/X_test_N.npy $(np)/X_test_O.npy $(np)/X_test_P.npy $(np)/X_test_Q.npy $(np)/X_test_R.npy $(np)/X_test_S.npy $(np)/X_test_T.npy $(np)/X_test_U.npy $(np)/X_test_form.npy $(np)/X_test_pos.npy

all_binary_train: $(bin)/A_train_input.bin $(bin)/B_train_input.bin $(bin)/C_train_input.bin $(bin)/D_train_input.bin $(bin)/E_train_input.bin $(bin)/F_train_input.bin $(bin)/G_train_input.bin $(bin)/H_train_input.bin $(bin)/I_train_input.bin $(bin)/J_train_input.bin $(bin)/K_train_input.bin $(bin)/L_train_input.bin $(bin)/M_train_input.bin $(bin)/N_train_input.bin $(bin)/O_train_input.bin $(bin)/P_train_input.bin $(bin)/Q_train_input.bin $(bin)/R_train_input.bin $(bin)/S_train_input.bin $(bin)/T_train_input.bin $(bin)/U_train_input.bin $(bin)/form_train_input.bin $(bin)/pos_train_input.bin

all_binary_test: $(bin)/A_test_input.bin $(bin)/B_test_input.bin $(bin)/C_test_input.bin $(bin)/D_test_input.bin $(bin)/E_test_input.bin $(bin)/F_test_input.bin $(bin)/G_test_input.bin $(bin)/H_test_input.bin $(bin)/I_test_input.bin $(bin)/J_test_input.bin $(bin)/K_test_input.bin $(bin)/L_test_input.bin $(bin)/M_test_input.bin $(bin)/N_test_input.bin $(bin)/O_test_input.bin $(bin)/P_test_input.bin $(bin)/Q_test_input.bin $(bin)/R_test_input.bin $(bin)/S_test_input.bin $(bin)/T_test_input.bin $(bin)/U_test_input.bin $(bin)/form_test_input.bin $(bin)/pos_train_input.bin

all_fann_train: fanns/A_train.fann fanns/B_train.fann fanns/C_train.fann fanns/D_train.fann fanns/E_train.fann fanns/F_train.fann fanns/G_train.fann fanns/H_train.fann fanns/I_train.fann fanns/J_train.fann fanns/K_train.fann fanns/L_train.fann fanns/M_train.fann fanns/N_train.fann fanns/O_train.fann fanns/P_train.fann fanns/Q_train.fann fanns/R_train.fann fanns/S_train.fann fanns/T_train.fann fanns/U_train.fann fanns/form_train.fann fanns/pos_train.fann

all_fann_dev: fanns/A_dev.fann fanns/B_dev.fann fanns/C_dev.fann fanns/D_dev.fann fanns/E_dev.fann fanns/F_dev.fann fanns/G_dev.fann fanns/H_dev.fann fanns/I_dev.fann fanns/J_dev.fann fanns/K_dev.fann fanns/L_dev.fann fanns/M_dev.fann fanns/N_dev.fann fanns/O_dev.fann fanns/P_dev.fann fanns/Q_dev.fann fanns/R_dev.fann fanns/S_dev.fann fanns/T_dev.fann fanns/U_dev.fann fanns/form_dev.fann fanns/pos_dev.fann

#Makefile commands for generating fann2binary exe
fann2binary: src/fann2binary.o
	gcc src/fann2binary.o -o fann2binary

src/fann2binary.o: src/fann2binary.c
	gcc -g -Wall -c -o src/fann2binary.o src/fann2binary.c

##############################################################################
#
#Makefile commands for generating numpy train files
#
##############################################################################
$(np)/X_train_A.npy: $(bin)/A_train_input.bin load_fann_bin.py
	python load_fann_bin.py TRAIN $(bin)/A_train_input.bin $(bin)/A_train_output.bin $(bin_info)/A_train.txt $(io)

$(np)/X_train_B.npy: $(bin)/B_train_input.bin load_fann_bin.py
	python load_fann_bin.py TRAIN $(bin)/B_train_input.bin $(bin)/B_train_output.bin $(bin_info)/B_train.txt $(io)

$(np)/X_train_C.npy: $(bin)/C_train_input.bin load_fann_bin.py
	python load_fann_bin.py TRAIN $(bin)/C_train_input.bin $(bin)/C_train_output.bin $(bin_info)/C_train.txt $(io)

$(np)/X_train_D.npy: $(bin)/D_train_input.bin load_fann_bin.py
	python load_fann_bin.py TRAIN $(bin)/D_train_input.bin $(bin)/D_train_output.bin $(bin_info)/D_train.txt $(io)

$(np)/X_train_E.npy: $(bin)/E_train_input.bin load_fann_bin.py
	python load_fann_bin.py TRAIN $(bin)/E_train_input.bin $(bin)/E_train_output.bin $(bin_info)/E_train.txt $(io)

$(np)/X_train_F.npy: $(bin)/F_train_input.bin load_fann_bin.py
	python load_fann_bin.py TRAIN $(bin)/F_train_input.bin $(bin)/F_train_output.bin $(bin_info)/F_train.txt $(io)

$(np)/X_train_G.npy: $(bin)/G_train_input.bin load_fann_bin.py
	python load_fann_bin.py TRAIN $(bin)/G_train_input.bin $(bin)/G_train_output.bin $(bin_info)/G_train.txt $(io)

$(np)/X_train_H.npy: $(bin)/H_train_input.bin load_fann_bin.py
	python load_fann_bin.py TRAIN $(bin)/H_train_input.bin $(bin)/H_train_output.bin $(bin_info)/H_train.txt $(io)

$(np)/X_train_I.npy: $(bin)/I_train_input.bin load_fann_bin.py
	python load_fann_bin.py TRAIN $(bin)/I_train_input.bin $(bin)/I_train_output.bin $(bin_info)/I_train.txt $(io)

$(np)/X_train_J.npy: $(bin)/J_train_input.bin load_fann_bin.py
	python load_fann_bin.py TRAIN $(bin)/J_train_input.bin $(bin)/J_train_output.bin $(bin_info)/J_train.txt $(io)

$(np)/X_train_K.npy: $(bin)/K_train_input.bin load_fann_bin.py
	python load_fann_bin.py TRAIN $(bin)/K_train_input.bin $(bin)/K_train_output.bin $(bin_info)/K_train.txt $(io)

$(np)/X_train_L.npy: $(bin)/L_train_input.bin load_fann_bin.py
	python load_fann_bin.py TRAIN $(bin)/L_train_input.bin $(bin)/L_train_output.bin $(bin_info)/L_train.txt $(io)

$(np)/X_train_M.npy: $(bin)/M_train_input.bin load_fann_bin.py
	python load_fann_bin.py TRAIN $(bin)/M_train_input.bin $(bin)/M_train_output.bin $(bin_info)/M_train.txt $(io)

$(np)/X_train_N.npy: $(bin)/N_train_input.bin load_fann_bin.py
	python load_fann_bin.py TRAIN $(bin)/N_train_input.bin $(bin)/N_train_output.bin $(bin_info)/N_train.txt $(io)

$(np)/X_train_O.npy: $(bin)/O_train_input.bin load_fann_bin.py
	python load_fann_bin.py TRAIN $(bin)/O_train_input.bin $(bin)/O_train_output.bin $(bin_info)/O_train.txt $(io)

$(np)/X_train_P.npy: $(bin)/P_train_input.bin load_fann_bin.py
	python load_fann_bin.py TRAIN $(bin)/P_train_input.bin $(bin)/P_train_output.bin $(bin_info)/P_train.txt $(io)

$(np)/X_train_Q.npy: $(bin)/Q_train_input.bin load_fann_bin.py
	python load_fann_bin.py TRAIN $(bin)/Q_train_input.bin $(bin)/Q_train_output.bin $(bin_info)/Q_train.txt $(io)

$(np)/X_train_R.npy: $(bin)/R_train_input.bin load_fann_bin.py
	python load_fann_bin.py TRAIN $(bin)/R_train_input.bin $(bin)/R_train_output.bin $(bin_info)/R_train.txt $(io)

$(np)/X_train_S.npy: $(bin)/S_train_input.bin load_fann_bin.py
	python load_fann_bin.py TRAIN $(bin)/S_train_input.bin $(bin)/S_train_output.bin $(bin_info)/S_train.txt $(io)

$(np)/X_train_T.npy: $(bin)/T_train_input.bin load_fann_bin.py
	python load_fann_bin.py TRAIN $(bin)/T_train_input.bin $(bin)/T_train_output.bin $(bin_info)/T_train.txt $(io)

$(np)/X_train_U.npy: $(bin)/U_train_input.bin load_fann_bin.py
	python load_fann_bin.py TRAIN $(bin)/U_train_input.bin $(bin)/U_train_output.bin $(bin_info)/U_train.txt $(io)

$(np)/X_train_form.npy: $(bin)/form_train_input.bin load_fann_bin.py
	python load_fann_bin.py TRAIN $(bin)/form_train_input.bin $(bin)/form_train_output.bin $(bin_info)/form_train.txt $(io)

$(np)/X_train_pos.npy: $(bin)/pos_train_input.bin load_fann_bin.py
	python load_fann_bin.py TRAIN $(bin)/pos_train_input.bin $(bin)/pos_train_output.bin $(bin_info)/pos_train.txt $(io)

##############################################################################
#
#Makefile commands for generating numpy test files
#
##############################################################################
$(np)/X_test_A.npy: $(bin)/A_test_input.bin load_fann_bin.py
	python load_fann_bin.py TEST $(bin)/A_test_input.bin $(bin)/A_test_output.bin $(bin_info)/A_test.txt $(io)

$(np)/X_test_B.npy: $(bin)/B_test_input.bin load_fann_bin.py
	python load_fann_bin.py TEST $(bin)/B_test_input.bin $(bin)/B_test_output.bin $(bin_info)/B_test.txt $(io)

$(np)/X_test_C.npy: $(bin)/C_test_input.bin load_fann_bin.py
	python load_fann_bin.py TEST $(bin)/C_test_input.bin $(bin)/C_test_output.bin $(bin_info)/C_test.txt $(io)

$(np)/X_test_D.npy: $(bin)/D_test_input.bin load_fann_bin.py
	python load_fann_bin.py TEST $(bin)/D_test_input.bin $(bin)/D_test_output.bin $(bin_info)/D_test.txt $(io)

$(np)/X_test_E.npy: $(bin)/E_test_input.bin load_fann_bin.py
	python load_fann_bin.py TEST $(bin)/E_test_input.bin $(bin)/E_test_output.bin $(bin_info)/E_test.txt $(io)

$(np)/X_test_F.npy: $(bin)/F_test_input.bin load_fann_bin.py
	python load_fann_bin.py TEST $(bin)/F_test_input.bin $(bin)/F_test_output.bin $(bin_info)/F_test.txt $(io)

$(np)/X_test_G.npy: $(bin)/G_test_input.bin load_fann_bin.py
	python load_fann_bin.py TEST $(bin)/G_test_input.bin $(bin)/G_test_output.bin $(bin_info)/G_test.txt $(io)

$(np)/X_test_H.npy: $(bin)/H_test_input.bin load_fann_bin.py
	python load_fann_bin.py TEST $(bin)/H_test_input.bin $(bin)/H_test_output.bin $(bin_info)/H_test.txt $(io)

$(np)/X_test_I.npy: $(bin)/I_test_input.bin load_fann_bin.py
	python load_fann_bin.py TEST $(bin)/I_test_input.bin $(bin)/I_test_output.bin $(bin_info)/I_test.txt $(io)

$(np)/X_test_J.npy: $(bin)/J_test_input.bin load_fann_bin.py
	python load_fann_bin.py TEST $(bin)/J_test_input.bin $(bin)/J_test_output.bin $(bin_info)/J_test.txt $(io)

$(np)/X_test_K.npy: $(bin)/K_test_input.bin load_fann_bin.py
	python load_fann_bin.py TEST $(bin)/K_test_input.bin $(bin)/K_test_output.bin $(bin_info)/K_test.txt $(io)

$(np)/X_test_L.npy: $(bin)/L_test_input.bin load_fann_bin.py
	python load_fann_bin.py TEST $(bin)/L_test_input.bin $(bin)/L_test_output.bin $(bin_info)/L_test.txt $(io)

$(np)/X_test_M.npy: $(bin)/M_test_input.bin load_fann_bin.py
	python load_fann_bin.py TEST $(bin)/M_test_input.bin $(bin)/M_test_output.bin $(bin_info)/M_test.txt $(io)

$(np)/X_test_N.npy: $(bin)/N_test_input.bin load_fann_bin.py
	python load_fann_bin.py TEST $(bin)/N_test_input.bin $(bin)/N_test_output.bin $(bin_info)/N_test.txt $(io)

$(np)/X_test_O.npy: $(bin)/O_test_input.bin load_fann_bin.py
	python load_fann_bin.py TEST $(bin)/O_test_input.bin $(bin)/O_test_output.bin $(bin_info)/O_test.txt $(io)

$(np)/X_test_P.npy: $(bin)/P_test_input.bin load_fann_bin.py
	python load_fann_bin.py TEST $(bin)/P_test_input.bin $(bin)/P_test_output.bin $(bin_info)/P_test.txt $(io)

$(np)/X_test_Q.npy: $(bin)/Q_test_input.bin load_fann_bin.py
	python load_fann_bin.py TEST $(bin)/Q_test_input.bin $(bin)/Q_test_output.bin $(bin_info)/Q_test.txt $(io)

$(np)/X_test_R.npy: $(bin)/R_test_input.bin load_fann_bin.py
	python load_fann_bin.py TEST $(bin)/R_test_input.bin $(bin)/R_test_output.bin $(bin_info)/R_test.txt $(io)

$(np)/X_test_S.npy: $(bin)/S_test_input.bin load_fann_bin.py
	python load_fann_bin.py TEST $(bin)/S_test_input.bin $(bin)/S_test_output.bin $(bin_info)/S_test.txt $(io)

$(np)/X_test_T.npy: $(bin)/T_test_input.bin load_fann_bin.py
	python load_fann_bin.py TEST $(bin)/T_test_input.bin $(bin)/T_test_output.bin $(bin_info)/T_test.txt $(io)

$(np)/X_test_U.npy: $(bin)/U_test_input.bin load_fann_bin.py
	python load_fann_bin.py TEST $(bin)/U_test_input.bin $(bin)/U_test_output.bin $(bin_info)/U_test.txt $(io)

$(np)/X_test_form.npy: $(bin)/form_test_input.bin load_fann_bin.py
	python load_fann_bin.py TEST $(bin)/form_test_input.bin $(bin)/form_test_output.bin $(bin_info)/form_test.txt $(io)

$(np)/X_test_pos.npy: $(bin)/pos_test_input.bin load_fann_bin.py
	python load_fann_bin.py TEST $(bin)/pos_test_input.bin $(bin)/pos_test_output.bin $(bin_info)/pos_test.txt $(io)

##############################################################################
#
#Makefile commands for generating fann binary train files
#
##############################################################################
$(bin)/A_train_input.bin: fann2binary fanns/A_train.fann
	./fann2binary fanns/A_train.fann fms/A.fm $(bin)/A_train_input.bin $(bin)/A_train_output.bin $(bin_info)/A_train.txt

$(bin)/B_train_input.bin: fann2binary fanns/B_train.fann
	./fann2binary fanns/B_train.fann fms/B.fm $(bin)/B_train_input.bin $(bin)/B_train_output.bin $(bin_info)/B_train.txt

$(bin)/C_train_input.bin: fann2binary fanns/C_train.fann
	./fann2binary fanns/C_train.fann fms/C.fm $(bin)/C_train_input.bin $(bin)/C_train_output.bin $(bin_info)/C_train.txt

$(bin)/D_train_input.bin: fann2binary fanns/D_train.fann
	./fann2binary fanns/D_train.fann fms/D.fm $(bin)/D_train_input.bin $(bin)/D_train_output.bin $(bin_info)/D_train.txt

$(bin)/E_train_input.bin: fann2binary fanns/E_train.fann
	./fann2binary fanns/E_train.fann fms/E.fm $(bin)/E_train_input.bin $(bin)/E_train_output.bin $(bin_info)/E_train.txt

$(bin)/F_train_input.bin: fann2binary fanns/F_train.fann
	./fann2binary fanns/F_train.fann fms/F.fm $(bin)/F_train_input.bin $(bin)/F_train_output.bin $(bin_info)/F_train.txt

$(bin)/G_train_input.bin: fann2binary fanns/G_train.fann
	./fann2binary fanns/G_train.fann fms/G.fm $(bin)/G_train_input.bin $(bin)/G_train_output.bin $(bin_info)/G_train.txt
	
$(bin)/H_train_input.bin: fann2binary fanns/H_train.fann
	./fann2binary fanns/H_train.fann fms/H.fm $(bin)/H_train_input.bin $(bin)/H_train_output.bin $(bin_info)/H_train.txt

$(bin)/I_train_input.bin: fann2binary fanns/I_train.fann
	./fann2binary fanns/I_train.fann fms/I.fm $(bin)/I_train_input.bin $(bin)/I_train_output.bin $(bin_info)/I_train.txt

$(bin)/J_train_input.bin: fann2binary fanns/J_train.fann
	./fann2binary fanns/J_train.fann fms/J.fm $(bin)/J_train_input.bin $(bin)/J_train_output.bin $(bin_info)/J_train.txt

$(bin)/K_train_input.bin: fann2binary fanns/K_train.fann
	./fann2binary fanns/K_train.fann fms/K.fm $(bin)/K_train_input.bin $(bin)/K_train_output.bin $(bin_info)/K_train.txt

$(bin)/L_train_input.bin: fann2binary fanns/L_train.fann
	./fann2binary fanns/L_train.fann fms/L.fm $(bin)/L_train_input.bin $(bin)/L_train_output.bin $(bin_info)/L_train.txt

$(bin)/M_train_input.bin: fann2binary fanns/M_train.fann
	./fann2binary fanns/M_train.fann fms/M.fm $(bin)/M_train_input.bin $(bin)/M_train_output.bin $(bin_info)/M_train.txt

$(bin)/N_train_input.bin: fann2binary fanns/N_train.fann
	./fann2binary fanns/N_train.fann fms/N.fm $(bin)/N_train_input.bin $(bin)/N_train_output.bin $(bin_info)/N_train.txt

$(bin)/O_train_input.bin: fann2binary fanns/O_train.fann
	./fann2binary fanns/O_train.fann fms/O.fm $(bin)/O_train_input.bin $(bin)/O_train_output.bin $(bin_info)/O_train.txt

$(bin)/P_train_input.bin: fann2binary fanns/P_train.fann
	./fann2binary fanns/P_train.fann fms/P.fm $(bin)/P_train_input.bin $(bin)/P_train_output.bin $(bin_info)/P_train.txt

$(bin)/Q_train_input.bin: fann2binary fanns/Q_train.fann
	./fann2binary fanns/Q_train.fann fms/Q.fm $(bin)/Q_train_input.bin $(bin)/Q_train_output.bin $(bin_info)/Q_train.txt

$(bin)/R_train_input.bin: fann2binary fanns/R_train.fann
	./fann2binary fanns/R_train.fann fms/R.fm $(bin)/R_train_input.bin $(bin)/R_train_output.bin $(bin_info)/R_train.txt

$(bin)/S_train_input.bin: fann2binary fanns/S_train.fann
	./fann2binary fanns/S_train.fann fms/S.fm $(bin)/S_train_input.bin $(bin)/S_train_output.bin $(bin_info)/S_train.txt

$(bin)/T_train_input.bin: fann2binary fanns/T_train.fann
	./fann2binary fanns/T_train.fann fms/T.fm $(bin)/T_train_input.bin $(bin)/T_train_output.bin $(bin_info)/T_train.txt

$(bin)/U_train_input.bin: fann2binary fanns/U_train.fann
	./fann2binary fanns/U_train.fann fms/U.fm $(bin)/U_train_input.bin $(bin)/U_train_output.bin $(bin_info)/U_train.txt

$(bin)/form_train_input.bin: fann2binary fanns/form_train.fann
	./fann2binary fanns/form_train.fann fms/form.fm $(bin)/form_train_input.bin $(bin)/form_train_output.bin $(bin_info)/form_train.txt

$(bin)/pos_train_input.bin: fann2binary fanns/pos_train.fann
	./fann2binary fanns/pos_train.fann fms/pos.fm $(bin)/pos_train_input.bin $(bin)/pos_train_output.bin $(bin_info)/pos_train.txt

##############################################################################
#
#Makefile commands for generating fann binary test files
#
##############################################################################
$(bin)/A_test_input.bin: fann2binary fanns/A_dev.fann
	./fann2binary fanns/A_dev.fann fms/A.fm $(bin)/A_test_input.bin $(bin)/A_test_output.bin $(bin_info)/A_test.txt

$(bin)/B_test_input.bin: fann2binary fanns/B_dev.fann
	./fann2binary fanns/B_dev.fann fms/B.fm $(bin)/B_test_input.bin $(bin)/B_test_output.bin $(bin_info)/B_test.txt

$(bin)/C_test_input.bin: fann2binary fanns/C_dev.fann
	./fann2binary fanns/C_dev.fann fms/C.fm $(bin)/C_test_input.bin $(bin)/C_test_output.bin $(bin_info)/C_test.txt

$(bin)/D_test_input.bin: fann2binary fanns/D_dev.fann
	./fann2binary fanns/D_dev.fann fms/D.fm $(bin)/D_test_input.bin $(bin)/D_test_output.bin $(bin_info)/D_test.txt

$(bin)/E_test_input.bin: fann2binary fanns/E_dev.fann
	./fann2binary fanns/E_dev.fann fms/E.fm $(bin)/E_test_input.bin $(bin)/E_test_output.bin $(bin_info)/E_test.txt

$(bin)/F_test_input.bin: fann2binary fanns/F_dev.fann
	./fann2binary fanns/F_dev.fann fms/F.fm $(bin)/F_test_input.bin $(bin)/F_test_output.bin $(bin_info)/F_test.txt

$(bin)/G_test_input.bin: fann2binary fanns/G_dev.fann
	./fann2binary fanns/G_dev.fann fms/G.fm $(bin)/G_test_input.bin $(bin)/G_test_output.bin $(bin_info)/G_test.txt
	
$(bin)/H_test_input.bin: fann2binary fanns/H_dev.fann
	./fann2binary fanns/H_dev.fann fms/H.fm $(bin)/H_test_input.bin $(bin)/H_test_output.bin $(bin_info)/H_test.txt

$(bin)/I_test_input.bin: fann2binary fanns/I_dev.fann
	./fann2binary fanns/I_dev.fann fms/I.fm $(bin)/I_test_input.bin $(bin)/I_test_output.bin $(bin_info)/I_test.txt

$(bin)/J_test_input.bin: fann2binary fanns/J_dev.fann
	./fann2binary fanns/J_dev.fann fms/J.fm $(bin)/J_test_input.bin $(bin)/J_test_output.bin $(bin_info)/J_test.txt

$(bin)/K_test_input.bin: fann2binary fanns/K_dev.fann
	./fann2binary fanns/K_dev.fann fms/K.fm $(bin)/K_test_input.bin $(bin)/K_test_output.bin $(bin_info)/K_test.txt

$(bin)/L_test_input.bin: fann2binary fanns/L_dev.fann
	./fann2binary fanns/L_dev.fann fms/L.fm $(bin)/L_test_input.bin $(bin)/L_test_output.bin $(bin_info)/L_test.txt

$(bin)/M_test_input.bin: fann2binary fanns/M_dev.fann
	./fann2binary fanns/M_dev.fann fms/M.fm $(bin)/M_test_input.bin $(bin)/M_test_output.bin $(bin_info)/M_test.txt

$(bin)/N_test_input.bin: fann2binary fanns/N_dev.fann
	./fann2binary fanns/N_dev.fann fms/N.fm $(bin)/N_test_input.bin $(bin)/N_test_output.bin $(bin_info)/N_test.txt

$(bin)/O_test_input.bin: fann2binary fanns/O_dev.fann
	./fann2binary fanns/O_dev.fann fms/O.fm $(bin)/O_test_input.bin $(bin)/O_test_output.bin $(bin_info)/O_test.txt

$(bin)/P_test_input.bin: fann2binary fanns/P_dev.fann
	./fann2binary fanns/P_dev.fann fms/P.fm $(bin)/P_test_input.bin $(bin)/P_test_output.bin $(bin_info)/P_test.txt

$(bin)/Q_test_input.bin: fann2binary fanns/Q_dev.fann
	./fann2binary fanns/Q_dev.fann fms/Q.fm $(bin)/Q_test_input.bin $(bin)/Q_test_output.bin $(bin_info)/Q_test.txt

$(bin)/R_test_input.bin: fann2binary fanns/R_dev.fann
	./fann2binary fanns/R_dev.fann fms/R.fm $(bin)/R_test_input.bin $(bin)/R_test_output.bin $(bin_info)/R_test.txt

$(bin)/S_test_input.bin: fann2binary fanns/S_dev.fann
	./fann2binary fanns/S_dev.fann fms/S.fm $(bin)/S_test_input.bin $(bin)/S_test_output.bin $(bin_info)/S_test.txt

$(bin)/T_test_input.bin: fann2binary fanns/T_dev.fann
	./fann2binary fanns/T_dev.fann fms/T.fm $(bin)/T_test_input.bin $(bin)/T_test_output.bin $(bin_info)/T_test.txt

$(bin)/U_test_input.bin: fann2binary fanns/U_dev.fann
	./fann2binary fanns/U_dev.fann fms/U.fm $(bin)/U_test_input.bin $(bin)/U_test_output.bin $(bin_info)/U_test.txt

$(bin)/form_test_input.bin: fann2binary fanns/form_dev.fann
	./fann2binary fanns/form_dev.fann fms/form.fm $(bin)/form_test_input.bin $(bin)/form_test_output.bin $(bin_info)/form_test.txt

$(bin)/pos_test_input.bin: fann2binary fanns/pos_dev.fann
	./fann2binary fanns/pos_dev.fann fms/pos.fm $(bin)/pos_test_input.bin $(bin)/pos_test_output.bin $(bin_info)/pos_test.txt

##############################################################################
#
#Makefile commands for generating fann train files
#
##############################################################################
fanns/A_train.fann: fms/A.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/A_train.fann ./alphas/A.alpha ./fms/A.fm dimensions.mcd $(train_nb_sents)

fanns/B_train.fann: fms/B.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/B_train.fann ./alphas/B.alpha ./fms/B.fm dimensions.mcd $(train_nb_sents)

fanns/C_train.fann: fms/C.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/C_train.fann ./alphas/C.alpha ./fms/C.fm dimensions.mcd $(train_nb_sents)

fanns/D_train.fann: fms/D.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/D_train.fann ./alphas/D.alpha ./fms/D.fm dimensions.mcd $(train_nb_sents)

fanns/E_train.fann: fms/E.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/E_train.fann ./alphas/E.alpha ./fms/E.fm dimensions.mcd $(train_nb_sents)

fanns/F_train.fann: fms/F.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/F_train.fann ./alphas/F.alpha ./fms/F.fm dimensions.mcd $(train_nb_sents)

fanns/G_train.fann: fms/G.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/G_train.fann ./alphas/G.alpha ./fms/G.fm dimensions.mcd $(train_nb_sents)

fanns/H_train.fann: fms/H.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/H_train.fann ./alphas/H.alpha ./fms/H.fm dimensions.mcd $(train_nb_sents)

fanns/I_train.fann: fms/I.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/I_train.fann ./alphas/I.alpha ./fms/I.fm dimensions.mcd $(train_nb_sents)

fanns/J_train.fann: fms/J.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/J_train.fann ./alphas/J.alpha ./fms/J.fm dimensions.mcd $(train_nb_sents)

fanns/K_train.fann: fms/K.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/K_train.fann ./alphas/K.alpha ./fms/K.fm dimensions.mcd $(train_nb_sents)

fanns/L_train.fann: fms/L.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/L_train.fann ./alphas/L.alpha ./fms/L.fm dimensions.mcd $(train_nb_sents)

fanns/M_train.fann: fms/M.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/M_train.fann ./alphas/M.alpha ./fms/M.fm dimensions.mcd $(train_nb_sents)

fanns/N_train.fann: fms/N.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/N_train.fann ./alphas/N.alpha ./fms/N.fm dimensions.mcd $(train_nb_sents)

fanns/O_train.fann: fms/O.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/O_train.fann ./alphas/O.alpha ./fms/O.fm dimensions.mcd $(train_nb_sents)

fanns/P_train.fann: fms/P.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/P_train.fann ./alphas/P.alpha ./fms/P.fm dimensions.mcd $(train_nb_sents)

fanns/Q_train.fann: fms/Q.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/Q_train.fann ./alphas/Q.alpha ./fms/Q.fm dimensions.mcd $(train_nb_sents)

fanns/R_train.fann: fms/R.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/R_train.fann ./alphas/R.alpha ./fms/R.fm dimensions.mcd $(train_nb_sents)

fanns/S_train.fann: fms/S.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/S_train.fann ./alphas/S.alpha ./fms/S.fm dimensions.mcd $(train_nb_sents)

fanns/T_train.fann: fms/T.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/T_train.fann ./alphas/T.alpha ./fms/T.fm dimensions.mcd $(train_nb_sents)

fanns/U_train.fann: fms/U.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/U_train.fann ./alphas/U.alpha ./fms/U.fm dimensions.mcd $(train_nb_sents)

fanns/form_train.fann: fms/form.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/form_train.fann ./alphas/form.alpha ./fms/form.fm dimensions.mcd $(train_nb_sents)

fanns/pos_train.fann: fms/pos.fm dimensions.mcd
	./make_fann.sh TRAIN $(train_data) ./fanns/pos_train.fann ./alphas/pos.alpha ./fms/pos.fm dimensions.mcd $(train_nb_sents)

##############################################################################
#
#Makefile commands for generating fann dev files
#
##############################################################################
fanns/A_dev.fann: fms/A.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/A_dev.fann ./alphas/A.alpha ./fms/A.fm dimensions.mcd $(test_nb_sents)

fanns/B_dev.fann: fms/B.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/B_dev.fann ./alphas/B.alpha ./fms/B.fm dimensions.mcd $(test_nb_sents)

fanns/C_dev.fann: fms/C.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/C_dev.fann ./alphas/C.alpha ./fms/C.fm dimensions.mcd $(test_nb_sents)

fanns/D_dev.fann: fms/D.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/D_dev.fann ./alphas/D.alpha ./fms/D.fm dimensions.mcd $(test_nb_sents)

fanns/E_dev.fann: fms/E.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/E_dev.fann ./alphas/E.alpha ./fms/E.fm dimensions.mcd $(test_nb_sents)

fanns/F_dev.fann: fms/F.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/F_dev.fann ./alphas/F.alpha ./fms/F.fm dimensions.mcd $(test_nb_sents)

fanns/G_dev.fann: fms/G.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/G_dev.fann ./alphas/G.alpha ./fms/G.fm dimensions.mcd $(test_nb_sents)

fanns/H_dev.fann: fms/H.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/H_dev.fann ./alphas/H.alpha ./fms/H.fm dimensions.mcd $(test_nb_sents)

fanns/I_dev.fann: fms/I.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/I_dev.fann ./alphas/I.alpha ./fms/I.fm dimensions.mcd $(test_nb_sents)

fanns/J_dev.fann: fms/J.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/J_dev.fann ./alphas/J.alpha ./fms/J.fm dimensions.mcd $(test_nb_sents)

fanns/K_dev.fann: fms/K.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/K_dev.fann ./alphas/K.alpha ./fms/K.fm dimensions.mcd $(test_nb_sents)

fanns/L_dev.fann: fms/L.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/L_dev.fann ./alphas/L.alpha ./fms/L.fm dimensions.mcd $(test_nb_sents)

fanns/M_dev.fann: fms/M.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/M_dev.fann ./alphas/M.alpha ./fms/M.fm dimensions.mcd $(test_nb_sents)

fanns/N_dev.fann: fms/N.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/N_dev.fann ./alphas/N.alpha ./fms/N.fm dimensions.mcd $(test_nb_sents)

fanns/O_dev.fann: fms/O.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/O_dev.fann ./alphas/O.alpha ./fms/O.fm dimensions.mcd $(test_nb_sents)

fanns/P_dev.fann: fms/P.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/P_dev.fann ./alphas/P.alpha ./fms/P.fm dimensions.mcd $(test_nb_sents)

fanns/Q_dev.fann: fms/Q.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/Q_dev.fann ./alphas/Q.alpha ./fms/Q.fm dimensions.mcd $(test_nb_sents)

fanns/R_dev.fann: fms/R.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/R_dev.fann ./alphas/R.alpha ./fms/R.fm dimensions.mcd $(test_nb_sents)

fanns/S_dev.fann: fms/S.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/S_dev.fann ./alphas/S.alpha ./fms/S.fm dimensions.mcd $(test_nb_sents)

fanns/T_dev.fann: fms/T.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/T_dev.fann ./alphas/T.alpha ./fms/T.fm dimensions.mcd $(test_nb_sents)

fanns/U_dev.fann: fms/U.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/U_dev.fann ./alphas/U.alpha ./fms/U.fm dimensions.mcd $(test_nb_sents)

fanns/form_dev.fann: fms/form.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/form_dev.fann ./alphas/form.alpha ./fms/form.fm dimensions.mcd $(test_nb_sents)

fanns/pos_dev.fann: fms/pos.fm dimensions.mcd
	./make_fann.sh TEST $(dev_data) ./fanns/pos_dev.fann ./alphas/pos.alpha ./fms/pos.fm dimensions.mcd $(test_nb_sents)

.PHONY: clean
clean:
	- rm ./fanns/*.fann
	- rm ./numpy_arrays/*.npy
	- rm io_dimensions*
	- rm -f *.o a.out core fann2binary 
	- rm ./binary_fanns/*.bin
	- rm ./binary_fanns_info/*.txt
