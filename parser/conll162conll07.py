import sys

if len(sys.argv) != 3:
    sys.stderr.write("usage: python conll162conll07.py [conll16_file] ["+
            "[conll07_file]\n")
    sys.exit(1)

conll16_name = sys.argv[1]
conll07_name = sys.argv[2]

conll16 = open(conll16_name, "r")
conll07 = open(conll07_name, "w")

for line in conll16:
    if line != "\n":
        line = line.split()
        tmp = (line[0]+"\t"+line[1]+"\t"+line[1]+"\t"+line[3]+"\t"+line[6]+
                "\t"+"_"+"\t"+line[len(line)-2]+"\t"+line[len(line)-1]+
                "\t"+"_"+"\t"+"_"+"\n")
        line = tmp
    conll07.write(line)
