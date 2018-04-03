# Definition einer Klasse "Laenge"
# Repräsentation von Strecken
#private Klassenattribut:
#   "__meter" (Dictionary) Längeneinheit : Zahlenwert

#öffentliche Attribut:
#       "betrag" (Zahlenwert) und "einheit" (Längeneinheit als String)

# Methoden:
#   getMeter() liefert Länge eines Objektes in Meter
#    __add__() liefert die Addition zweier Objekte mit Rücksicht auf die Eiheiten
#   __str__() lesbare Darstellung des Objektes als Zeichenkette

class Laenge(object):
    __meter={"mm":0.001,
             "cm":0.01,
             "m":1.0,
             "km":1000,
             "in":0.0254,
             "ft":0.3048,
             "yd":0.9143,
             "mil":1609}

    def __init__(self, betrag, einheit):
        self.betrag=float(betrag)
        self.einheit=einheit

    def getMeter(self):
        return self.betrag*self.__meter[self.einheit]

    def __add__(self, other):
        s=self.getMeter() + other.getMeter()
        
        return Laenge(s/self.__meter[self.einheit], self.einheit)

    def __str__(self):
        return str(self.betrag) + " " + self.einheit


#Hauptprogramm
print(Laenge(12,"cm")+Laenge(2, "in"))

erddurchmesser=Laenge(12713.507, "km")
print(erddurchmesser)

print(Laenge(0, "mil") + erddurchmesser)    #Ausgabe in Milen

