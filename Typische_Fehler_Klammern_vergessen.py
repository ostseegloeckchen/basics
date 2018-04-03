#versehentliches Verwechseln von Methoden und Attributen

class Rechteck(object):
    def __init__(self, laenge, breite):
        self.laenge=laenge
        self.breite=breite

    def flaeche(self):
        return self.laenge*self.breite


#Hauptprogramm
a=Rechteck(2,1)
b=Rechteck(1,2)

print(a.flaeche)
print(b.flaeche)

print()

print(a.flaeche())
print(b.flaeche())

print(a.flaeche==b.flaeche)    #Hier wurden die leeren Klammern von "flaeche" vergessen --> flaeche(), daher ist es ein Verglich zwischen den String-Repräsentationen der Methoden-Objekte

#richtig:
print(a.flaeche()==b.flaeche())    # Vergleich der Methoden zur Flächenberechnung, vergleicht die Werte der Flächen
