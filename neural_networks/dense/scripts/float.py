import numpy

ex = open("test.txt", "r")

for line in ex:
    line = map(float, line.strip('\n').split())
    print line

in_array = numpy.fromfile("help.bin", dtype='f8')
print in_array

