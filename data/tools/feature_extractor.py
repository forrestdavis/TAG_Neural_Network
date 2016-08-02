#Extracts dimensions from TAG grammar
#Not optimized to ensure that each feature is its own function
#Sample output:
#t30 root:G dir:LEFT modif:NP lfronts:nil rfronts:nil ladjnodes:NP_G 
#radjnodes:G_NP substnodes:nil predaux:FALSE coanc:FALSE particle:NA 
#particleShift:NA comp:n pred:FALSE dsubcat:nil dsubcat2:nil 
#datshift:NA esubj:NA rel:NA wh:NA voice:NA
#
#A more detailed explanation of the differences between the previous 
#work on dimensions and the new dimensions can be found in 
#dimension_updates.txt, new_stats.txt and old_stats.txt
#
#Forrest Davis
#June 2016
#Written for Python version 2.7.11

import sys

#Function that extracts dimensions from the grammar. It returns
#a list of labels for the dimensions and a list of values for the
#dimensions. The label and value indices correspond to each other.
#The current options are (exact return output is detailed in their
# individual functions):
#   trees, root, dir, modif, lfronts, rfonts, ladjnodes, radjnodes,
#   substnodes, predaux, coanc, particle, particleShift, lcomp, rcomp, 
#   pred, dsubcat, dsubcat2, datshift, esubj, rel, wh, voice
def getDimensions(grammar):
    #want to get each tree and add it to a list
    #So you will have a list where each entry is a tree and
    #then each node will be a list of five components taken from the 
    #format of the grammar file:
    #TAG, ARUGUMENT_NUMBER, NODE_NUMBER, TRAVERSAL, NODE_CATEGORY
    #for example NP#0#2#l#s will become [NP, 0, 2, 1, s]
    tree_list = [] 
    for tree in grammar:
        #Make list from line in file
        temporary_list = tree.split()
        #break each node into its components
        for x in xrange(0, len(temporary_list)):
            #Handles # part of speech by temporary ignoring it
            #so that the splitting of components works correctly
            if temporary_list[x][0] == '#':
                temporary_list[x] = temporary_list[x][1:]
            #Split node into components
            temporary_list[x] = temporary_list[x].split('#', 4)
            #Adds back the hastag part of speech
            if temporary_list[x][0] == "":
                temporary_list[x][0] += "-HASHTAG-"
        tree_list.append(temporary_list)
    
    #Get individual dimensions
    roots = getRoots(tree_list)
    directions = getDirections(tree_list)
    modifs = getModifs(tree_list)
    lfronts = getLFronts(tree_list)
    rfronts = getRFronts(tree_list)
    ladjnodes = getLAdjNodes(tree_list)
    radjnodes = getRAdjNodes(tree_list)
    predauxs = getPredAuxs(tree_list)
    coancs = getCoAncs(tree_list)
    preds = getPreds(tree_list)
    particles = getParticles(tree_list)
    comps = getComps(tree_list)
    dsubcats = getDSubCats(tree_list)
    dsubcats2 = getDSubCats2(tree_list)
    shifts = getParticleShifts(tree_list)
    datshifts = getDatShifts(tree_list)
    esubjs = getESubjs(tree_list)
    rels = getRels(tree_list)
    whs = getWhs(tree_list)
    voices = getVoices(tree_list)
    substnodes = getSubstnodes(tree_list)
    #appos = getAppos(tree_list)

    dimension_labels = ["tree", "root", "dir", "modif", "lfronts", 
            "rfronts", "ladjnodes", "radjnodes", "substnodes", "predaux",
            "coanc", "particle", "particleShift", "comp", 
            "pred", "dsubcat", "dsubcat2", "datshift", "esubj", "rel", 
            "wh", "voice"]
    dimension_values = [tree_list, roots, directions, modifs, lfronts, 
            rfronts, ladjnodes, radjnodes, substnodes, predauxs, coancs, 
            particles, shifts, comps, preds, dsubcats, dsubcats2, 
            datshifts, esubjs, rels, whs, voices]

    #Ensures that labels and values are the same length so that output
    #formatting is correct
    if len(dimension_labels) != len(dimension_values):
        print("There are a different amount of dimension labels than "+
        "dimension values being returned. Ensure that if you have edited"+
        " the return of getDimensions that you have changed both the "+
        "labels and the values that you are returning.")
        sys.exit(1)

    return dimension_labels, dimension_values
    
#Function to get root of tree. Returns the tag on the root of the tree.
def getRoots(tree_list):
    roots = [] 
    #Iterate through grammar trees and check if they are an auxiliary tree
    for tree in tree_list:
        #check if modifier auxiliary tree
        #check if in right position
        if tree[2][4] == 'f':
            roots.append(tree[4][0])
        #check if in left position
        elif tree[len(tree)-2][4] == 'f':
            roots.append(tree[2][0])
        #Else not a modifier auxiliary tree so root is first node
        else:
            roots.append(tree[1][0])
    return roots

#Function to get direction of the foot node for modifier auxiliary trees
#else NA
def getDirections(tree_list):
    directions = [] 
    #Iterate through trees and if foot node is in the 2nd node than the 
    #direction is right. If the the foor node is in the 2nd from end node
    #than the direction is left. Else direction does not apply
    for tree in tree_list:
        if tree[2][4] == 'f':
            directions.append("RIGHT")
        elif tree[len(tree)-2][4] == 'f':
            directions.append("LEFT")
        else:
            directions.append("NA") 
    return directions 

#Function to get the category of the actual root node of the modifier 
#auxiliary tree i.e. the category of the foot node; otherwise returns NA
def getModifs(tree_list):
    modifs = [] 
    #Iterate through trees and if tree is an auxulary tree grab the foot 
    #node which is the true root of the true
    for tree in tree_list:
        if tree[2][4] == 'f':
            modifs.append(tree[2][0])
        elif tree[len(tree)-2][4] == 'f':
            modifs.append(tree[len(tree)-2][0])
        else:
            modifs.append("NA")
    return modifs

#Function to get left frontier nodes, which are any node to the left of
#the anchor that are substitution nodes. Returns a list for each tree 
#that contains only the left traversal of frontier nodes. Returns nil
#if there are no frontier nodes.
def getLFronts(tree_list):
    lfronts = []
    for tree in tree_list:
        temporary_list = [] 
        #Continue through list till you hit the head node checking
        #for nodes that can be substituted 
        for x in xrange(1, len(tree)):
            if tree[x][4] == 's' and tree[x][3] == 'l':
                temporary_list.append(tree[x])
            elif tree[x][4] == 'c' and tree[x][3] == 'l':
                temporary_list.append(tree[x])
            elif tree[x][4] == 'h':
                break
        #If there are no left frontier nodes return nil
        if len(temporary_list) == 0:
            temporary_list.append(["nil"])
        lfronts.append(temporary_list)
    return lfronts

#Function to get right frontier nodes. Same process as getLFronts but
#gets frontier nodes to the right of the anchor.
def getRFronts(tree_list):
    rfronts = []
    for tree in tree_list:
        temporary_list = [] 
        head_position = 0
        #move through nodes till you hit the head node, mark current 
        #position and then break
        for x in xrange(1, len(tree)):
            if tree[x][4] == 'h':
                head_position = x
                break
        #move through nodes from the head till the end grabbing all nodes 
        #that can be substituted 
        for y in xrange(head_position, len(tree)):
            if tree[y][4] == 's' and tree[y][3] == 'l': 
                temporary_list.append(tree[y]) 
            elif tree[y][4] == 'c' and tree[y][3] == 'l': 
                temporary_list.append(tree[y]) 
        #If there are no right frontier nodes return nil
        if len(temporary_list) == 0:
            temporary_list.append(["nil"])
        rfronts.append(temporary_list)
    return rfronts

#Function to get left adjunction nodes. It goes through each tree, in each
#tree it goes through each node and checks for a few things. The root node
#is an adjunction node if the true is not a modifier auxiliary tree. I 
#check this by seeing if there is a direction associated with the tree. If
#it is NA than the tree is not a modifier auxiliary tree and the root is
#a adjunction node. Then all other nodes are adjunction nodes as long as 
#they are not a substitution node or a foot node. Both the left and right
#crossing of a node are considered and the left travarsel of the head is 
#considered as well
#currently changed to only mark nodes one time
def getLAdjNodes(tree_list):
    ladjnodes = []
    directions = getDirections(tree_list)
    #Iterate through every tree
    for x in xrange(len(tree_list)):
        temporary_list = [] 
        for y in xrange(1, len(tree_list[x])):
            '''
            if y == 1:
                temporary_list.append(tree_list[x][y])
            '''
            if (tree_list[x][y][4] != "s" 
            and tree_list[x][y][4] != "f" 
            and tree_list[x][y][4] != "c"
            and tree_list[x][y][0] != "-NONE-"
            and tree_list[x][y][3] == "l"
            and tree_list[x][y][4] != "h"):
                temporary_list.append(tree_list[x][y])
            if tree_list[x][y][4] == 'h':
                break
        if temporary_list:
            ladjnodes.append(temporary_list)
        else:
            ladjnodes.append(["nil"])

    return ladjnodes


#Same as getRAdjNodes but looks for adjunction nodes to the right of the 
#head including the right traversal of the head node.
def getRAdjNodes(tree_list):
    radjnodes = []
    directions = getDirections(tree_list)
    for x in xrange(len(tree_list)):
        temporary_list = [] 
        #Find head node position
        for y in xrange(1, len(tree_list[x])):
            if tree_list[x][y][4] == 'h' and tree_list[x][y][3] == 'r':
                break
        #move through nodes from the head till the end grabbing all nodes 
        for z in xrange(y+1, len(tree_list[x])):
            if z == (len(tree_list[x])-1):
                temporary_list.append(tree_list[x][z])
            elif (z < (len(tree_list[x])-1) and tree_list[x][z][4] != "s" 
            and tree_list[x][z][4] != "f" and tree_list[x][z][4] != "c"
            and tree_list[x][z][0] != "-NONE-" and tree_list[x][3] == "l"):
                temporary_list.append(tree_list[x][z])
        if temporary_list:
            radjnodes.append(temporary_list)
        else:
            radjnodes.append(["nil"])

    return radjnodes

#Function that returns TRUE if a tree is a predicative auxiliary tree else
#FALSE. It does this by looking for a tree with a foot node that has a NA 
#direction which means it is not a modifier auxilary tree. 
def getPredAuxs(tree_list):
    predauxs = []
    directions = getDirections(tree_list)
    for x in xrange(len(tree_list)):
        isPredAux = 0 
        for y in xrange(1, len(tree_list[x])):
            if tree_list[x][y][4] == 'f' and directions[x] == "NA":
                if tree_list[x][y][3] == 'l':
                    isPredAux = 1
        if isPredAux == 0:
            predauxs.append("FALSE")
        else:
            predauxs.append("TRUE")

    return predauxs

#Function to check if tree has a co-anchor. It does this by moving through
#the trees and looking for a node that has a "c" in its 4 index. Returns
#TRUE if there is a co-anchor else it returns FALSE.
def getCoAncs(tree_list):
    coancs = [] 
    for tree in tree_list:
        isCoanc = 0
        for x in xrange(1, len(tree)):
            if tree[x][4] == "c":
                isCoanc = 1
                Coanc = tree[x][0]
        if isCoanc == 0:
            coancs.append("FALSE")
        else:
            #coancs.append("TRUE")
            coancs.append(Coanc)
    return coancs

#Function to check if a tree has a particle. It does this by looking for a
#node in the tree that is tagged with PRT. Not marking a distinction
#between shifted and not shifted particles. Checks if tree is verbal i.e.
#it has a verb or it is a tree with a predicative structure. If it is then 
#it returns TRUE if there is a particle else it returns FALSE. If it 
#is not a verbal tree than it returns NA. Currently returns more than 
#previous work.
def getParticles(tree_list):
    particles = []
    preds = getPreds(tree_list)
    for x in xrange(len(tree_list)):
        hasPart = 0
        isVerbal = 0
        #if tree has a predicate structure than it is verbal
        if preds[x] == "TRUE":
            isVerbal = 1
        for y in xrange(1, len(tree_list[x])):
            #if tree has a VP or a V than it is verbal
            if tree_list[x][y][0] == "VP" or tree_list[x][y][0] == "V":
                isVerbal = 1
            #if tree has PRT than it has a particle. PRT|ADVP catches one 
            #special node that contains a particle but written like that.
            if(tree_list[x][y][0] == "PRT" 
            or tree_list[x][y][0] == "PRT|ADVP" or
            tree_list[x][y][0] == "RP"):
                hasPart = 1
        if hasPart:
            particles.append("TRUE")
        elif hasPart == 0 and isVerbal == 1:
            particles.append("FALSE")
        else:
            particles.append("NA")

    return particles

#Checks to see if a tree with a particle has particle shift. It does this
#by checking if there is a NP node following the V meaning the verb is 
#first followed by a noun phrase before a particle. Returns YES if that is
#the case, NO if there is no shift or NA if the tree is non-verbal, 
#meaning a particle isn't considered.
def getParticleShifts(tree_list):
    shifts = [] 
    particles = getParticles(tree_list)
    for x in xrange(len(tree_list)):
        isShifted = 0
        if particles[x] == "TRUE":
            for y in xrange(1, len(tree_list[x])):
                #if at V node
                if tree_list[x][y][4] == "h" and tree_list[x][y][3] == "r":
                    #If the following node is a NP than it is shifted
                    if len(tree_list[x]) > y+1:
                        if tree_list[x][y+1][0] == "NP":
                            isShifted = 1
            if isShifted:
                shifts.append("YES")
            else:
                shifts.append("NO")
        else:
            shifts.append("NA")
    return shifts

#Function that determines if a tree has a complementizer. It returns three
#options. Theses are l if there is a left complementizer, r if there is a
#right complementizer or n if there is no complementizer
def getComps(tree_list):
    comps = [] 
    for tree in tree_list:
        isComp = (0, 0)
        isLeft = 1
        for x in xrange(1, len(tree)):
            if tree[x][4] == "h":
                isLeft = 0
            if tree[x][0] == "IN" and tree[x][1] == "c":
                if tree[x-1][0] == "S" or tree[x+1][0] == "S":
                    if isLeft:
                        isComp = (1,0)
                    else:
                        isComp = (0,1)
        if isComp == (0, 0):
            comps.append("n")
        elif isComp == (1, 0):
            comps.append("l")
        else:
            comps.append("r")
    return comps

#Function to check if a tree is a nominal, adjectival, or prepositional
#tree which projects a predicative structure. It does this by seeing if
#the head node is a N, A, or IN node and if that node is connected to a 
#S node. It utilizes a stack to traverse the tree. Nodes on the stack
#are connected. It returns TRUE if it is a predicative tree else it 
#returns FALSE.
def getPreds(tree_list):
    preds = [] 
    directions = getDirections(tree_list)
    for x in xrange(len(tree_list)):
        isPred = 0
        stack = []
        for y in xrange(1, len(tree_list[x])):
            #If the tree is a modifier auxilary tree than the root node
            #is not considered
            if y == 1 and directions[x] == "NA":
                stack.append(tree_list[x][y][0])
            if (y > 1 and y < (len(tree_list[x])-1) 
                    and tree_list[x][y][4] != "f"):
                if tree_list[x][y][3] == "l":
                    stack.append(tree_list[x][y][0])
                else:
                    stack.pop()
            if y == len(tree_list[x])-1 and directions[x] == "NA":
                stack.pop()
            if tree_list[x][y][4] == "h":
                #Looks for predicative structure
                if((tree_list[x][y][0] == "A" or tree_list[x][y][0] == "N"
                or tree_list[x][y][0] == "IN") 
                and tree_list[x][y][3] == "l" and "S" in stack):
                    isPred = 1
        if isPred == 0:
            preds.append("FALSE")
        else:
            preds.append("TRUE")
    return preds

#Function that gets all the deep subcategorization frame nodes. It returns
#a list with each element corresponding to a tuple of the category of the
#node and the argument number. The list is ordered by argument number. 
#It finds the nodes by looking for a argument number in index 1 of the 
#node. 
def getDSubCats(tree_list):
    dsubcats = []
    for tree in tree_list:
        temporary_list = [] 
        for x in xrange(1, len(tree)):
            #Checks for an argument number
            if tree[x][1].isdigit() and tree[x][3] == "l":
                temporary_list.append((tree[x][0], tree[x][1]))
        if len(temporary_list) == 0:
            dsubcats.append([("nil")])
        else:
            #Insertion sort on nodes to order based on argument
            for i in range(1, len(temporary_list)):
                j = i
                while j>0 and temporary_list[j][1]<temporary_list[j-1][1]:
                    temporary_list[j], temporary_list[j-1] = (
                            temporary_list[j-1], temporary_list[j])
                    j -= 1

            dsubcats.append(temporary_list)
    return dsubcats

#Same process as DSubCats but notes if the dsubcat nodes are attached to a
#PP. It does this by using a stack that has all the current parent nodes of
#the node in it. Returns same values as DSubCats except an added tuple 
#index for (P)
def getDSubCats2(tree_list):
    dsubcats2 = []
    dsubcats = getDSubCats(tree_list)
    for x in xrange(len(tree_list)):
        temporary_list = []
        if dsubcats[x][0] != "nil":
            stack = [] 
            for y in xrange(1, len(tree_list[x])):
                if tree_list[x][y][3] == "l":
                    stack.append(tree_list[x][y][0])
                if tree_list[x][y][3] == "r":
                    stack.pop()
                if(tree_list[x][y][1].isdigit() and 
                   tree_list[x][y][3] == "l"):
                    if "PP" in stack and tree_list[x][y][0] != "PP":
                        temporary_list.append((tree_list[x][y][0], 
                            tree_list[x][y][1], "(P)"))
                    else:
                        temporary_list.append((tree_list[x][y][0], 
                            tree_list[x][y][1]))
            #Insertion sort on nodes to order based on argument
            for i in range(1, len(temporary_list)):
                j = i
                while j>0 and temporary_list[j][1]<temporary_list[j-1][1]:
                    temporary_list[j], temporary_list[j-1] = (
                            temporary_list[j-1], temporary_list[j])
                    j -= 1

            dsubcats2.append(temporary_list)
        else:
            dsubcats2.append([("nil")])
    return dsubcats2 

#Function that takes the trees as an input and returns a list of child
#nodes. For each node in the tree it finds the children directly under the
#node. It returns a list where the first element always corresponds to the 
#current node, followed by any children nodes it may have. If it is the
#right traversal of a node than it returns a blank list. Each node is 
#represented by its tag(index 0), argument number(index 1), its node
#number(index 2) and its substitution or foot information(index 3). 
def getDirectChildNodes(tree_list):
    directChildNodes = []
    tree = tree_list[2683]
    for x in xrange(len(tree_list)):
        tree = tree_list[x]
        temporary_list = []
        temporary_list.append(tree_list[x][0])
        #for each node in the tree traverse the rest of the tree marking
        #any nodes that are the direct child of the current node
        for y in xrange(1, len(tree)):
            children_list = []
            if tree[y][3] == "l":
                children_list.append(
                        (tree[y][0], tree[y][1], tree[y][2], tree[y][4]))
            isChild = 1
            for z in xrange(y+1, len(tree)):
                if len(children_list) != 0:
                    if isChild and tree[z][3] == "l":
                        children_list.append((tree[z][0], 
                                tree[z][1], tree[z][2], tree[z][4]))
                        isChild = 0
                    if((tree[z][0], tree[z][1], tree[z][2], tree[z][4]) 
                            == children_list[0]):
                        break
                    elif(not isChild and 
                    (tree[z][0], tree[z][1], tree[z][2], tree[z][4]) 
                    in children_list and tree[z][3] == "r"):
                        isChild = 1
            temporary_list.append(children_list)
        directChildNodes.append(temporary_list)
    return directChildNodes

#Function that checks if a tree has dative shift. If the tree has a 
#ditransitive verb it returns YES if there is dative shift, and NO if there
#is not. If the tree does not have a ditransitive verb it returns NA.
def getDatShifts(tree_list):
    datshifts = [] 
    #List of each node with its direct children
    directChildNodes = getDirectChildNodes(tree_list)
    for x in xrange(len(tree_list)):
        tree = tree_list[x]
        isDitransitive = 0
        hasShift = 0 
        #Iterate through the nodes of the tree checking if the current 
        #node is a VP. If it is it checks to see how many NP children it
        #has.
        for y in xrange(1, len(tree)):
            if len(directChildNodes[x][y]) != 0:
                if directChildNodes[x][y][0][0] == "VP":
                    number_NP = 0
                    NP_list = []
                    for node in directChildNodes[x][y]:
                        if node[0] == "NP":
                            NP_list.append(node)
                            number_NP += 1
                    if number_NP >= 2:
                        isDitransitive = 1
                        #If NP argument numbers are out of order has
                        #dative shift
                        if NP_list[1][1] == "1" or NP_list[0][1] == "2":
                            hasShift = 1
                        #If two NPs are children of VP and they are 
                        #directly next to each other than must have
                        #dative shift
                        if NP_list[0][1] == "" and NP_list[1][1] == "":
                            if (int(NP_list[1][2])-int(NP_list[0][2]))==2:
                                hasShift = 1
        if isDitransitive and not hasShift:
            datshifts.append("NO")
        elif isDitransitive and hasShift:
            datshifts.append("YES")
        elif not isDitransitive:
            datshifts.append("NA")
    return datshifts

#Function to check if the tree has no expressed subject. It does this
#by checking that each S in the tree with a NP has a trace under it's
#NP. The function returns YES if there is no expressed subject, NO
#if there is an expressed subject, or NA if the tree is non-verbal
def getESubjs(tree_list):
    esubjs = []
    #Gets list of nodes and their children
    directChildNodes = getDirectChildNodes(tree_list)
    preds = getPreds(tree_list)
    for x in xrange(len(tree_list)):
        tree = tree_list[x]
        NP_nodes = []
        seenNP = 0
        isVerbal = 0
        #Checks if verbal
        if preds[x] == "TRUE":
            isVerbal = 1
        for y in xrange(1, len(tree)):
            children = directChildNodes[x][y]
            if children:
                #Checks if verbal
                if children[0][0] == "VP" or children[0][0] == "V":
                    isVerbal = 1
                #If node is a S look at children
                if children[0][0] == "S":
                    if len(children) > 1:
                        #If has NP node child with argument number
                        if(children[1][0] == "NP" and 
                                children[1][1].isdigit()):
                            NP_nodes.append(children[1])
                            seenNP = 1
                #Pops NP node from list if it has a trace 
                if children[0] in NP_nodes:
                    if len(children) == 2:
                        if children[1][0] == "-NONE-":
                            NP_nodes.pop(0)
        #If all NP list is empty and there has been a NP then
        #they must be all traces and the tree has no subject
        if not NP_nodes and seenNP:
            esubjs.append("YES")
        elif not isVerbal:
            esubjs.append("NA")
        else:
            esubjs.append("NO")
    return esubjs
    
#Function that returns if a tree is passive or active.
#Specific return is pas_by if the tree represents a verb that expresses
#passive through the use of by i.e "inflated by", else pas if the tree
#is passive, act if the tree is active, or NA if non-verbal.
#Differences in results from old work is detailed in dimension_updates.txt
def getVoices(tree_list):
    voices = []
    for x in xrange(len(tree_list)):
        #Each pattern represents a different passive tree structure
        #I tried to keep it as general as possible but often general
        #overproduced. This is the smallest number I could use to get all
        #the passive trees. If a pattern is empty at the end and any 
        #further restrictions are met through notPAS variables then 
        #the tree is passive
        #PAS_PP represents pas_by pattern
        PAS_PP_1_pattern = [("VP", "", "l"), ("NP", "*", "l"), 
                       ("-NONE-", "","l"), ("-NONE-", "","r"), 
                       ("NP", "*","r"), ("PP", "", "l"), 
                       ("IN", "", "l"), ("IN", "", "r"), 
                       ("NP", "0", "l"), ("NP", "0", "r"), 
                       ("PP", "", "r"), ("VP", "", "r")]
        PAS_PP_2_pattern = [("S", "", "l"), ("NP", "1", "l"), 
                       ("NP", "1", "r"), ("VP", "","l"), ("PP", "","l"), 
                       ("IN", "","l"), ("IN", "","r"), 
                       ("NP", "0", "l"), ("NP", "0", "r"), 
                       ("PP", "", "r"), ("VP", "", "r"), ("S", "", "r")]
        PAS_PP_3_pattern = [("S", "", "l"), ("NP", "a", "l"), 
                       ("NP", "a", "r"), ("VP", "","l"), ("PP", "","l"), 
                       ("IN", "","l"), ("IN", "","r"), 
                       ("NP", "", "l"), ("NP", "", "r"), 
                       ("PP", "", "r"), ("VP", "", "r"), ("S", "", "r")]
        PAS_PP_4_pattern = [("S", "", "l"), ("NP", "", "l"), 
                       ("-NONE-", "", "l"), ("-NONE-", "", "r"), 
                       ("NP", "", "r"), ("VP", "", "l"), ("V", "", "l"),
                       ("V", "", "r"), ("PP", "", "l"), ("IN", "", "l"),
                       ("IN", "", "r"), ("NP", "1", "l"), ("NP", "1", "r"),
                       ("PP", "", "r"), ("VP", "", "r"), ("S", "", "r")]
        PAS_PP_5_pattern = [("S", "", "l"), ("NP", "a", "l"), 
                       ("NP", "a", "r"), ("VP", "", "l"), ("NP", "", "l"),
                       ("-NONE-", "", "l"), ("-NONE-", "", "r"), 
                       ("NP", "", "r"), ("PP", "a", "l"), ("PP", "a", "r"),
                       ("VP", "", "r"), ("S", "", "r")]
        PAS_1_pattern = [("S", "", "l"), ("NP", "1", "l"), 
                       ("NP", "1", "r"), ("VP", "", "l"), 
                       ("VP", "", "r"), ("S", "", "r")]
        PAS_2_pattern = [("S", "", "l"), ("NP", "2", "l"), 
                       ("NP", "2", "r"), ("VP", "", "l"), 
                       ("V", "", "l"), ("V", "", "r"), 
                       ("NP", "", "l"), ("-NONE-", "", "l"), 
                       ("-NONE-", "", "r"), ("NP", "", "r"), 
                       ("NP", "1", "l"), ("NP", "1", "r"),
                       ("VP", "", "r"), ("S", "", "r")]
        PAS_3_pattern = [("S", "", "l"), ("NP", "a", "l"), 
                       ("NP", "a", "r"), ("VP", "", "l"), ("NP", "", "l"), 
                       ("-NONE-", "", "l"), ("-NONE-", "", "r"), 
                       ("NP", "", "r"), ("VP", "", "r"), 
                       ("S", "", "r")]
        PAS_4_pattern = [("S", "", "l"), ("S", "1", "l"), 
                       ("S", "1", "r"), ("VP", "", "l"), 
                       ("V", "", "l"), ("V", "", "r"),
                       ("S", "2", "l"), ("S", "2", "r"),
                       ("VP", "", "r"), ("S", "", "r")]
        PAS_5_pattern = [("S", "", "l"), ("VP", "", "l"), 
                       ("VP", "", "r"), ("NP", "1", "l"), 
                       ("NP", "1", "r"), ("S", "", "r")]
        PAS_6_pattern = [("VP", "", "l"), ("V", "", "l"), ("V", "", "r"),
                       ("NP", "1", "l"), ("-NONE-", "", "l"), 
                       ("-NONE-", "", "r"), ("NP", "1", "r"),
                       ("PP", "", "l"), ("IN", "", "l"), ("IN", "", "r"),
                       ("NP", "2", "l"), ("NP", "2", "r"), ("PP", "", "r"),
                       ("VP", "", "r")]
        #7_a and 7_b represent the same pattern but with different 
        #restrictions 
        PAS_7_a_pattern = [("VP", "", "l"), ("V", "", "l"), 
                       ("V", "", "r"), ("NP", "1", "l"), 
                       ("-NONE-", "", "l"), ("-NONE-", "", "r"), 
                       ("NP", "1", "r"), ("VP", "", "r")]
        PAS_7_b_pattern = [("VP", "", "l"), ("V", "", "l"), 
                       ("V", "", "r"), ("NP", "1", "l"), 
                       ("-NONE-", "", "l"), ("-NONE-", "", "r"), 
                       ("NP", "1", "r"), ("VP", "", "r")]

        tree = tree_list[x]
        #These variables are used to enforce restrictions on the 
        #form
        isActive=notPAS=notPAS_2=notPAS_3=notPAS_4=notPAS_6 = 0
        notPAS_7_a = notPAS_7_b = 0
        notPAS_PP = notPAS_PP_4 = 0
        last_3_popped = ""
        last_5_popped = last_7_a_popped = last_7_b_popped = ""
        last_7_a_popped_pos = last_7_b_popped_pos = -1
        last_3_popped_pos = last_5_popped_pos = -1
        for y in xrange(1, len(tree)):
            if tree[y][0] == "V" and tree[y][4] == "h": 
                isActive = 1
            if PAS_PP_1_pattern:
                if len(PAS_PP_1_pattern) == 10:
                    #if NP with argument 0 then not passive
                    if tree[y][0] == "NP" and tree[y][1] == "0":
                        notPAS_PP = 1
                #Allows general argument number
                if len(PAS_PP_1_pattern)==11 or len(PAS_PP_1_pattern)==8:
                    node = (tree[y][0], "*", tree[y][3])
                else:
                    node = (tree[y][0], tree[y][1], tree[y][3])
                #VP is not popped from pattern if it is the modif
                if node[0] == "VP" and node[2] == "l":
                    if tree[y+1][4] == "f" and tree[y+1][0] == "VP":
                        continue
                    else:
                        PAS_PP_1_pattern.pop(0)
                elif node == PAS_PP_1_pattern[0]:
                    PAS_PP_1_pattern.pop(0)
            if PAS_PP_2_pattern:
                node = (tree[y][0] , tree[y][1], tree[y][3])
                if node == PAS_PP_2_pattern[0]:
                    PAS_PP_2_pattern.pop(0)
            if PAS_PP_3_pattern:
                node = (tree[y][0] , tree[y][1], tree[y][3])
                if node == PAS_PP_3_pattern[0]:
                    PAS_PP_3_pattern.pop(0)
            if PAS_PP_4_pattern:
                #If NP with argument 0 in node than not passive
                if tree[y][0] == "NP" and tree[y][1] == "0":
                    notPAS_PP_4 = 1
                node = (tree[y][0] , tree[y][1], tree[y][3])
                if node == PAS_PP_4_pattern[0]:
                    PAS_PP_4_pattern.pop(0)
            if PAS_PP_5_pattern:
                node = (tree[y][0] , tree[y][1], tree[y][3])
                if node == PAS_PP_5_pattern[0]:
                    PAS_PP_5_pattern.pop(0)
            if PAS_1_pattern:
                #If NP with argument 0 in node than not passive
                if tree[y][0] == "NP" and tree[y][1] == "0":
                    notPAS = 1
                node = (tree[y][0], tree[y][1], tree[y][3])
                #Found that S with argument 0 in tree than tree is not
                #passive
                if node[0] == "S" and node[1] == "0":
                    notPAS = 1
                if node == PAS_1_pattern[0]:
                    PAS_1_pattern.pop(0)
            if PAS_5_pattern:
                node = (tree[y][0], tree[y][1], tree[y][3])
                if node == PAS_5_pattern[0]:
                    #Ensures tree structure is correct
                    if last_5_popped == ("VP", "", "r"):
                        if y - last_5_popped_pos == 1:
                            last_5_popped = PAS_5_pattern.pop(0)
                            last_5_popped_pos = y
                    else:
                        last_5_popped = PAS_5_pattern.pop(0)
                        last_5_popped_pos = y
            if PAS_2_pattern:
                #If tree is a unlike coordinated phrase then 
                #not passive
                if tree[y][0] == "UCP":
                    notPAS_2 = 1
                    #Ensures actual root is UCP
                    if tree[y][4] == "f":
                        notPAS_2 = 0
                #If has NP with argument 0 then not passive
                if tree[y][0] == "NP" and tree[y][1] == "0":
                    notPAS_2 = 1
                node = (tree[y][0], tree[y][1], tree[y][3])
                if node == PAS_2_pattern[0]:
                    PAS_2_pattern.pop(0)
            if PAS_3_pattern:
                #If has NP with argument 0 then not passive
                if tree[y][0] == "NP" and tree[y][1] == "0":
                    notPAS_3 = 1
                node = (tree[y][0], tree[y][1], tree[y][3])
                if node == PAS_3_pattern[0]:
                    #Ensures structure
                    if last_3_popped == ("NP", "a", "r"):
                        if y - last_3_popped_pos == 1:
                            last_3_popped = PAS_3_pattern.pop(0)
                            last_3_popped_pos = y
                    else:
                        last_3_popped = PAS_3_pattern.pop(0)
                        last_3_popped_pos = y
            if PAS_4_pattern:
                #If has NP with argument 0 then not passive
                if tree[y][0] == "NP" and tree[y][1] == "0":
                    notPAS_4 = 1
                node = (tree[y][0], tree[y][1], tree[y][3])
                if node == PAS_4_pattern[0]:
                    PAS_4_pattern.pop(0)

            #Appears in treebank that if tree has a left NP modif structure
            #than it cannot be passive
            if tree[y][0]=="NP" and tree[y][2]!="2" and tree[y][4]=="f":
                notPAS_6 = 1
            if PAS_6_pattern:
                #If tree is a unlike coordinated phrase then 
                #not passive
                if tree[y][0] == "UCP":
                    notPAS_6 = 1
                    if tree[y][4] == "f":
                        notPAS_6 = 0
                node = (tree[y][0], tree[y][1], tree[y][3])
                if node == PAS_6_pattern[0]:
                    PAS_6_pattern.pop(0)
            
            #Appears in treebank that if tree has a left NP modif structure
            #than it cannot be passive
            if tree[y][0]=="NP" and tree[y][2]!="2" and tree[y][4]=="f":
                notPAS_7_a = notPAS_7_b = 1
            #If has NP with argument 0 then not passive
            if tree[y][0] == "NP" and tree[y][1] == "0":
                notPAS_7_a = notPAS_7_b = 1
            #If tree is a fragment than cannot be passive
            if tree[y][0] == "FRAG" and tree[y][2] == "1":
                notPAS_7_a = notPAS_7_b = 1
            if PAS_7_a_pattern:
                #If tree is a unlike coordinated phrase then 
                #not passive
                if tree[y][0] == "UCP":
                    notPAS_7_a = 1
                    if tree[y][4] == "f":
                        notPAS_7_a = 0
                node = (tree[y][0], tree[y][1], tree[y][3])
                if node == PAS_7_a_pattern[0]:
                    #Ensures correct structure
                    if last_7_a_popped == ("NP", "1", "r"):
                        if y - last_7_a_popped_pos == 1:
                            last_7_a_popped = PAS_7_a_pattern.pop(0)
                            last_7_a_popped_pos = y
                    else:
                        last_7_a_popped = PAS_7_a_pattern.pop(0)
                        last_7_a_popped_pos = y
            if PAS_7_b_pattern:
                #If tree is a unlike coordinated phrase then 
                #not passive
                if tree[y][0] == "UCP":
                    notPAS_7_b = 1
                    if tree[y][4] == "f":
                        notPAS_7_b = 0
                node = (tree[y][0], tree[y][1], tree[y][3])
                if node == PAS_7_b_pattern[0]:
                    #Ensures correct structure
                    if last_7_b_popped == ("V", "", "r"):
                        if y - last_7_b_popped_pos == 1:
                            last_7_b_popped = PAS_7_b_pattern.pop(0)
                            last_7_b_popped_pos = y
                    else:
                        last_7_b_popped = PAS_7_b_pattern.pop(0)
                        last_7_b_popped_pos = y

        if not PAS_PP_1_pattern:
            voices.append("pas_by")
        elif not PAS_PP_2_pattern:
            voices.append("pas_by")
        elif not PAS_PP_3_pattern:
            voices.append("pas_by")
        elif not PAS_PP_4_pattern and not notPAS_PP_4:
            voices.append("pas_by")
        elif not PAS_PP_5_pattern:
            voices.append("pas_by")
        elif not PAS_1_pattern and not notPAS:
            voices.append("pas")
        elif not PAS_2_pattern and not notPAS_2:
            voices.append("pas")
        elif not PAS_3_pattern and not notPAS_3:
            voices.append("pas")
        elif not PAS_4_pattern and not notPAS_4:
            voices.append("pas")
        elif not PAS_5_pattern and not notPAS:
            voices.append("pas")
        elif not PAS_6_pattern and not notPAS and not notPAS_6:
            voices.append("pas")
        elif not PAS_7_a_pattern and not notPAS_7_a:
            voices.append("pas")
        elif not PAS_7_b_pattern and not notPAS_7_b:
            voices.append("pas")
        elif isActive:
            voices.append("act")
        else:
            voices.append("NA")
    return voices            

#Function that returns if a tree has wh-movement. 
#Returns NA if the tree is non-Verbal else it has a few different options.
#It returns 0 if the wh-movement occurs in the subject position, 
#1 if it returns in the direct object position and 2 if it occurs in a
#indirect object position. If there is no wh-movement and the tree is
#verbal it returns NO.
def getWhs(tree_list):
    whs = []
    preds = getPreds(tree_list)
    for x in xrange(len(tree_list)):
        #Patterns for the various kinds of wh-movement
        #a * represents a mutli-option node
        #An empty pattern at the end means that the tree has that
        #pattern
        WH_0_pattern = [("S", "", "l"), ("NP", "*", "l"), 
                     ("NP", "*", "r"), ("S", "", "l"), 
                     ("NP", "", "l"), ("-NONE-", "", "l"), 
                     ("-NONE-", "", "r"), ("NP", "", "r"), 
                     ("S", "", "r"), ("S", "", "r")]
        WH_0_pattern_1 = [("S", "", "l"), ("NP", "*", "l"), 
                     ("NP", "*", "r"), ("S", "", "l"), 
                     ("NP", "", "l"), ("-NONE-", "", "l"), 
                     ("-NONE-", "", "r"), ("NP", "", "r"), 
                     ("S", "", "r"), ("S", "", "r")]
        WH_1_pattern = [("S", "", "l"), ("NP", "1", "l"), 
                     ("NP", "1", "r"), ("S", "", "l"), 
                     ("VP", "", "l"), ("NP", "", "l"), 
                     ("-NONE-", "", "l"), ("-NONE-", "", "r"),
                     ("NP", "", "r"), ("VP", "", "r"), 
                     ("S", "", "r")]
        WH_2_pattern = [("S", "", "l"), ("NP", "*", "l"), 
                     ("NP", "*", "r"), ("S", "", "l"), 
                     ("NP", "0", "l"), ("NP", "0", "r"), 
                     ("PP", "", "l"), ("NP", "", "l"), 
                     ("-NONE-", "", "l"), ("-NONE-", "", "r"),
                     ("NP", "", "r"), ("PP", "", "r"), 
                     ("S", "", "r")]
        tree = tree_list[x]
        isRel = 0
        #last_popped and last_popped_pos ensure tree structure
        #is correct
        last_popped = ""
        last_popped_pos = 0
        last_popped_1 = ""
        last_popped_pos_1 = 0
        last_popped_2 = ""
        last_popped_pos_2 = 0
        isVerbal = 0
        if preds[x] == "TRUE":
            isVerbal = 1
        for y in xrange(1, len(tree)):
            if tree[y][0] == "VP" or tree[y][0] == "V":
                isVerbal = 1
            #If it is a relative clause than it does not have wh
            if(y == 2 and tree[y][0] == "NP" and tree[y][4] == "f"):
                isRel = 1
                #Handles the case that it is nested under a NP adjunction
                #node but isn't a relative clause
                if tree[y+2][0] == "NP":
                    isRel = 0
            if WH_0_pattern:
                node_0 = tree[y][0]
                node_1 = tree[y][1]
                if len(WH_0_pattern) == 9 or len(WH_0_pattern) == 8:
                    #Allows for any NP node to be counted as long as it is
                    #an argument NP
                    if tree[y][1] != "":
                        node_1 = "*"
                    #Catches how
                    if tree[y][0] == "AdvP":
                        node_0 = "NP"
                node = (node_0, node_1, tree[y][3])
                if node == WH_0_pattern[0]:
                    #Making sure first NP is followed immediately by S
                    if last_popped == ("NP", "*", "r"):
                        if y - last_popped_pos == 1:
                            last_popped = WH_0_pattern.pop(0)
                            last_popped_pos = y 
                    #Making sure deeper S is followed immediately by 
                    #it's NP
                    elif(last_popped==("S", "", "l") 
                            and len(WH_0_pattern)==6):
                        if y - last_popped_pos == 1:
                            last_popped = WH_0_pattern.pop(0)
                            last_popped_pos == 1
                    else:
                        last_popped = WH_0_pattern.pop(0)
                        last_popped_pos = y
            #Same as WH_0_pattern above but gets case that NP trace is not
            #immediately after the deeper S but still a child of the 
            #deeper S
            if WH_0_pattern_1:
                node_1 = tree[y][1]
                if len(WH_0_pattern_1) == 9 or len(WH_0_pattern_1) == 8:
                    if tree[y][1] != "":
                        node_1 = "*"
                node = (tree[y][0] , node_1, tree[y][3])
                if node == WH_0_pattern_1[0]:
                    if last_popped_1 == ("NP", "*", "r"):
                        if y - last_popped_pos_1 == 1:
                            last_popped_1 = WH_0_pattern_1.pop(0)
                            last_popped_pos_1 = y 
                    #Ensures NP with trace is a child of the deeper S
                    elif last_popped_1 == ("NP", "", "r"):
                        if y - last_popped_pos_1 == 1:
                            last_popped_1 = WH_0_pattern_1.pop(0)
                            last_popped_pos_1 == 1
                    else:
                        last_popped_1 = WH_0_pattern_1.pop(0)
                        last_popped_pos_1 = y
            if WH_1_pattern:
                node_0 = tree[y][0]
                node_1 = tree[y][1]
                if len(WH_1_pattern) == 10 or len(WH_1_pattern) == 9:
                    #Catches wh word how
                    if tree[y][0] == "AdvP":
                        node_0 = "NP"
                    #a node marked with argument a also counts
                    if tree[y][1] == "a":
                        node_1 = "1"
                node = (node_0, node_1, tree[y][3])
                if node == WH_1_pattern[0]:
                    #ensures first NP is followed immediately by deeper S
                    if last_popped_2 == ("NP", "1", "r"):
                        if y - last_popped_pos_2 == 1:
                            last_popped_2 = WH_1_pattern.pop(0)
                            last_popped_pos_2 = y
                    else:
                        last_popped_2 = WH_1_pattern.pop(0)
                        last_popped_pos_2 = y
            if WH_2_pattern:
                node_1 = tree[y][1]
                if len(WH_2_pattern) == 12 or len(WH_2_pattern) == 11:
                    #First NP can have argument number 1 or 2
                    if tree[y][1] == "1" or tree[y][1] == "2":
                        node_1 = "*"
                node = (tree[y][0], node_1, tree[y][3])
                if node == WH_2_pattern[0]:
                    WH_2_pattern.pop(0)
            
        if not WH_0_pattern and not isRel:
            whs.append("0")
        elif not WH_0_pattern_1 and not isRel:
            whs.append("0")
        #WH_2 check occurs before WH_1 to ensure that it is not mistaken
        #as WH_1
        elif not WH_2_pattern and not isRel:
            whs.append("2")
        elif not WH_1_pattern and not isRel:
            whs.append("1")
        else:
            if isVerbal:
                whs.append("NO")
            else:
                whs.append("NA")

    return whs

#Function that checks if the tree has a relative clause structure. There
#are four different types of relative clause patterns. They all have a NP
#foot node with right direction. Then the first type has a trace under the
#subject, the second has a trace under the direct object, the third has a 
#trace under the indirect object and the fourth is a relative clause that
#does not fit this pattern. The return values are 0,1,2,+ respectively, and
#NA if the tree is non-verbal or else NO.
def getRels(tree_list):
    rels = []
    preds = getPreds(tree_list)
    for x in xrange(len(tree_list)):
        PP_pattern = [("NP", "l"), ("NP", "l"), ("NP", "r"), 
                ("S", "l"), ("NP", "l"), ("NP", "r"), 
                ("S", "l"), ("NP", "l"), ("NP", "r"), 
                ("VP", "l"), ("PP", "l"), ("NP", "l"), 
                ("-NONE-", "l"), ("-NONE-", "r"), ("NP", "r"), 
                ("PP", "r"), ("VP", "r"), ("S", "r"), 
                ("S", "r"), ("NP", "r")]
        VP_pattern = [("NP", "", "l"), ("NP", "", "l"), ("NP", "", "r"), 
                ("S", "", "l"), ("NP", "*", "l"), ("NP", "*", "r"), 
                ("S", "", "l"), ("VP", "", "l"), ("NP", "", "l"), 
                ("-NONE-", "", "l"), ("-NONE-", "", "r"), ("NP", "", "r"),
                ("VP", "", "r"), ("S", "", "r"), ("S", "", "r"), 
                ("NP", "", "r")]
        NP_pattern = [("NP", "", "l"), ("NP", "", "l"), ("NP", "", "r"), 
                ("S", "", "l"), ("*", "*", "l"), ("*", "*", "r"), 
                ("S", "", "l"), ("NP", "", "l"), ("-NONE-", "", "l"), 
                ("-NONE-", "", "r"), ("NP", "", "r"), 
                ("S", "", "r"), ("S", "", "r"), ("NP", "", "r")]
        tree = tree_list[x]
        last_position_NP = 1
        seenPP = 0
        hasS = 0
        #has reduced relative clause
        hasRRC = 0
        #has parenthetical
        hasPRN = 0
        #has Coordination clause of some kind
        hasC = 0
        hasVP = 0
        isVerbal = 0
        if preds[x] == "TRUE":
            isVerbal = 1
        hasStructure = 0
        for y in xrange(1, len(tree)):
            if tree[y][0] == "VP" or tree[y][0] == "V":
                isVerbal = 1
            if tree[y][0] == "VP" and tree[y][1] == "":
                hasVP = 1
            if(tree[y][0]=="NP" and tree[y][2]=="2" 
                    and tree[y][3]=="r" and tree[y][4]=="f"):
                hasStructure = 1
                if tree[y+1][0] == "NP":
                    hasStructure = 0
            if tree[y][0] == "S" and tree[y][1] == "":
                hasS = 1
            if tree[y][0] == "RRC":
                hasRRC = 1
            if tree[y][0] == "PRN":
                hasPRN = 1
            #has coordinating conjuction or unlike coordinated phrase
            if tree[y][0] == "UCP" or tree[y][0] == "CC":
                hasC = 1
            if VP_pattern:
                if tree[y][0] == "PP":
                    seenPP = 1
                #Allows for any argument number for the child of the first
                #S
                if len(VP_pattern) == 12 or len(VP_pattern) == 11:
                    node = (tree[y][0], "*", tree[y][3])
                else:
                    node = (tree[y][0], tree[y][1], tree[y][3])
                if node  == VP_pattern[0]:
                    #Ensures NP is not a child of the PP 
                    if len(VP_pattern) == 8:
                        if not seenPP:
                            VP_pattern.pop(0)
                    else:
                        VP_pattern.pop(0)
            if PP_pattern:
                if (tree[y][0], tree[y][3]) == PP_pattern[0]:
                    PP_pattern.pop(0)
            if NP_pattern:
                #Allows for generic child of first S
                if len(NP_pattern) == 10 or len(NP_pattern) == 9:
                    node = ("*", "*", tree[y][3])
                else:
                    node = (tree[y][0], tree[y][1], tree[y][3])
                if node  == NP_pattern[0]:
                    #Ensures NP is child of the S
                    if len(NP_pattern) == 7:
                        if (int(tree[y][2]) - last_position_NP) <= 2:
                            last_position_NP = int(tree[y][2])
                            NP_pattern.pop(0)
                    else:
                        last_position_NP = int(tree[y][2])
                        NP_pattern.pop(0)
        if not NP_pattern:
            rels.append("0")
        elif not PP_pattern:
            rels.append("2")
        elif not VP_pattern:
            rels.append("1")
        #if none of the above patterns fits but is a relative clause
        #then it is rel +
        #hasStructure ensures NP right foot node, not PRN ensures the tree
        #is not a parenthetical tree which has similar pattern to Reduced
        #relative clauses, not C ensures it is not a coordination clause
        #of some kind which is similar to relative clause pattern and then
        # the final and for hasS or hasVp or hasRRC ensures it is a 
        #relative clause
        elif(hasStructure and not hasPRN and not hasC 
                and (hasS or hasVP or hasRRC)):
            rels.append("+")
        elif not isVerbal:
            rels.append("NA")
        else:
            rels.append("NO")
    return rels

#Function that returns a list of all substitution nodes of a tree
#or nil if there are none. From the grammmar it appears that any
#tree with an argument number "a" was counted as a substnode in the old
#this reflects the same process.
def getSubstnodes(tree_list):
    substnodes = []
    for x in xrange(len(tree_list)):
        tree = tree_list[x]
        tmp_list = []
        for y in xrange(1, len(tree)):
            if tree[y][1] == "a" and tree[y][3] == "l":
                tmp_list.append(tree[y][0])
        if not tmp_list:
            substnodes.append(["nil"])
        else:
            substnodes.append(tmp_list)
    return substnodes

#WORK IN PROGRESS
def getAppos(tree_list):
    appos = []
    for x in xrange(len(tree_list)):
        tree = tree_list[x]
        isNPModif = 0 
        hasV = 0
        hasArg = 0
        for y in xrange(1, len(tree)):
            if((tree[y][0]=="NP" or tree[y][0]=="NPP")
                and tree[y][2]=="2" and tree[y][4]=="f"):
                isNPModif = 1
            if tree[y][0] == "V":
                hasV = 1
            if tree[y][1] != "":
                hasArg = 1
        if isNPModif and not hasV and not hasArg:
            appos.append("+")
        else:
            appos.append("-")
    print "STILL WORKING ON THIS"
    return appos

#Main function
if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: python feature_extractor.py " +
                "<grammar_file> <name_of_output_file>\n")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    grammar = open(input_file, "r")
    output = open(output_file, "w")
    dimension_labels, dimension_values = getDimensions(grammar)

    number_of_trees = len(dimension_values[0])

    for y in xrange(number_of_trees):
        for x in xrange(len(dimension_labels)):
            if dimension_labels[x] == "tree":
                output.write(dimension_values[x][y][0][0] + " ")
            else:
                if(dimension_labels[x] == "lfronts" 
                        or dimension_labels[x]=="rfronts"):
                    tmp = ""
                    for node in dimension_values[x][y]:
                        if node[0] != "nil":
                            if not node[1].isdigit():
                                argument = "X"
                            else:
                                argument = node[1]
                            tmp += (node[0] + "#" + node[4] + 
                                    "#" + argument + "_")
                        else:
                            tmp += node[0] + "_"
                    output.write(dimension_labels[x] + ":" 
                            + tmp[:len(tmp)-1] + " ")
                elif(dimension_labels[x] == "ladjnodes" 
                        or dimension_labels[x]=="radjnodes"):
                    tmp = ""
                    for node in dimension_values[x][y]:
                        tmp += node[0] + "_"
                    output.write(dimension_labels[x] + ":" 
                            + tmp[:len(tmp)-1] + " ")
                elif(dimension_labels[x] == "dsubcat" 
                        or dimension_labels[x]=="dsubcat2"):
                    tmp = ""
                    for node in dimension_values[x][y]:
                        if node == "nil":
                            tmp += node + "_"
                        else:
                            if node[len(node)-1] == "(P)":
                                tmp +=(node[0] + "#" + node[1] 
                                        + node[2] + "_")
                            else:
                                tmp += node[0] + "#" + node[1] + "_"
                    output.write(dimension_labels[x] + ":" 
                            + tmp[:len(tmp)-1] + " ")
                elif(dimension_labels[x] == "substnodes"):
                    tmp = ""
                    for node in dimension_values[x][y]:
                        tmp += node + "_"
                    output.write(dimension_labels[x] + ":" +
                            tmp[:len(tmp)-1] + " ")
                elif x == len(dimension_labels)-1:
                    output.write(dimension_labels[x] + 
                            ":" + dimension_values[x][y] + "\n")
                else:
                    output.write(dimension_labels[x] + ":" + 
                            dimension_values[x][y] + " ")
    grammar.close()
    output.close()

