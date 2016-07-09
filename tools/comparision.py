#Simple program to compare the old dimensions to the new dimensions
#takes two input files. Theses files must be a list of trees with a desired
#dimension. To get the dimension use the program finder.py. Prints the
#trees that are not contained in the other treeproperties.
old = open("old_particles_minus.txt", "r")
new = open("new_particles_minus.txt", "r")

old_list = []
for line in old:
    line = line.split(" ")
    old_list.append(line[0])

new_list = []
for line in new:
    line = line.split(" ")
    new_list.append(line[0])

print "additional trees"
for element in new_list:
    if element not in old_list:
        print element
print "------------------------------------------------"
print "missing trees"
for element in old_list:
    if element not in new_list:
        print element
