# Berechne für alle natürlichen Zahlen von 0 bis 9 das Quadrat und
# bilde daraus eine (virtuelle) Folge.
# Die einzelnen Elemente müssen mit einer for-Schleife abgerufen werden.

g=(i*i for i in range(10))

print(g)

for n in g:
    print(n,end=" ")
