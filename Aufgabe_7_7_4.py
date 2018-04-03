# Ermitteln der Menge von rechtwinkeligen Dreiecken
# mit ganzzahligen Seitenlänen kleiner als 20


dreiecke=set(frozenset((a,b,c))
    for a in range(1,19)
    for b in range(1,19)
    for c in range(1,19)
    if a*a+b*b==c*c)
for d in dreiecke:
    print(tuple(d), end=" ")
    
#c=[round((i*i+j*j)**0.5,2) for i in a for j in b]

#print(c)

#laengen=tuple((i,j,k) for i in a for j in b for k in c)
#print(laengen)
#hile c[k]<20 and c[k]==int
