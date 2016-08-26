all: train test

train: all_fann_train all_numpy_train

test: all_fann_dev all_numpy_test

all_numpy_train: numpy_arrays/X_train_A.npy numpy_arrays/X_train_B.npy numpy_arrays/X_train_C.npy numpy_arrays/X_train_D.npy numpy_arrays/X_train_E.npy numpy_arrays/X_train_F.npy numpy_arrays/X_train_G.npy numpy_arrays/X_train_H.npy numpy_arrays/X_train_I.npy numpy_arrays/X_train_J.npy numpy_arrays/X_train_K.npy numpy_arrays/X_train_L.npy numpy_arrays/X_train_M.npy numpy_arrays/X_train_N.npy numpy_arrays/X_train_O.npy numpy_arrays/X_train_P.npy numpy_arrays/X_train_Q.npy numpy_arrays/X_train_R.npy numpy_arrays/X_train_S.npy numpy_arrays/X_train_T.npy numpy_arrays/X_train_U.npy

all_numpy_test: numpy_arrays/X_test_A.npy numpy_arrays/X_test_B.npy numpy_arrays/X_test_C.npy numpy_arrays/X_test_D.npy numpy_arrays/X_test_E.npy numpy_arrays/X_test_H.npy numpy_arrays/X_test_I.npy numpy_arrays/X_test_J.npy numpy_arrays/X_test_K.npy numpy_arrays/X_test_L.npy numpy_arrays/X_test_M.npy numpy_arrays/X_test_N.npy numpy_arrays/X_test_O.npy numpy_arrays/X_test_P.npy numpy_arrays/X_test_Q.npy numpy_arrays/X_test_R.npy numpy_arrays/X_test_S.npy numpy_arrays/X_test_T.npy numpy_arrays/X_test_U.npy

all_fann_train: fanns/A_train.fann fanns/B_train.fann fanns/C_train.fann fanns/D_train.fann fanns/E_train.fann fanns/F_train.fann fanns/G_train.fann fanns/H_train.fann fanns/I_train.fann fanns/J_train.fann fanns/K_train.fann fanns/L_train.fann fanns/M_train.fann fanns/N_train.fann fanns/O_train.fann fanns/P_train.fann fanns/Q_train.fann fanns/R_train.fann fanns/S_train.fann fanns/T_train.fann fanns/U_train.fann

all_fann_dev: fanns/A_dev.fann fanns/B_dev.fann fanns/C_dev.fann fanns/D_dev.fann fanns/E_dev.fann fanns/H_dev.fann fanns/I_dev.fann fanns/J_dev.fann fanns/K_dev.fann fanns/L_dev.fann fanns/M_dev.fann fanns/N_dev.fann fanns/O_dev.fann fanns/P_dev.fann fanns/Q_dev.fann fanns/R_dev.fann fanns/S_dev.fann fanns/T_dev.fann fanns/U_dev.fann

#Makefile commands for generating fann files from train fann files
numpy_arrays/X_train_A.npy: fanns/A_train.fann
	python ../scripts/general.py fanns/A_train.fann fms/A.fm io_dimensions_1000.txt TRAIN

numpy_arrays/X_train_B.npy: fanns/B_train.fann
	python ../scripts/general.py fanns/B_train.fann fms/B.fm io_dimensions_1000.txt TRAIN

numpy_arrays/X_train_C.npy: fanns/C_train.fann
	python ../scripts/general.py fanns/C_train.fann fms/C.fm io_dimensions_1000.txt TRAIN

numpy_arrays/X_train_D.npy: fanns/D_train.fann
	python ../scripts/general.py fanns/D_train.fann fms/D.fm io_dimensions_1000.txt TRAIN

numpy_arrays/X_train_E.npy: fanns/E_train.fann
	python ../scripts/general.py fanns/E_train.fann fms/E.fm io_dimensions_1000.txt TRAIN

numpy_arrays/X_train_F.npy: fanns/F_train.fann
	python ../scripts/general.py fanns/F_train.fann fms/F.fm io_dimensions_1000.txt TRAIN

numpy_arrays/X_train_G.npy: fanns/G_train.fann
	python ../scripts/general.py fanns/G_train.fann fms/G.fm io_dimensions_1000.txt TRAIN

numpy_arrays/X_train_H.npy: fanns/H_train.fann
	python ../scripts/general.py fanns/H_train.fann fms/H.fm io_dimensions_1000.txt TRAIN

numpy_arrays/X_train_I.npy: fanns/I_train.fann
	python ../scripts/general.py fanns/I_train.fann fms/I.fm io_dimensions_1000.txt TRAIN

numpy_arrays/X_train_J.npy: fanns/J_train.fann
	python ../scripts/general.py fanns/J_train.fann fms/J.fm io_dimensions_1000.txt TRAIN

numpy_arrays/X_train_K.npy: fanns/K_train.fann
	python ../scripts/general.py fanns/K_train.fann fms/K.fm io_dimensions_1000.txt TRAIN

numpy_arrays/X_train_L.npy: fanns/L_train.fann
	python ../scripts/general.py fanns/L_train.fann fms/L.fm io_dimensions_1000.txt TRAIN

numpy_arrays/X_train_M.npy: fanns/M_train.fann
	python ../scripts/general.py fanns/M_train.fann fms/M.fm io_dimensions_1000.txt TRAIN

numpy_arrays/X_train_N.npy: fanns/N_train.fann
	python ../scripts/general.py fanns/N_train.fann fms/N.fm io_dimensions_1000.txt TRAIN

numpy_arrays/X_train_O.npy: fanns/O_train.fann
	python ../scripts/general.py fanns/O_train.fann fms/O.fm io_dimensions_1000.txt TRAIN

numpy_arrays/X_train_P.npy: fanns/P_train.fann
	python ../scripts/general.py fanns/P_train.fann fms/P.fm io_dimensions_1000.txt TRAIN

numpy_arrays/X_train_Q.npy: fanns/Q_train.fann
	python ../scripts/general.py fanns/Q_train.fann fms/Q.fm io_dimensions_1000.txt TRAIN

numpy_arrays/X_train_R.npy: fanns/R_train.fann
	python ../scripts/general.py fanns/R_train.fann fms/R.fm io_dimensions_1000.txt TRAIN

numpy_arrays/X_train_S.npy: fanns/S_train.fann
	python ../scripts/general.py fanns/S_train.fann fms/S.fm io_dimensions_1000.txt TRAIN

numpy_arrays/X_train_T.npy: fanns/T_train.fann
	python ../scripts/general.py fanns/T_train.fann fms/T.fm io_dimensions_1000.txt TRAIN

numpy_arrays/X_train_U.npy: fanns/U_train.fann
	python ../scripts/general.py fanns/U_train.fann fms/U.fm io_dimensions_1000.txt TRAIN

#Makefile commands for generating fann files from dev fann files
numpy_arrays/X_test_A.npy: fanns/A_dev.fann
	python ../scripts/general.py fanns/A_dev.fann fms/A.fm io_dimensions_1000.txt TEST

numpy_arrays/X_test_B.npy: fanns/B_dev.fann
	python ../scripts/general.py fanns/B_dev.fann fms/B.fm io_dimensions_1000.txt TEST

numpy_arrays/X_test_C.npy: fanns/C_dev.fann
	python ../scripts/general.py fanns/C_dev.fann fms/C.fm io_dimensions_1000.txt TEST

numpy_arrays/X_test_D.npy: fanns/D_dev.fann
	python ../scripts/general.py fanns/D_dev.fann fms/D.fm io_dimensions_1000.txt TEST

numpy_arrays/X_test_E.npy: fanns/E_dev.fann
	python ../scripts/general.py fanns/E_dev.fann fms/E.fm io_dimensions_1000.txt TEST

numpy_arrays/X_test_F.npy: fanns/F_dev.fann
	python ../scripts/general.py fanns/F_dev.fann fms/F.fm io_dimensions_1000.txt TEST

numpy_arrays/X_test_G.npy: fanns/G_dev.fann
	python ../scripts/general.py fanns/G_dev.fann fms/G.fm io_dimensions_1000.txt TEST

numpy_arrays/X_test_H.npy: fanns/H_dev.fann
	python ../scripts/general.py fanns/H_dev.fann fms/H.fm io_dimensions_1000.txt TEST

numpy_arrays/X_test_I.npy: fanns/I_dev.fann
	python ../scripts/general.py fanns/I_dev.fann fms/I.fm io_dimensions_1000.txt TEST

numpy_arrays/X_test_J.npy: fanns/J_dev.fann
	python ../scripts/general.py fanns/J_dev.fann fms/J.fm io_dimensions_1000.txt TEST

numpy_arrays/X_test_K.npy: fanns/K_dev.fann
	python ../scripts/general.py fanns/K_dev.fann fms/K.fm io_dimensions_1000.txt TEST

numpy_arrays/X_test_L.npy: fanns/L_dev.fann
	python ../scripts/general.py fanns/L_dev.fann fms/L.fm io_dimensions_1000.txt TEST

numpy_arrays/X_test_M.npy: fanns/M_dev.fann
	python ../scripts/general.py fanns/M_dev.fann fms/M.fm io_dimensions_1000.txt TEST

numpy_arrays/X_test_N.npy: fanns/N_dev.fann
	python ../scripts/general.py fanns/N_dev.fann fms/N.fm io_dimensions_1000.txt TEST

numpy_arrays/X_test_O.npy: fanns/O_dev.fann
	python ../scripts/general.py fanns/O_dev.fann fms/O.fm io_dimensions_1000.txt TEST

numpy_arrays/X_test_P.npy: fanns/P_dev.fann
	python ../scripts/general.py fanns/P_dev.fann fms/P.fm io_dimensions_1000.txt TEST

numpy_arrays/X_test_Q.npy: fanns/Q_dev.fann
	python ../scripts/general.py fanns/Q_dev.fann fms/Q.fm io_dimensions_1000.txt TEST

numpy_arrays/X_test_R.npy: fanns/R_dev.fann
	python ../scripts/general.py fanns/R_dev.fann fms/R.fm io_dimensions_1000.txt TEST

numpy_arrays/X_test_S.npy: fanns/S_dev.fann
	python ../scripts/general.py fanns/S_dev.fann fms/S.fm io_dimensions_1000.txt TEST

numpy_arrays/X_test_T.npy: fanns/T_dev.fann
	python ../scripts/general.py fanns/T_dev.fann fms/T.fm io_dimensions_1000.txt TEST

numpy_arrays/X_test_U.npy: fanns/U_dev.fann
	python ../scripts/general.py fanns/U_dev.fann fms/U.fm io_dimensions_1000.txt TEST

#Makefile for generating fann train files
fanns/A_train.fann: fms/A.fm dimensions.mcd
	./make_train.sh TRAIN ./fanns/A_train.fann ./alphas/A.alpha ./fms/A.fm dimensions.mcd 1000

fanns/B_train.fann: fms/B.fm dimensions.mcd
	./make_train.sh TRAIN ./fanns/B_train.fann ./alphas/B.alpha ./fms/B.fm dimensions.mcd 1000

fanns/C_train.fann: fms/C.fm dimensions.mcd
	./make_train.sh TRAIN ./fanns/C_train.fann ./alphas/C.alpha ./fms/C.fm dimensions.mcd 1000

fanns/D_train.fann: fms/D.fm dimensions.mcd
	./make_train.sh TRAIN ./fanns/D_train.fann ./alphas/D.alpha ./fms/D.fm dimensions.mcd 1000

fanns/E_train.fann: fms/E.fm dimensions.mcd
	./make_train.sh TRAIN ./fanns/E_train.fann ./alphas/E.alpha ./fms/E.fm dimensions.mcd 1000

fanns/F_train.fann: fms/F.fm dimensions.mcd
	./make_train.sh TRAIN ./fanns/F_train.fann ./alphas/F.alpha ./fms/F.fm dimensions.mcd 1000

fanns/G_train.fann: fms/G.fm dimensions.mcd
	./make_train.sh TRAIN ./fanns/G_train.fann ./alphas/G.alpha ./fms/G.fm dimensions.mcd 1000

fanns/H_train.fann: fms/H.fm dimensions.mcd
	./make_train.sh TRAIN ./fanns/H_train.fann ./alphas/H.alpha ./fms/H.fm dimensions.mcd 1000

fanns/I_train.fann: fms/I.fm dimensions.mcd
	./make_train.sh TRAIN ./fanns/I_train.fann ./alphas/I.alpha ./fms/I.fm dimensions.mcd 1000

fanns/J_train.fann: fms/J.fm dimensions.mcd
	./make_train.sh TRAIN ./fanns/J_train.fann ./alphas/J.alpha ./fms/J.fm dimensions.mcd 1000

fanns/K_train.fann: fms/K.fm dimensions.mcd
	./make_train.sh TRAIN ./fanns/K_train.fann ./alphas/K.alpha ./fms/K.fm dimensions.mcd 1000

fanns/L_train.fann: fms/L.fm dimensions.mcd
	./make_train.sh TRAIN ./fanns/L_train.fann ./alphas/L.alpha ./fms/L.fm dimensions.mcd 1000

fanns/M_train.fann: fms/M.fm dimensions.mcd
	./make_train.sh TRAIN ./fanns/M_train.fann ./alphas/M.alpha ./fms/M.fm dimensions.mcd 1000

fanns/N_train.fann: fms/N.fm dimensions.mcd
	./make_train.sh TRAIN ./fanns/N_train.fann ./alphas/N.alpha ./fms/N.fm dimensions.mcd 1000

fanns/O_train.fann: fms/O.fm dimensions.mcd
	./make_train.sh TRAIN ./fanns/O_train.fann ./alphas/O.alpha ./fms/O.fm dimensions.mcd 1000

fanns/P_train.fann: fms/P.fm dimensions.mcd
	./make_train.sh TRAIN ./fanns/P_train.fann ./alphas/P.alpha ./fms/P.fm dimensions.mcd 1000

fanns/Q_train.fann: fms/Q.fm dimensions.mcd
	./make_train.sh TRAIN ./fanns/Q_train.fann ./alphas/Q.alpha ./fms/Q.fm dimensions.mcd 1000

fanns/R_train.fann: fms/R.fm dimensions.mcd
	./make_train.sh TRAIN ./fanns/R_train.fann ./alphas/R.alpha ./fms/R.fm dimensions.mcd 1000

fanns/S_train.fann: fms/S.fm dimensions.mcd
	./make_train.sh TRAIN ./fanns/S_train.fann ./alphas/S.alpha ./fms/S.fm dimensions.mcd 1000

fanns/T_train.fann: fms/T.fm dimensions.mcd
	./make_train.sh TRAIN ./fanns/T_train.fann ./alphas/T.alpha ./fms/T.fm dimensions.mcd 1000

fanns/U_train.fann: fms/U.fm dimensions.mcd
	./make_train.sh TRAIN ./fanns/U_train.fann ./alphas/U.alpha ./fms/U.fm dimensions.mcd 1000

#Makefile for generating fann test files
fanns/A_dev.fann: fms/A.fm dimensions.mcd
	./make_dev.sh TEST ./fanns/A_dev.fann ./alphas/A.alpha ./fms/A.fm dimensions.mcd 

fanns/B_dev.fann: fms/B.fm dimensions.mcd
	./make_dev.sh TEST ./fanns/B_dev.fann ./alphas/B.alpha ./fms/B.fm dimensions.mcd 

fanns/C_dev.fann: fms/C.fm dimensions.mcd
	./make_dev.sh TEST ./fanns/C_dev.fann ./alphas/C.alpha ./fms/C.fm dimensions.mcd 

fanns/D_dev.fann: fms/D.fm dimensions.mcd
	./make_dev.sh TEST ./fanns/D_dev.fann ./alphas/D.alpha ./fms/D.fm dimensions.mcd 

fanns/E_dev.fann: fms/E.fm dimensions.mcd
	./make_dev.sh TEST ./fanns/E_dev.fann ./alphas/E.alpha ./fms/E.fm dimensions.mcd 

fanns/F_dev.fann: fms/F.fm dimensions.mcd
	./make_dev.sh TEST ./fanns/F_dev.fann ./alphas/F.alpha ./fms/F.fm dimensions.mcd 

fanns/G_dev.fann: fms/G.fm dimensions.mcd
	./make_dev.sh TEST ./fanns/G_dev.fann ./alphas/G.alpha ./fms/G.fm dimensions.mcd 

fanns/H_dev.fann: fms/H.fm dimensions.mcd
	./make_dev.sh TEST ./fanns/H_dev.fann ./alphas/H.alpha ./fms/H.fm dimensions.mcd 

fanns/I_dev.fann: fms/I.fm dimensions.mcd
	./make_dev.sh TEST ./fanns/I_dev.fann ./alphas/I.alpha ./fms/I.fm dimensions.mcd 

fanns/J_dev.fann: fms/J.fm dimensions.mcd
	./make_dev.sh TEST ./fanns/J_dev.fann ./alphas/J.alpha ./fms/J.fm dimensions.mcd 

fanns/K_dev.fann: fms/K.fm dimensions.mcd
	./make_dev.sh TEST ./fanns/K_dev.fann ./alphas/K.alpha ./fms/K.fm dimensions.mcd 

fanns/L_dev.fann: fms/L.fm dimensions.mcd
	./make_dev.sh TEST ./fanns/L_dev.fann ./alphas/L.alpha ./fms/L.fm dimensions.mcd 

fanns/M_dev.fann: fms/M.fm dimensions.mcd
	./make_dev.sh TEST ./fanns/M_dev.fann ./alphas/M.alpha ./fms/M.fm dimensions.mcd 

fanns/N_dev.fann: fms/N.fm dimensions.mcd
	./make_dev.sh TEST ./fanns/N_dev.fann ./alphas/N.alpha ./fms/N.fm dimensions.mcd 

fanns/O_dev.fann: fms/O.fm dimensions.mcd
	./make_dev.sh TEST ./fanns/O_dev.fann ./alphas/O.alpha ./fms/O.fm dimensions.mcd 

fanns/P_dev.fann: fms/P.fm dimensions.mcd
	./make_dev.sh TEST ./fanns/P_dev.fann ./alphas/P.alpha ./fms/P.fm dimensions.mcd 

fanns/Q_dev.fann: fms/Q.fm dimensions.mcd
	./make_dev.sh TEST ./fanns/Q_dev.fann ./alphas/Q.alpha ./fms/Q.fm dimensions.mcd 

fanns/R_dev.fann: fms/R.fm dimensions.mcd
	./make_dev.sh TEST ./fanns/R_dev.fann ./alphas/R.alpha ./fms/R.fm dimensions.mcd 

fanns/S_dev.fann: fms/S.fm dimensions.mcd
	./make_dev.sh TEST ./fanns/S_dev.fann ./alphas/S.alpha ./fms/S.fm dimensions.mcd 

fanns/T_dev.fann: fms/T.fm dimensions.mcd
	./make_dev.sh TEST ./fanns/T_dev.fann ./alphas/T.alpha ./fms/T.fm dimensions.mcd 

fanns/U_dev.fann: fms/U.fm dimensions.mcd
	./make_dev.sh TEST ./fanns/U_dev.fann ./alphas/U.alpha ./fms/U.fm dimensions.mcd 
