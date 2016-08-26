import os

path = "./numpy_arrays"
for filename in os.listdir(path):
    if "test" in filename:
        print filename
        print type(filename)
