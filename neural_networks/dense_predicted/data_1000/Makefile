#1000_files = numpy_arrays/X_train_A_1000.npy

PATH = numpy_arrays

all: numpy_arrays/X_train_A.npy numpy_arrays/X_test_A.npy



#Makefile commands for generating numpy arrays for model. 
#All are dependent on fann files of same feature type

numpy_arrays/X_train_A.npy: fanns/A_train.fann
	python ../scripts/1000_transform_fann.py A TRAIN

numpy_arrays/X_test_A.npy: fanns/A_dev.fann
	python ../scripts/1000_transform_fann.py A TEST

numpy_arrays/X_train_B.npy: fanns/B_train.fann
	python ../scripts/1000_transform_fann.py B TRAIN

numpy_arrays/X_test_B.npy: fanns/B_dev.fann
	python ../scripts/1000_transform_fann.py B TEST

numpy_arrays/X_train_C.npy: fanns/C_train.fann
	python ../scripts/1000_transform_fann.py C TRAIN

numpy_arrays/X_test_C.npy: fanns/C_dev.fann
	python ../scripts/1000_transform_fann.py C TEST

numpy_arrays/X_train_D.npy: fanns/D_train.fann
	python ../scripts/1000_transform_fann.py D TRAIN

numpy_arrays/X_test_D.npy: fanns/D_dev.fann
	python ../scripts/1000_transform_fann.py D TEST

numpy_arrays/X_train_E.npy: fanns/E_train.fann
	python ../scripts/1000_transform_fann.py E TRAIN

numpy_arrays/X_test_E.npy: fanns/E_dev.fann
	python ../scripts/1000_transform_fann.py E TEST

numpy_arrays/X_train_F.npy: fanns/F_train.fann
	python ../scripts/1000_transform_fann.py F TRAIN

numpy_arrays/X_test_F.npy: fanns/F_dev.fann
	python ../scripts/1000_transform_fann.py F TEST

numpy_arrays/X_train_G.npy: fanns/G_train.fann
	python ../scripts/1000_transform_fann.py G TRAIN

numpy_arrays/X_test_G.npy: fanns/G_dev.fann
	python ../scripts/1000_transform_fann.py G TEST

numpy_arrays/X_train_H.npy: fanns/H_train.fann
	python ../scripts/1000_transform_fann.py H TRAIN

numpy_arrays/X_test_H.npy: fanns/H_dev.fann
	python ../scripts/1000_transform_fann.py H TEST

numpy_arrays/X_train_I.npy: fanns/I_train.fann
	python ../scripts/1000_transform_fann.py I TRAIN

numpy_arrays/X_test_I.npy: fanns/I_dev.fann
	python ../scripts/1000_transform_fann.py I TEST

numpy_arrays/X_train_J.npy: fanns/J_train.fann
	python ../scripts/1000_transform_fann.py J TRAIN

numpy_arrays/X_test_J.npy: fanns/J_dev.fann
	python ../scripts/1000_transform_fann.py J TEST

numpy_arrays/X_train_K.npy: fanns/K_train.fann
	python ../scripts/1000_transform_fann.py K TRAIN

numpy_arrays/X_test_K.npy: fanns/K_dev.fann
	python ../scripts/1000_transform_fann.py K TEST

numpy_arrays/X_train_L.npy: fanns/L_train.fann
	python ../scripts/1000_transform_fann.py L TRAIN

numpy_arrays/X_test_L.npy: fanns/L_dev.fann
	python ../scripts/1000_transform_fann.py L TEST
	
numpy_arrays/X_train_M.npy: fanns/M_train.fann
	python ../scripts/1000_transform_fann.py M TRAIN

numpy_arrays/X_test_M.npy: fanns/M_dev.fann
	python ../scripts/1000_transform_fann.py M TEST

numpy_arrays/X_train_N.npy: fanns/N_train.fann
	python ../scripts/1000_transform_fann.py N TRAIN

numpy_arrays/X_test_N.npy: fanns/N_dev.fann
	python ../scripts/1000_transform_fann.py N TEST

numpy_arrays/X_train_O.npy: fanns/O_train.fann
	python ../scripts/1000_transform_fann.py O TRAIN

numpy_arrays/X_test_O.npy: fanns/O_dev.fann
	python ../scripts/1000_transform_fann.py O TEST

numpy_arrays/X_train_P.npy: fanns/P_train.fann
	python ../scripts/1000_transform_fann.py P TRAIN

numpy_arrays/X_test_P.npy: fanns/P_dev.fann
	python ../scripts/1000_transform_fann.py P TEST

numpy_arrays/X_train_Q.npy: fanns/Q_train.fann
	python ../scripts/1000_transform_fann.py Q TRAIN

numpy_arrays/X_test_Q.npy: fanns/Q_dev.fann
	python ../scripts/1000_transform_fann.py Q TEST

numpy_arrays/X_train_R.npy: fanns/R_train.fann
	python ../scripts/1000_transform_fann.py R TRAIN

numpy_arrays/X_test_R.npy: fanns/R_dev.fann
	python ../scripts/1000_transform_fann.py R TEST

numpy_arrays/X_train_S.npy: fanns/S_train.fann
	python ../scripts/1000_transform_fann.py S TRAIN

numpy_arrays/X_test_S.npy: fanns/S_dev.fann
	python ../scripts/1000_transform_fann.py S TEST

numpy_arrays/X_train_T.npy: fanns/T_train.fann
	python ../scripts/1000_transform_fann.py T TRAIN

numpy_arrays/X_test_T.npy: fanns/T_dev.fann
	python ../scripts/1000_transform_fann.py T TEST

numpy_arrays/X_train_U.npy: fanns/U_train.fann
	python ../scripts/1000_transform_fann.py U TRAIN

numpy_arrays/X_test_U.npy: fanns/U_dev.fann
	python ../scripts/1000_transform_fann.py U TEST

numpy_arrays/X_train_form.npy: fanns/form_train.fann
	python ../scripts/1000_transform_fann.py form TRAIN

numpy_arrays/X_test_form.npy: fanns/form_dev.fann
	python ../scripts/1000_transform_fann.py form TEST

numpy_arrays/X_train_pos.npy: fanns/pos_train.fann
	python ../scripts/1000_transform_fann.py pos TRAIN

numpy_arrays/X_test_pos.npy: fanns/pos_dev.fann
	python ../scripts/1000_transform_fann.py pos TEST

#Makefile commands for generating fann files. All are dependent
#on fm file and mcd file

fanns/A_train.fann: fms/A.fm dimensions.mcd
	./fann_scripts/A_train_fann.sh

fanns/A_dev.fann: fms/A.fm dimensions.mcd
	./fann_scripts/A_dev_fann.sh
		
fanns/B_train.fann: fms/B.fm dimensions.mcd
	./fann_scripts/B_train_fann.sh

fanns/B_dev.fann: fms/B.fm dimensions.mcd
	./fann_scripts/B_dev_fann.sh

fanns/C_train.fann: fms/C.fm dimensions.mcd
	./fann_scripts/C_train_fann.sh

fanns/C_dev.fann: fms/C.fm dimensions.mcd
	./fann_scripts/C_dev_fann.sh

fanns/D_train.fann: fms/D.fm dimensions.mcd
	./fann_scripts/D_train_fann.sh

fanns/D_dev.fann: fms/D.fm dimensions.mcd
	./fann_scripts/D_dev_fann.sh

fanns/E_train.fann: fms/E.fm dimensions.mcd
	./fann_scripts/E_train_fann.sh

fanns/E_dev.fann: fms/E.fm dimensions.mcd
	./fann_scripts/E_dev_fann.sh

fanns/F_train.fann: fms/F.fm dimensions.mcd
	./fann_scripts/F_train_fann.sh

fanns/F_dev.fann: fms/F.fm dimensions.mcd
	./fann_scripts/F_dev_fann.sh

fanns/G_train.fann: fms/G.fm dimensions.mcd
	./fann_scripts/G_train_fann.sh

fanns/G_dev.fann: fms/G.fm dimensions.mcd ./fann_scripts/G_dev_fann.sh fanns/H_train.fann: fms/H.fm dimensions.mcd
	./fann_scripts/H_train_fann.sh

fanns/H_dev.fann: fms/H.fm dimensions.mcd
	./fann_scripts/H_dev_fann.sh

fanns/I_train.fann: fms/I.fm dimensions.mcd
	./fann_scripts/I_train_fann.sh

fanns/I_dev.fann: fms/I.fm dimensions.mcd
	./fann_scripts/I_dev_fann.sh

fanns/J_train.fann: fms/J.fm dimensions.mcd
	./fann_scripts/J_train_fann.sh

fanns/J_dev.fann: fms/J.fm dimensions.mcd
	./fann_scripts/J_dev_fann.sh

fanns/K_train.fann: fms/K.fm dimensions.mcd
	./fann_scripts/K_train_fann.sh

fanns/K_dev.fann: fms/K.fm dimensions.mcd
	./fann_scripts/K_dev_fann.sh

fanns/L_train.fann: fms/L.fm dimensions.mcd
	./fann_scripts/L_train_fann.sh

fanns/L_dev.fann: fms/L.fm dimensions.mcd
	./fann_scripts/L_dev_fann.sh

fanns/M_train.fann: fms/M.fm dimensions.mcd
	./fann_scripts/M_train_fann.sh

fanns/M_dev.fann: fms/M.fm dimensions.mcd
	./fann_scripts/M_dev_fann.sh

fanns/N_train.fann: fms/N.fm dimensions.mcd
	./fann_scripts/N_train_fann.sh

fanns/N_dev.fann: fms/N.fm dimensions.mcd
	./fann_scripts/N_dev_fann.sh

fanns/O_train.fann: fms/O.fm dimensions.mcd
	./fann_scripts/O_train_fann.sh

fanns/O_dev.fann: fms/O.fm dimensions.mcd
	./fann_scripts/O_dev_fann.sh

fanns/P_train.fann: fms/P.fm dimensions.mcd
	./fann_scripts/P_train_fann.sh

fanns/P_dev.fann: fms/P.fm dimensions.mcd
	./fann_scripts/P_dev_fann.sh

fanns/Q_train.fann: fms/Q.fm dimensions.mcd
	./fann_scripts/Q_train_fann.sh

fanns/Q_dev.fann: fms/Q.fm dimensions.mcd
	./fann_scripts/Q_dev_fann.sh

fanns/R_train.fann: fms/R.fm dimensions.mcd
	./fann_scripts/R_train_fann.sh

fanns/R_dev.fann: fms/R.fm dimensions.mcd
	./fann_scripts/R_dev_fann.sh

fanns/S_train.fann: fms/S.fm dimensions.mcd
	./fann_scripts/S_train_fann.sh

fanns/S_dev.fann: fms/S.fm dimensions.mcd
	./fann_scripts/S_dev_fann.sh

fanns/T_train.fann: fms/T.fm dimensions.mcd
	./fann_scripts/T_train_fann.sh

fanns/T_dev.fann: fms/T.fm dimensions.mcd
	./fann_scripts/T_dev_fann.sh

fanns/U_train.fann: fms/U.fm dimensions.mcd
	./fann_scripts/U_train_fann.sh

fanns/U_dev.fann: fms/U.fm dimensions.mcd
	./fann_scripts/U_dev_fann.sh

fanns/form_train.fann: fms/form.fm dimensions.mcd
	./fann_scripts/form_train_fann.sh

fanns/form_dev.fann: fms/form.fm dimensions.mcd
	./fann_scripts/form_dev_fann.sh

fanns/pos_train.fann: fms/pos.fm dimensions.mcd
	./fann_scripts/pos_train_fann.sh

fanns/pos_dev.fann: fms/pos.fm dimensions.mcd
	./fann_scripts/pos_dev_fann.sh

clean:
	-rm io_dimensions_1000.txt
	-rm ./numpy_arrays/*.npy
	-rm ./fanns/*.fann
