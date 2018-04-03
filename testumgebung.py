# Testen des Moduls "Geld"

import sys
sys.path.append("module")   # ohne diesen Aufruf funktioniert das Skript nicht
from Modul_Klassendefinition_Geld import Geld

print("Test der Klasse Geld")

print()

anweisung=input("Anweisung: ")
while anweisung != "":
    try:
        exec(anweisung) #1 Aufruf der Funktion "exc()" 
    except:
        print("Fehler: " + str(sys.exc_info()[0]))  

    anweisung=input("Anweisung: ")

print("Ende des Tests")

#1 mit der Funktion "exc()" wird das Programm dazu aufgefordert eine Funktion bzw. ein Python-Programm auszuführen
