# Ermitteln der Elementeanzahl in einem Stapel
# a) rekursiv

print("Wieviele Elemente befinden sich in dem Stapel / Stack?")

def laengeStapel(stapel):
    if stapel.empty():          # Abbruch der rekursiven Schleife, wenn Stapel leer ist
        return 0
    else:
        hilf = stapel.pop()
        laenge = 1 + laengeStapel(stapel)   # rekursiver Aufruf der Funktion mit kleinerem Stapel (oberstes Element wurde entfernt)
        stapel.push(hilf)                   # Originalzustand wird wieder hergestellt
        return laenge



# b) nicht rekursiv
def laenge(stapel):
    i = 0                           # Zähler wird initialisiert
    hilf1 = Stack()
    while not stapel.empty():
        i += 1                      #1 solange Stapel nicht leer, wird Zähler um 1 erhöht 
        hilf1.push(stapel.pop())

    while not hilf1.empty():        #2 Herstellung des Orginalzustandes
        stapel.push(hilf1.pop())

    return i

#1 Das mit "pop()" entfernte Element wird auf dem Hilfstapel zwischengelagert

#2 Die geretteten Elemente werden vom Hilfsstapel zurück transportiert



# Hauptprogramm

from module_Stack import *

inhalt = input("Stapelinhalt: ")

test = Stack()
for zeichen in inhalt:
    test.push(zeichen)

print()
print("Anzahl der Elemente: ", laengeStapel(test))
print("Anzahl der Elemente: ", laenge(test))
    
