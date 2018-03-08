#Ermittle alle denkbaren Sequenzen mit den vier Basenpaaren AT, TA, CG, GC

paare="AT","TA","CG","GC"
for a in paare:
    for b in paare:
        for c in paare:
            for d in paare:
                print(a+b+c+d,end=" ")
