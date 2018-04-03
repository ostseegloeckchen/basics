#Erstellen einer Generator-Funktion

def generiere_zahlen(n):
    for i in range(n):
        yield i*i

g=generiere_zahlen(10)
print(g)

for i in g:
    print(i, end=" ")
    

print()
# Andere Form der Zahlengenerierung
def generiere_zahlen_1(n):
    i=1
    while i<=n:
        yield i*i
        i +=1

g1=generiere_zahlen_1(3)
g1

# Generierung von unendlich vielen Kollektoren (virtuell)
def generiere_zahlen_2():
    i=1
    while True:         # Endlos-Schleife
        yield i*i
        i +=1

g2=generiere_zahlen_2()
