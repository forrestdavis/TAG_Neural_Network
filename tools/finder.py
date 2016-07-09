#Simple program for checking for features in old dimensions
results = open("../data/d6.clean2.treepropertiesappo", "r")
#results = open("../data/d6.treeproperties", "r")

total = 0

for line in results:
    if " rel:0 " in line: 
        print line[:6]
        total += 1
print total
