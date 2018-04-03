#Zeichenketten auffüllen

# die Zeichenkette "rechts" wird links mit so vielen Gleichheitszeichen aufgefüllt,
# dass das Wort "rechts" am Ende einer Zeichenkette mit 20 Zeichen steht

print("rechts".rjust(20, "="))

print()

# die Zeichenkette "links" wird rechts mit so vielen Bindestrichen aufgefüllt,
# dass das Wort "links" am Anfang einer Zeichenkette mit 20 Zeichen steht

print("links".ljust(20, "-"))

print()

# die Zeichenkette "mittig" wird rechts und links mit so vielen §-Zeichen aufgefüllt,
# dass das Wort "mittig" in der Mitte einer Zeichenkette mit 20 Zeichen steht

print(" mittig ".center(40,"§"))

print()

# Ausgabe eines Strings der mit einem Großbuchstaben beginnt und dem lauter kleine Buchstaben folgen
print("eine Insel".capitalize())

print()

# Ausgabe eines Strings mit kleinen Buchstaben
print("Eine Insel".lower())

print()

# Ausgabe eines Stringsmit großen Buchstaben
print("eine Insel".upper())




