#Simple program for checking for features in old dimensions
#results = open("../data/d6.clean2.treepropertiesappo", "r")
results = open("../data/d6.treeproperties", "r")

total = 0

for line in results:
<<<<<<< HEAD
    if " particle:- " in line: 
=======
    if " comp:l" in line: 
>>>>>>> fix_features
        print line[:6]
        total += 1
print total
