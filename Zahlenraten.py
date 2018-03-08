#Erraten einer unbekannten Zufallszahl zwischen 0 und 100

import random           #Import des Moduls random
zufallszahl=random.randint(0,100) #Erzeuge Zufallszahl

print("Raten Sie eine Zahl zwischen 0 und 100!")

zahl=-1
while zahl!=zufallszahl:
    zahl=int(input("Zahl: "))
    if zahl==zufallszahl:
        print("Zahl gefunden")
    elif zahl<zufallszahl:
        print("Zahl zu klein")
    elif zahl>zufallszahl:
        print("Zahl zu groß")

print("Herzlichen Glückwunsch, Sie haben die Zahl gefunden!")
