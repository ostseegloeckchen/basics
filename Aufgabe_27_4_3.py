# drehe die Objekte in einer Schlange um
# ohne return-Anweisung
# Verwende als Hilfsobjekt einen Stack


# Wie kann ich das Ergebnis des Umdrehens sichtbar machen???, das funktioniert unten nicht!!!
from module_Stack import *
from module_Queue import *

def umdrehenSchlange(schlange):
    while not schlange.empty():
        hilf = Stack()
        hilf.push(schlange.dequeue()) #

    while not hilf.empty():
        #umgedrehteSchlange = Queue()
        schlange.enqueue(hilf.pop)



# Hauptprogramm

schlangeninhalt = input("Inhalt der Originalschlange: ")
test = Queue()
for zeichen in schlangeninhalt:
    test.enqueue(zeichen)

ergebnis = umdrehenSchlange(test)

print()

print("Output: ", ergebnis.front)

        
