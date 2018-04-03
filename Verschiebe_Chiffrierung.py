#Anwendung des Caesar Algorithmus (Verschiebechiffre)
#Anwendung mit Pythonwin

import sys

klartext=sys.argv[1]            #Lesen der Argumente aus der Liste "sys.argv"
n=int(sys.argv[2])              #Umwandeln des Str in sys.argv [2] in eine ganze Zahl
print(klartext)
chiffriert=""
klartext=klartext.upper()       #Umwandlung in Grossbuchstaben
for c in klartext:
    nr=ord(c)+n                 #3
    if nr > ord("Z"):           #4
        nr -=25
    if c != " ":
        chiffriert += chr(nr)
    else:
        chiffriert += " "       #5

print(chiffriert)

#argv = Argumentevektor des Moduls sys
