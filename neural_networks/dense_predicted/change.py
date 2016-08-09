import numpy

fann = open("output.txt", "r")

count = 0
nb_features = 21

total_list = [[] for i in xrange(nb_features)]

for line in fann:
    if count == nb_features:
        count = 0
    line = line.split()
    for element in line:
        if count == 0:
            total_list[count].append(float(element))
        else:
            total_list[count].append(int(element))
    count += 1

form_test = numpy.array([total_list[0]], dtype=numpy.float)
pos_test = numpy.array([total_list[1]], dtype=numpy.uint8)
A_test = numpy.array([total_list[2]], dtype=numpy.uint8)
B_test = numpy.array([total_list[3]], dtype=numpy.uint8)
C_test = numpy.array([total_list[4]], dtype=numpy.uint8)
D_test = numpy.array([total_list[5]], dtype=numpy.uint8)
E_test = numpy.array([total_list[6]], dtype=numpy.uint8)
H_test = numpy.array([total_list[7]], dtype=numpy.uint8)
I_test = numpy.array([total_list[8]], dtype=numpy.uint8)
J_test = numpy.array([total_list[9]], dtype=numpy.uint8)
K_test = numpy.array([total_list[10]], dtype=numpy.uint8)
L_test = numpy.array([total_list[11]], dtype=numpy.uint8)
M_test = numpy.array([total_list[12]], dtype=numpy.uint8)
N_test = numpy.array([total_list[13]], dtype=numpy.uint8)
O_test = numpy.array([total_list[14]], dtype=numpy.uint8)
P_test = numpy.array([total_list[15]], dtype=numpy.uint8)
Q_test = numpy.array([total_list[16]], dtype=numpy.uint8)
R_test = numpy.array([total_list[17]], dtype=numpy.uint8)
S_test = numpy.array([total_list[18]], dtype=numpy.uint8)
T_test = numpy.array([total_list[19]], dtype=numpy.uint8)
U_test = numpy.array([total_list[20]], dtype=numpy.uint8)
numpy.save("./data_test/form_test.npy", form_test)
numpy.save("./data_test/pos_test.npy", pos_test)
numpy.save("./data_test/A_test.npy", A_test)
numpy.save("./data_test/B_test.npy", B_test)
numpy.save("./data_test/C_test.npy", C_test)
numpy.save("./data_test/D_test.npy", D_test)
numpy.save("./data_test/E_test.npy", E_test)
numpy.save("./data_test/H_test.npy", H_test)
numpy.save("./data_test/I_test.npy", I_test)
numpy.save("./data_test/J_test.npy", J_test)
numpy.save("./data_test/K_test.npy", K_test)
numpy.save("./data_test/L_test.npy", L_test)
numpy.save("./data_test/M_test.npy", M_test)
numpy.save("./data_test/N_test.npy", N_test)
numpy.save("./data_test/O_test.npy", O_test)
numpy.save("./data_test/P_test.npy", P_test)
numpy.save("./data_test/Q_test.npy", Q_test)
numpy.save("./data_test/R_test.npy", R_test)
numpy.save("./data_test/S_test.npy", S_test)
numpy.save("./data_test/T_test.npy", T_test)
numpy.save("./data_test/U_test.npy", U_test)
