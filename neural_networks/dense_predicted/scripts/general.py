import numpy
##########################################################################
# Class for getting a prediction for depedency parser movement given input
# data and a trained model
#
# Forrest Davis
# August 11, 2016
##########################################################################

#Function for transfom fann file into output
#fm and fann file must contain (in any order):
#s0X s1X s2X s3X b0X b1X b2X b3X where X is a feature from the fm file
def fann2numpy(fm_file, fann_file):
    fann = open(fann_file, "r")
    fm = open(fm_file, "r")
    dictionary = {}

    for feature in fm:
        feature = feature.strip('\n')
        #If # at beginning of line skip
        if feature[0] == "#":
            pass
        else:
            fv = fann.readline().strip('\n')
            dim = feature[2:]
            #if feature type (A, f, ...) not in dictionary add it
            #dictionary is in form {X: {s0X: one hot encoding}} for any
            #X in feature file
            if dim not in dictionary:
                #word_embeddings are float objects
                if dim == "f":
                    dictionary[dim] = {}
                    dictionary[dim][feature] = map(float, fv.split())
                else:
                    dictionary[dim] = {}
                    dictionary[dim][feature] = map(int, fv.split())
            else:
                if dim == "f":
                    fv = map(float, fv.split())
                    dictionary[dim][feature] = fv
                else:
                    fv = map(int, fv.split())
                    dictionary[dim][feature] = fv

    #Creating combined list from dictionary
    #Array is in form s0, s1, s2, s3, b0, b1, b2, b3
    for key in dictionary:
        s0=s1=s2=s3=b0=b1=b2=b3 = []
        for subkey in dictionary[key]:
            if "s0" in subkey:
                s0=dictionary[key][subkey]
            if "s1" in subkey:
                s1=dictionary[key][subkey]
            if "s2" in subkey:
                s2=dictionary[key][subkey]
            if "s3" in subkey:
                s3=dictionary[key][subkey]
            if "b0" in subkey:
                b0=dictionary[key][subkey]
            if "b1" in subkey:
                b1=dictionary[key][subkey]
            if "b2" in subkey:
                b2=dictionary[key][subkey]
            if "b3" in subkey:
                b3=dictionary[key][subkey]
                
        #Ensure that there is necessary input for testing on current model 
        assert len(s0) != 0, "s0%s is necessary for model" %key
        assert len(s1) != 0, "s1%s is necessary for model" %key
        assert len(s2) != 0, "s2%s is necessary for model" %key
        assert len(s3) != 0, "s3%s is necessary for model" %key
        assert len(b0) != 0, "b0%s is necessary for model" %key
        assert len(b1) != 0, "b1%s is necessary for model" %key
        assert len(b2) != 0, "b2%s is necessary for model" %key
        assert len(b3) != 0, "b3%s is necessary for model" %key
        
        s0 += s1+s2+s3+b0+b1+b2+b3
        #Create numpy arrays of list
        if key == "A":
            A_test = numpy.array([s0], dtype=numpy.uint8)
        if key == "B":
            B_test = numpy.array([s0], dtype=numpy.uint8)
        if key == "C":
            C_test = numpy.array([s0], dtype=numpy.uint8)
        if key == "D":
            D_test = numpy.array([s0], dtype=numpy.uint8)
        if key == "E":
            E_test = numpy.array([s0], dtype=numpy.uint8)
        if key == "H":
            H_test = numpy.array([s0], dtype=numpy.uint8)
        if key == "I":
            I_test = numpy.array([s0], dtype=numpy.uint8)
        if key == "J":
            J_test = numpy.array([s0], dtype=numpy.uint8)
        if key == "K":
            K_test = numpy.array([s0], dtype=numpy.uint8)
        if key == "L":
            L_test = numpy.array([s0], dtype=numpy.uint8)
        if key == "M":
            M_test = numpy.array([s0], dtype=numpy.uint8)
        if key == "N":
            N_test = numpy.array([s0], dtype=numpy.uint8)
        if key == "O":
            O_test = numpy.array([s0], dtype=numpy.uint8)
        if key == "P":
            P_test = numpy.array([s0], dtype=numpy.uint8)
        if key == "Q":
            Q_test = numpy.array([s0], dtype=numpy.uint8)
        if key == "R":
            R_test = numpy.array([s0], dtype=numpy.uint8)
        if key == "S":
            S_test = numpy.array([s0], dtype=numpy.uint8)
        if key == "T":
            T_test = numpy.array([s0], dtype=numpy.uint8)
        if key == "U":
            U_test = numpy.array([s0], dtype=numpy.uint8)
        if key == "f":
            form_test = numpy.array([s0], dtype=numpy.uint8)
        if key == "p":
            pos_test = numpy.array([s0], dtype=numpy.uint8)
    fann.close()
    fm.close()
    return (A_test, B_test, C_test, D_test, E_test, H_test, I_test, J_test, 
            K_test, L_test, M_test, N_test, O_test, P_test, Q_test, R_test, S_test,
            T_test, U_test, form_test, pos_test)

if __name__ == "__main__":
    fm_file = "U.fm"
    fann_file = "U.fann"

    fann = open(fann_file, "r")
    fm = open(fm_file, "r")
    dictionary = {}
    feats = []
    output = []
    #Get input/output info for model
    info = fann.readline().strip('\n').split()

    #Create a list of features from the fm file
    for feat in fm:
        feat = feat.strip('\n')
        dim = feat[2:]
        #If # at beginning of line skip
        if feat[0] == "#":
            pass
        else:
            feats.append(feat)
            if dim not in dictionary:
                dictionary[dim] = {}
                dictionary[dim][feat] = []
            else:
                dictionary[dim][feat] = []

    #Iterate through fann file and return a dictionary of the form
    #{X: {exact feature(i.e s0A): one hot encodings}} where X is a feature
    feat_num = 0
    num_feats = len(feats)
    for line in fann:
        line = line.strip('\n')
        if line:
            if feat_num == num_feats:
                line = map(int, line.split())
                output.append(line)
                feat_num = 0 
            else:
                feat = feats[feat_num]
                dim = feat[2:]
                #If word embedding need to map to float not int
                if dim == "f":
                    line = map(float, line.split())
                else:
                    line = map(int, line.split())
                fv = dictionary[dim][feat]
                if not fv:
                    dictionary[dim][feat] = [line]
                else:
                    fv.append(line)
                    dictionary[dim][feat] = fv
                feat_num += 1

    for key in dictionary:
        s0=s1=s2=s3=b0=b1=b2=b3 = []
        for subkey in dictionary[key]:
            print subkey, dictionary[key][subkey]
            if "s0" in subkey:
                s0=dictionary[key][subkey]
            if "s1" in subkey:
                s1=dictionary[key][subkey]
            if "s2" in subkey:
                s2=dictionary[key][subkey]
            if "s3" in subkey:
                s3=dictionary[key][subkey]
            if "b0" in subkey:
                b0=dictionary[key][subkey]
            if "b1" in subkey:
                b1=dictionary[key][subkey]
            if "b2" in subkey:
                b2=dictionary[key][subkey]
            if "b3" in subkey:
                b3=dictionary[key][subkey]
        print "s0", s0
        print "s1", s1
        print "s2", s2
        print "s3", s3
        print "b0", b0
        print "b1", b1
        print "b2", b2
        print "b3", b3
        assert len(s0) != 0, "s0%s is necessary for model" %key
        assert len(s1) != 0, "s1%s is necessary for model" %key
        assert len(s2) != 0, "s2%s is necessary for model" %key
        assert len(s3) != 0, "s3%s is necessary for model" %key
        assert len(b0) != 0, "b0%s is necessary for model" %key
        assert len(b1) != 0, "b1%s is necessary for model" %key
        assert len(b2) != 0, "b2%s is necessary for model" %key
        assert len(b3) != 0, "b3%s is necessary for model" %key

        total = [[] for i in xrange(len(s0))]
        print total
        for x in xrange(len(s0)):
            total[x] = s0[x]+s1[x]+s2[x]+s3[x]+b0[x]+b1[x]+b2[x]+b3[x]
        print total[0]

        #Create numpy arrays from dictionary
        data = []
        if key == "A":
            A_test = numpy.array(total, dtype=numpy.uint8)
            data.append(A_test)
        if key == "B":
            B_test = numpy.array(total, dtype=numpy.uint8)
            data.append(B_test)
        if key == "C":
            C_test = numpy.array(total, dtype=numpy.uint8)
            data.append(C_test)
        if key == "D":
            D_test = numpy.array(total, dtype=numpy.uint8)
            data.append(D_test)
        if key == "E":
            E_test = numpy.array(total, dtype=numpy.uint8)
            data.append(E_test)
        if key == "F":
            F_test = numpy.array(total, dtype=numpy.uint8)
            data.append(F_test)
        if key == "G":
            G_test = numpy.array(total, dtype=numpy.uint8)
            data.append(G_test)
        if key == "H":
            H_test = numpy.array(total, dtype=numpy.uint8)
            data.append(H_test)
        if key == "I":
            I_test = numpy.array(total, dtype=numpy.uint8)
            data.append(I_test)
        if key == "J":
            J_test = numpy.array(total, dtype=numpy.uint8)
            data.append(J_test)
        if key == "K":
            K_test = numpy.array(total, dtype=numpy.uint8)
            data.append(K_test)
        if key == "L":
            L_test = numpy.array(total, dtype=numpy.uint8)
            data.append(L_test)
        if key == "M":
            M_test = numpy.array(total, dtype=numpy.uint8)
            data.append(M_test)
        if key == "N":
            N_test = numpy.array(total, dtype=numpy.uint8)
            data.append(N_test)
        if key == "O":
            O_test = numpy.array(total, dtype=numpy.uint8)
            data.append(O_test)
        if key == "P":
            P_test = numpy.array(total, dtype=numpy.uint8)
            data.append(P_test)
        if key == "Q":
            Q_test = numpy.array(total, dtype=numpy.uint8)
            data.append(Q_test)
        if key == "R":
            R_test = numpy.array(total, dtype=numpy.uint8)
            data.append(R_test)
        if key == "S":
            S_test = numpy.array(total, dtype=numpy.uint8)
            data.append(S_test)
        if key == "T":
            T_test = numpy.array(total, dtype=numpy.uint8)
            data.append(T_test)
        if key == "U":
            U_test = numpy.array(total, dtype=numpy.uint8)
            data.append(U_test)
        if key == "f":
            form_test = numpy.array(total, dtype=numpy.float)
            data.append(form_test)
        if key == "p":
            pos_test = numpy.array(total, dtype=numpy.uint8)
            data.append(pos_test)

    Y_test = numpy.array(output, dtype=numpy.uint8)
    data.append(Y_test)
    print data

    
    fann.close()
    fm.close()
