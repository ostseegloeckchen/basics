#

def menge(s):               #die "menge"-Funktion löscht alle Dublikate in der Sequenz "s"
    d={}                    #
    for i in s:
        d[i]=None           #Wurden die Elemente der Menge nun als Schlüsselwörter übernommen oder als Werte?
    return list(d.keys())   
    return list(d.values())

##for key in d.keys():
##    print(key+ ": ",end=" ")
##    for w in d[key]:
##        print(w, end=" ")
##    print()
##
##for key in d():
##    print(key,": ",d[key])
##
##print()

#print(list(d.keys()))

#Hauptprogramm
s=[1,2,5,67,7,2,1,1,36,2]

print(menge(s))



