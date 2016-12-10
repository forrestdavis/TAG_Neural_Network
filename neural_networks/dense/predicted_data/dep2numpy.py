import sys
import numpy

train = open("fanns/dep_dev.fann", "r")

info = train.readline().strip("\n").split()

X = []
Y = []
x = []
for line in train:
    line = line.strip("\n").split()
    if line:
        if len(line) == 17:
            Y.append(map(int, line))
            X.append(x)
            x = []
        else:
            x += map(int, line)

print Y[0]
print X[0]

X_numpy = numpy.array(X, dtype=numpy.uint8)
Y_numpy = numpy.array(Y, dtype=numpy.uint8)

numpy.save("X_dep", X_numpy)
numpy.save("Y_dep", Y_numpy)
