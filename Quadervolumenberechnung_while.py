#Berechnung des Volumens eines Quaders solange der Anwender es möchte

print("Möchten Sie das Volumen eines Quaders berechnen")
input("Eingabe: ja = j / nein = n: ")
antwort='j'

while antwort=='j':
    l=input("Länge in cm: ")
    b=input("Breite in cm: ")
    h=input("Höhe in cm: ")
    volumen=float(l)*float(b)*float(h)
    print("Das Volumen beträgt",volumen,"ccm.")
    antwort=input("Noch einmal (j,n)?: ")
print("Vielen Dank fü die Verwendung dieses Programmes.")
