filename = "fifo.tmp"

with open(filename, 'r') as f:
    data = f.read()

array = [int(x) for x in data.split()]

print array
