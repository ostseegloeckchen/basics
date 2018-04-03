#ausrichten von Spalten bei der Ausgabe auf dem Bildschirmm

from math import *
for x in range(6,12):
    print(x, format(sqrt(x),"8.3f"),sep="\t")   #1
      
#1 Gleitkommazahlen mit 3 Nachkommastellen
#1 mit der Funktion "format"
#1 "8": Für die Darstellung der Zahl werden acht Stellen reserviert
#1 ".3": Es gibt drei Nachkommastellen
#1 "f": Datentyp "float"
