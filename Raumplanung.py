#Finde für einen beliebigen Raum alle Nachbarräume
#Vereinige zwei Raumpläne (die sich möglicherweise überschneiden) zu einem größerem Gesamtplan

def finde_nachbarraeume(plan, raum):
    """Menge aller Nachbarräume"""
    raeume, tueren=plan
    t_raum=set(t for t in tueren if raum in t)      #1 Menge der Türen jedes Raumes
    nachbarraeume=set()                             #2 Hier wird eine leere Menge erzeugt (siehe unten)
    for t in t_raum:
        nachbarraeume=nachbarraeume|t               #3 siehe unten, "|" liefert die Vereinigung der Mengen nachbarraeume und t
    return nachbarraeume-set([raum])                #4 siehe unten

def vereinige(plan1,plan2):
    """füge zwei Pläne zusammen"""
    return(plan1[0]|plan2[0],plan1[1]|plan2[1])     #5 Vereinigung zweier Graphen

V1={1,2,3,4,5}                                      #6
E1=set(frozenset(t)
       for t in [(1,2),(2,3),(3,4),(4,5)])

raumplan1=(V1,E1)                                   #7

V2={4,5,6,7}
E2=set(frozenset(t)
       for t in [(5,4),(5,6),(5,7),(6,7)])

raumplan2=(V2,E2)

gesamtplan=vereinige(raumplan1,raumplan2)
nachbarraeume=finde_nachbarraeume(gesamtplan,2)

print("Räume des Gesamtplans: ")

for r in gesamtplan[0]:
    print(r, end=" ")

print()

print("Türen des Gesamtplans: ")

for t in gesamtplan[1]:
    print(tuple(t),end=" ")

print()

print("Nachbarräume von Raum 2: ")
for r in nachbarraeume:
    print(r, end=" ")

#1 Die Menge "t_raum" enthält alle Türen des Raumes "raum".
#1 = Menge der Kanten die zum Knoten gehören
#3 In der for-Schleife werden sukzessive alle Kanen aus der Menge t_raum
#3 (die ja Mengen mit jeweis zwei Knoten sind) vereinigt.
#3 Am Ende enthält die Menge nachbarraeume alle Räume, die über Türen mit dem Raum "raum"
#3 verbunden sind sowie den Raum "raum" selbst.
#4 Der Raum "raum" selbst wird hier wieder abgezogen.
#5 Vereinigung zweier Knotenmengen und der beiden Kantenmengen
#6 Die Kantenmenge ist ein Mengen-Objekt vom Typ "set",
#6 das lauter (unveränderliche) Mengen-Objekte vom Typ "frozenset" enthält.
#6 Die Kantenmenge wird mit einem Generatorenausdruck aus Liste von Tupeln erzeugt.
#7 Der Raumplan (ein Graph) wird durch ein Tupel mit zwei Mengen V1 und E1 repräsentiert.
