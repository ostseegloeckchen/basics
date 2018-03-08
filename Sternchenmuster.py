#Erzeugung verschiedener Sternchenmuster

for i in range(3):
    print("*","*","*","*")

print()

for i in range(5):
    print((4-i)*"  ",(i+1)*"* ",(i+1)*"* ")

print()
for i in range(5):
    print((i)*"  ",(5-i)*"* ",(5-i)*"* ")

print()

for i in range(4): #i fängt bei 0 an
    print((3-i)*"  ",(2*i+1)*"* ")
    #0. Zeile 3 Mal ein leeres Feld und 1 Mal ein Stern
    #1. Zeile 2 Mal ein leeres Feld und 3 Mal ein Stern
    #usw.
    #im ersten Term zwei Leerzeichen in den leeren Anführungszeichen
    #im zweiten Term ein Leerzeichen nach dem *, dann stimmen die Abstände

print()
for i in range(4):
    print((0+i)*"  ",(7-i*2)*"* ")
