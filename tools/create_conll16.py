#Function that takes a conll07 file and appends the dimensions 
#corresponding to the stag for the word. 
import sys

def createDecompressFile(dimensions, old_conll, output_file):
    dimensions_list = []
    with open(dimensions, 'r') as dimensions:
        for line in dimensions:
            dimensions_list.append(line.split())
        for i in range(1, len(dimensions_list)):
            j = i
            while j>0 and dimensions_list[j][0]<dimensions_list[j-1][0]:
                dimensions_list[j], dimensions_list[j-1] = dimensions_list[j-1], dimensions_list[j]
                j -= 1

    number_of_dimensions = len(dimensions_list[0])-1
    with open(output_file, 'w') as output:
        with open(old_conll, 'r') as old_conll:
            train_list = []
            for line in old_conll:
                tmp_list = line.split('\t')
                if len(tmp_list) == 10:
                    values = [tmp_list[0],tmp_list[1],tmp_list[3][0],
                            tmp_list[3],tmp_list[6],tmp_list[7],tmp_list[4]]
                    for element in values:
                        output.write(element + '\t')
                    if tmp_list[4] == 'tCO':
                        for x in xrange(0, number_of_dimensions - 1):
                            output.write('NA' + '\t')
                        output.write('NA' +'\n')
                    else:
                        searchTree = int(tmp_list[4][1:])
                        for x in xrange(1,len(dimensions_list[searchTree])
                                - 1):
                            element = dimensions_list[searchTree][x]
                            element = element.split(':')
                            output.write(element[1] + '\t')
                        element = dimensions_list[searchTree][x+1]
                        element = element.split(':')
                        output.write(element[1] + '\n')
                elif tmp_list[0] == '\n':
                    output.write('\n')
if __name__ == '__main__':

    if len(sys.argv) != 4:
        sys.stderr.write("Usage: python create_conll16.py " + 
        "<suptertags_file> <old_conll_file> <name_of_output_file>\n")
        sys.exit(1)

    dimensions = sys.argv[1]
    old_conll = sys.argv[2]
    output_file = sys.argv[3]
    createDecompressFile(dimensions, old_conll, output_file)
