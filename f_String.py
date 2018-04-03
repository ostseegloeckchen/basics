# f-Strings mit Platzhaltern

name = "Anna"

print(f"Ihr Name ist {name}.")

print()

laenge = 12.5
breite = 20

print(f"Die Fläche beträgt {laenge * breite} Quadratmeter.")

print()

from math import pi

print(f"Die Kreiszahl hat den Wert {pi:.2f}.")

print()

print(f"Die Kreiszahl hat den wert {pi:.5f}.")

print()

print(f"Die Kreiszahl hat den wert {pi:12.5f}.")

print()

# alles was in den Platzhaltern von f-Strings eingesetzt werden soll
# muss vorher bekannt sein, da die Platzhalter von f-Strings sofort bearbeitet werden
# daher funktioniert folgende Anweisung nicht

print(f"Der unbekannte Wert ist {x}")


