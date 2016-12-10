import sys

parse = open("hyp", "r")
gold = open("../data/d6.dev.conll07", "r")

pos = {}
cur_sent = []
hasError = 0
for p_line in parse:
    if p_line == '\n':
        if hasError:
            for line in cur_sent:
                print line
        hasError = 0
        cur_sent = []
    else:
        cur_sent.append(p_line)
    g_line = gold.readline()

    if p_line != g_line:
        hasError = 1
        cur_sent.append("##########################"
                +"  " +g_line.split()[6] +" "+g_line.split()[7])
        p_array = p_line.split()
        if p_array[3] not in pos:
            pos[p_array[3]]=1
        else:
            pos[p_array[3]]+=1

#sys.stderr.write(pos)
for key in pos:
    sys.stderr.write(key + "\t"+ str(pos[key]) +"\n")

total = 0
sub_total = 0.0
for key in pos:
    if key == "``" or key == "''" or key == "." or key == "," or key==":":
        sub_total += pos[key]
    total += pos[key]
sys.stderr.write(str(total)+"\n")
sys.stderr.write(str(sub_total/total)+"\n")

