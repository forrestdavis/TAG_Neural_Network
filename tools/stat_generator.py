#Simple function that generates some stats about the new trees
results = open("../data/treeproperties_new.str", "r")

total_trees = 0.0 
dir_right = 0.0
dir_left = 0.0
dir_NA = 0.0
lfronts_nil = 0.0
rfronts_nil = 0.0
fronts_nil = 0.0
fronts = 0.0
substnodes_nil = 0.0
substnodes = 0.0
false_predaux = 0.0
true_predaux = 0.0
false_coanc = 0.0
true_coanc = 0.0
false_particle = 0.0
true_particle = 0.0
particleShift = 0.0
lcomp_NA = 0.0
rcomp_NA = 0.0
comp_NA = 0.0
comp = 0.0
false_pred = 0.0
true_pred = 0.0
dsubcat_nil = 0.0
datshift_yes = 0.0
datshift_no = 0.0
datshift_na = 0.0
esubj_yes = 0.0
esubj_no = 0.0
esubj_na = 0.0
rel_0 = 0.0
rel_1 = 0.0
rel_2 = 0.0
rel_plus = 0.0
rel_no = 0.0
rel_na = 0.0
wh_0 = 0.0
wh_1 = 0.0
wh_2 = 0.0
wh_no = 0.0
wh_na = 0.0
pas = 0.0
act = 0.0
pas_by = 0.0
voice_na = 0.0
for line in results:
    total_trees += 1
    if " dir:RIGHT " in line:
        dir_right += 1
    if " dir:LEFT " in line:
        dir_left += 1
    if " dir:NA " in line:
        dir_NA += 1
    if " lfronts:nil " in line:
        lfronts_nil += 1
    if " rfronts:nil " in line:
        rfronts_nil += 1
    if " lfronts:nil " in line and " rfronts:nil " in line:
        fronts_nil += 1
    if " lfronts:nil " not in line and " rfronts:nil " not in line:
        fronts += 1
    if " substnodes:nil " in line:
        substnodes_nil += 1
    if " substnodes:nil " not in line:
        substnodes += 1
    if " predaux:FALSE " in line:
        false_predaux += 1
    if " predaux:TRUE " in line:
        true_predaux += 1
    if " coanc:FALSE " in line:
        false_coanc += 1
    if " coanc:FALSE" not in line:
        true_coanc += 1
    if " particle:FALSE " in line:
        false_particle += 1
    if " particle:TRUE " in line:
        true_particle += 1
    if " particleShift:YES " in line:
        particleShift += 1
    if " lcomp:NA " in line:
        lcomp_NA += 1
    if " rcomp:NA " in line:
        rcomp_NA += 1
    if " lcomp:NA " in line and " rcomp:NA " in line:
        comp_NA += 1
    if " lcomp:NA " not in line and " rcomp:NA " not in line:
        comp += 1
    if " pred:FALSE " in line:
        false_pred += 1
    if " pred:TRUE " in line:
        true_pred += 1
    if " dsubcat:nil" in line:
        dsubcat_nil += 1
    if " datshift:YES" in line:
        datshift_yes += 1
    if " datshift:NO" in line:
        datshift_no += 1
    if " datshift:NA" in line:
        datshift_na += 1
    if " esubj:YES" in line:
        esubj_yes += 1
    if " esubj:NO" in line:
        esubj_no += 1
    if " esubj:NA" in line:
        esubj_na += 1
    if " rel:0" in line:
        rel_0 += 1
    if " rel:1" in line:
        rel_1 += 1
    if " rel:2" in line:
        rel_2 += 1
    if " rel:+" in line:
        rel_plus += 1
    if " rel:NO" in line:
        rel_no += 1
    if " rel:NA" in line:
        rel_na += 1
    if " wh:0" in line:
        wh_0 += 1
    if " wh:1" in line:
        wh_1 += 1
    if " wh:2" in line:
        wh_2 += 1
    if " wh:NO" in line:
        wh_no += 1
    if " wh:NA" in line:
        wh_na += 1
    if " voice:pas" in line and " voice:pas_by" not in line:
        pas += 1
    if " voice:act" in line:
        act += 1
    if " voice:pas_by" in line:
        pas_by += 1
    if " voice:NA" in line:
        voice_na += 1
    
print "Total trees: ", total_trees
print "Total trees with dir right: ", dir_right, " percentage: ",(dir_right/total_trees)
print "Total trees with dir left: ", dir_left, " percentage: ",(dir_left/total_trees)
print "Total trees with dir na: ", dir_NA, " percentage: ",(dir_NA/total_trees)
print "Total trees with no lfronts: ", lfronts_nil, " percentage: ",(lfronts_nil/total_trees)
print "Total trees with lfronts: ", (total_trees - lfronts_nil), " percentage: ",((total_trees-lfronts_nil)/total_trees)
print "Total trees with no rfronts: ", rfronts_nil, " percentage: ",(rfronts_nil/total_trees)
print "Total trees with rfronts: ", (total_trees - rfronts_nil), " percentage: ",((total_trees-rfronts_nil)/total_trees)
print "Total trees with no fronts: ", fronts_nil, " percentage: ",(fronts_nil/total_trees)
print "Total trees with both rfronts and lfronts: ", fronts, " percentage: ",(fronts/total_trees)
print "Total trees with no substnodes: ", substnodes_nil, " percentage: ",(substnodes_nil/total_trees)
print "Total trees with substnodes: ", substnodes, " percentage: ",(substnodes/total_trees)
print "Total trees with predaux false: ", false_predaux, " percentage: ",(false_predaux/total_trees)
print "Total trees with predaux true: ", true_predaux, " percentage: ",(true_predaux/total_trees)
print "Total trees with no coanc: ", false_coanc, " percentage: ",(false_coanc/total_trees)
print "Total trees with a coanc: ", true_coanc, " percentage: ",(true_coanc/total_trees)
print "Total trees with no particle: ", false_particle, " percentage: ",(false_particle/total_trees)
print "Total trees with a particle: ", true_particle, " percentage: ",(true_particle/total_trees)
print "Total trees with a particle that is shifted: ", particleShift, " percentage: ",(particleShift/total_trees)
print "Total trees with a particle that is shifted: ", particleShift, " percentage of total particles: ",(particleShift/true_particle)
print "Total trees with no lcomp: ", lcomp_NA, " percentage: ",(lcomp_NA/total_trees)
print "Total trees with lcomp: ", (total_trees - lcomp_NA), " percentage: ",((total_trees - lcomp_NA)/total_trees)
print "Total trees with no rcomp: ", rcomp_NA, " percentage: ",(rcomp_NA/total_trees)
print "Total trees with rcomp: ", (total_trees - rcomp_NA), " percentage: ",((total_trees - rcomp_NA)/total_trees)
print "Total trees with no lcomp and no rcomp: ", comp_NA, " percentage: ",(comp_NA/total_trees)
print "Total trees with both lcomp and rcomp: ", comp, " percentage: ",(comp/total_trees)
print "Total trees with pred false: ", false_pred, " percentage: ",(false_pred/total_trees)
print "Total trees with pred true: ", true_pred, " percentage: ",(true_pred/total_trees)
print "Total trees with no dsubcat: ", dsubcat_nil, " percentage: ",(dsubcat_nil/total_trees)
print "Total trees with dsubcat: ", (total_trees - dsubcat_nil), " percentage: ",((total_trees-dsubcat_nil)/total_trees)
print "Total trees with yes datshift: ", (datshift_yes), " percentage: ",((datshift_yes)/total_trees)
print "Total trees with no datshift: ", (datshift_no), " percentage: ",((datshift_no)/total_trees)
print "Total trees with na datshift: ", (datshift_na), " percentage: ",((datshift_na)/total_trees)
print "Total trees with yes esubj: ", (esubj_yes), " percentage: ",((esubj_yes)/total_trees)
print "Total trees with no esubj: ", (esubj_no), " percentage: ",((esubj_no)/total_trees)
print "Total trees with na esubj: ", (esubj_na), " percentage: ",((esubj_na)/total_trees)
print "Total trees with rel 0: ", (rel_0), " percentage: ",((rel_0)/total_trees)
print "Total trees with rel 1: ", (rel_1), " percentage: ",((rel_1)/total_trees)
print "Total trees with rel 2: ", (rel_2), " percentage: ",((rel_2)/total_trees)
print "Total trees with rel +: ", (rel_plus), " percentage: ",((rel_plus)/total_trees)
print "Total trees with no rel: ", (rel_no), " percentage: ",((rel_no)/total_trees)
print "Total trees with na rel: ", (rel_na), " percentage: ",((rel_na)/total_trees)
print "Total trees with wh 0: ", (wh_0), " percentage: ",((wh_0)/total_trees)
print "Total trees with wh 1: ", (wh_1), " percentage: ",((wh_1)/total_trees)
print "Total trees with wh 2: ", (wh_2), " percentage: ",((wh_2)/total_trees)
print "Total trees with no wh: ", (wh_no), " percentage: ",((wh_no)/total_trees)
print "Total trees with na wh: ", (wh_na), " percentage: ",((wh_na)/total_trees)
print "Total trees with voice pas: ", (pas), " percentage: ",((pas)/total_trees)
print "Total trees with voice act: ", (act), " percentage: ",((act)/total_trees)
print "Total trees with voice pas_by: ", (pas_by), " percentage: ",((pas_by)/total_trees)
print "Total trees with voice pas_by: ", (pas_by), " percentage of all passive: ",((pas_by)/(pas+pas_by))
print "Total trees with voice na: ", (voice_na), " percentage: ",((voice_na)/total_trees)
