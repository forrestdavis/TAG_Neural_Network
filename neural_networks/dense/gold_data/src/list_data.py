import sys
#####################################################
# Transforms the one-hot encoding of the fann file for 
# lfronts, rfronts, ladjnodes, radjnodes, dsubcat, 
# dsubcat2 into a vector corresponding to the nodes 
# represented in the list. This way the shared nodes
# between two trees can be accessed during training.
#####################################################

lfront_nodes = [('PP', 's', '2'), ('NP', 's', '0'), ('AdvP', 's', 'X'), 
        ('VP', 's', 'X'), ('IN', 's', 'X'), ('PRT', 's', 'X'), 
        ('PP', 's', 'X'), ('NP', 's', 'X'), ('NP', 's', '1'), 
        ('S', 's', '1'), ('Punct', 's', 'X'), ('S', 's', '0'), 
        ('AP', 's', 'X'), ('VP', 's', '1'), 
        ('NP', 's', '2'), ('AdvP', 's', '2'), ('AdvP', 's', '1'), 
        ('PP', 's', '1'), ('AdvP', 's', '0'), ('S', 's', '2'), 
        ('S', 's', 'X'), ('AP', 's', '2'), ('AP', 's', '0'), 
        ('FRAG', 's', '1'), ('N', 's', 'X'), ('CC', 's', 'X'), 
        ('PP', 's', '0'), ('IN', 's', '0'), ('.', 's', 'X')]

rfront_nodes = [('NP', 's', '1'), ('PP', 's', '2'), ('S', 's', '1'), 
        ('IN', 'c', 'X'),
('S', 's', 'X'), ('NP', 's', 'X'), ('N', 's', 'X'), ('RP', 'c', 'X'), 
('V', 's', '1'), ('AdvP', 's', 'X'), ('NP', 's', '2'), ('S', 's', '2'), 
('PP', 's', 'X'), ('PP', 's', '1'), ('IN', 's', 'X'), ('NP', 's', '0'), 
('FRAG', 's', '1'), ('Punct', 's', 'X'), ('CC', 's', 'X'), 
('AP', 's', '1'), ('.', 's', 'X'), ('Ad', 'c', 'X'), ('UCP', 's', '1'), 
('D', 's', '1'), ('AP', 's', '2'), ('NP', 's', '3'), ('S', 's', '3'),
('PRN', 's', 'X'), ('VP', 's', 'X'), ('Comp', 's', '1'), ('VP', 's', '1'), 
('PRN', 's', '1'), ('PRT', 's', 'X'), ('PP', 's', '0'), ('A', 'c', 'X'), 
('-RRB-', 's', '1'), ('X', 's', 'X'), ('CC', 's', '2'), ('-LRB-', 's', '1'), 
('AdvP', 's', '1'), ('N', 's', '1'), ('A', 's', 'X'), ('IN', 's', '1'), 
('A', 's', '1'), ('S', 's', '0'), ('Ad', 's', '1'), ('N', 'c', 'X'), 
('CC', 's', '1'), ('X', 's', '1'), ('UCP', 's', '2'), ('UH', 's', '1'), 
('AdvP', 's', '2'), ('-RRB-', 's', 'X'), ('Ad', 's', 'X'), ('S', 's', '4'), 
('-LRB-', 's', 'X'), ('AdvP', 's', '0'), ('AP', 's', 'X'), ('FW', 's', '1'),
 ('V', 'c', 'X'), ('INTJ', 's', 'X'), ('G', 's', '1'), ('PP', 's', '3'), 
('NPP', 's', '1'), ('CONJP', 's', 'X'), ('INTJ', 's', '1'), ('VP', 's', '2'), 
('RRC', 's', '1'), ('AP', 's', '3'), ('RP', 's', '1'), ('V', 's', 'X'), 
('MD', 's', '1'), ('NP', 's', '4'), ('PRN', 's', '2')]

ladj_nodes = ['S', 'NP', 'VP', 'V', 'Ad', 'PRN', '-LRB-', 'EX', 'AdvP', 'CONJP', 
'Punct', 'INTJ', 'UH', 'AP', 'POS', 'X', 'D', 'UCP', 'IN', 'A', 'N', 'PP', 
'``', 'CC', "''", 'WP', '.', 'FRAG', 'TO', 'PDT', 'G', 'RRC', 'RP', 'NPP',
'Comp', 'LST', 'QP', '$', 'FW', '-RRB-', 'SYM', 'MD', 'PRT', 'PRT|ADVP', 
'WP$', '-HASHTAG-']

radj_nodes = ['V', 'VP', 'S', 'PP', 'Ad', 'NP', '-LRB-', 'PRN', 'EX', 'AdvP', 
'CONJP', 'PRT', 'Punct', 'UH', 'INTJ', 'AP', 'POS', 'D', 'X', 'UCP', 
'IN', 'A', 'N', '``', 'CC', "''", 'WP', '.', 'FRAG', 'TO', 'PDT', 
'G', 'RRC', 'RP', 'NPP', 'Comp', 'LST', 'QP', '$', 'FW', '-RRB-', 
'SYM', 'MD', 'PRT|ADVP', 'WP$', '-HASHTAG-']

dsub_nodes = [('NP', '0'), ('NP', '1'), ('PP', '2'), ('NP', '2'), ('VP', '1'),
        ('S', '1'), ('V', '1'), ('S', '2'), ('PP', '1'), ('FRAG', '1'), 
        ('AP', '1'), ('S', '0'), ('UCP', '1'), ('D', '1'), ('AP', '2'), 
        ('NP', '3'), ('S', '3'), ('Comp', '1'), ('PRN', '1'), ('AdvP', '2'), 
        ('AdvP', '1'), ('PP', '0'), ('-RRB-', '1'), ('CC', '2'), 
        ('-LRB-', '1'), ('AdvP', '0'), ('N', '1'), ('IN', '1'), 
        ('A', '1'), ('Ad', '1'), ('CC', '1'), ('X', '1'), ('UCP', '2'),
        ('UH', '1'), ('VP', '0'), ('AP', '0'), ('S', '4'), ('VP', '2'),
        ('FW', '1'), ('G', '1'), ('PP', '3'), ('NPP', '1'), ('INTJ', '1'), 
        ('IN', '0'), ('RRC', '1'), ('AP', '3'), ('RP', '1'), 
        ('MD', '1'), ('NP', '4'), ('PRN', '2')]

dsub2_nodes = [('NP', '0'), ('NP', '1'), ('PP', '2'), ('NP', '2'), ('VP', '1'),
 ('S', '1'), ('NP', '1(P)'), ('S', '1(P)'), ('V', '1'), 
('NP', '2(P)'), ('S', '2'), ('PP', '1'), ('NP', '0(P)'), 
('FRAG', '1(P)'), ('S', '2(P)'), ('AP', '1(P)'), 
('S', '0'), ('UCP', '1(P)'), ('D', '1'), ('AP', '2(P)'), 
('D', '1(P)'), ('NP', '3(P)'), ('S', '3'), ('Comp', '1'), 
('PRN', '1(P)'), ('S', '3(P)'), ('AdvP', '2'), ('AdvP', '1'), 
('PP', '0'), ('AP', '1'), ('-RRB-', '1(P)'), ('CC', '2(P)'), 
('-LRB-', '1(P)'), ('VP', '1(P)'), ('AdvP', '0'), 
('AdvP', '1(P)'), ('N', '1(P)'), ('IN', '1(P)'), 
('IN', '1'), ('A', '1(P)'), ('Ad', '1(P)'), ('CC', '1(P)'), 
('X', '1'), ('N', '1'), ('UCP', '2(P)'), ('UH', '1'), ('VP', '0'), 
('AdvP', '2(P)'), ('NP', '3'), ('AP', '2'), ('X', '1(P)'),
 ('AP', '0'), ('S', '4(P)'), ('S', '4'), ('VP', '2'), 
('FW', '1'), ('G', '1'), ('FRAG', '1'), ('A', '1'), ('PP', '3'), 
('NPP', '1'), ('INTJ', '1'), ('Ad', '1'), ('VP', '2(P)'), 
('IN', '0'), ('RRC', '1'), ('AP', '3(P)'), ('RP', '1'), 
('G', '1(P)'), ('MD', '1'), ('NP', '4(P)'), ('PRN', '2(P)')]


if len(sys.argv) != 3:
    sys.stderr.write("Usage: python list_data.py <feature>"+
            " <TRAIN or TEST>\n")
    sys.exit(1)

vocab_filename = "alphas/"+sys.argv[1]+".alpha"
if sys.argv[2] == "TRAIN":
    fann_filename = "fanns/"+sys.argv[1]+"_train.fann"
if sys.argv[2] == "TEST":
    fann_filename = "fanns/"+sys.argv[1]+"_dev.fann"
output_filename = sys.argv[1]+"_output.fann"
vocab_file = open(vocab_filename, "r")
vocab = [] 

isFeat = 0
feat = sys.argv[1]
if feat == "D":
    data = lfront_nodes
if feat == "E":
    data = rfront_nodes
if feat == "F":
    data = ladj_nodes
if feat == "G":
    data = radj_nodes
if feat == "O":
    data = dsub_nodes
if feat == "P":
    data = dsub2_nodes

nb_type = 0
for line in vocab_file:
    line = line.strip("\n")
    if line == feat:
        isFeat = 1
    elif isFeat:
        if line.isdigit():
            nb_type = int(line)
        isFeat = 0
    elif nb_type:
        vocab.append(line)
        nb_type -= 1

vocab_file.close()

fann_file = open(fann_filename, "r")
output_file = open(output_filename, "w")

info = fann_file.readline().split()
output = int(info[2])
output_file.write(info[0] + '\t'+ str(len(data)*8)+" "+str(output)+'\n')
isInput = 1
if feat == "D" or feat == "E":
    for line in fann_file:
        line = line.strip("\n")
        if line:
            if len(line) != output*2-1:
                line = line.split()
                nb = -1
                for x in xrange(len(line)):
                    if line[x] == "1":
                        nb = x 
                if nb == -1:
                    node = [("nil")]
                else:
                    node = vocab[nb]
                    node = node.split("_")
                    for x in xrange(len(node)):
                        node[x] = tuple(node[x].split("#"))
                out = []
                for x in xrange(len(data)):
                    hasElement = 0
                    for element in node:
                        if data[x] == element:
                            hasElement = 1
                    if hasElement:
                        out.append("1")
                    else:
                        out.append("0")
                for element in out:
                    output_file.write(element + " ")
                output_file.write("\n")
            else:
                output_file.write("\n")
                output_file.write(line + "\n")
                output_file.write("\n\n")
if feat == "F" or feat == "G":
    for line in fann_file:
        line = line.strip("\n")
        if line:
            if len(line) != output*2-1:
                line = line.split()
                nb = -1
                for x in xrange(len(line)):
                    if line[x] == "1":
                        nb = x 
                if nb == -1:
                    node = [("nil")]
                else:
                    node = vocab[nb]
                    node = node.split("_")
                out = []
                for x in xrange(len(data)):
                    hasElement = 0
                    for element in node:
                        if data[x] == element:
                            hasElement = 1
                    if hasElement:
                        out.append("1")
                    else:
                        out.append("0")
                for element in out:
                    output_file.write(element + " ")
                output_file.write("\n")
            else:
                output_file.write("\n")
                output_file.write(line + "\n")
                output_file.write("\n\n")
if feat == "O" or feat == "P":
    for line in fann_file:
        line = line.strip("\n")
        if line:
            if len(line) != output*2-1:
                line = line.split()
                nb = -1
                for x in xrange(len(line)):
                    if line[x] == "1":
                        nb = x 
                if nb == -1:
                    node = [("nil")]
                else:
                    node = vocab[nb]
                    node = node.split("_")
                    for x in xrange(len(node)):
                        node[x] = tuple(node[x].split("#"))
                out = []
                for x in xrange(len(data)):
                    hasElement = 0
                    for element in node:
                        if data[x] == element:
                            hasElement = 1
                    if hasElement:
                        out.append("1")
                    else:
                        out.append("0")
                for element in out:
                    output_file.write(element + " ")
                output_file.write("\n")
            else:
                output_file.write("\n")
                output_file.write(line + "\n")
                output_file.write("\n\n")
fann_file.close()
output_file.close()
