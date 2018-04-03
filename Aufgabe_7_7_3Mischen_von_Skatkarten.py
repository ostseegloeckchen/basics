#Erstelle ein Programm mit dem 32 Skatkarten gemischt werden können.

farben=["Kreuz","Pik","Herz","Karo"]
werte=["7","8","9","10","Bube","Dame","König","Ass"]
spiel=[(i,j) for i in farben for j in werte]            #erzeugt eine Liste von Karten

print(spiel)

import random

anzahl=random.randint(20,40)        #20 bis 40 mal werden jetzt Karten vertauscht

for i in range(anzahl):
    karte1=random.randint(0,31)     #Erzeugung von Zufallszahlen zw. 0 und 31
    karte2=random.randint(0,31)     #Erzeugung von Zufallszahlen zw. 0 und 31
    
    spiel[karte1],spiel[karte2]=spiel[karte2],spiel[karte1] #Vertauschen von Karten mit dem jeweiligen Index

print()
print("Gemischte Karten")
print("----------------")
print(spiel)
