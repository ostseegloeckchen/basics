# Definiere eine Klasse "Quader" als Spezilisierung der Klasse "Ding"
# Die Klasse "Quader" soll Quader aus verschiedenen Metallen modellieren
# Überladen der Vergleichoperatoren "==", ">", ">="
# Verleich der Massen

from Aufgabe_10_11_1_Ding import Ding

class Quader(Ding):
    
    """Spezialisierung der Klasse Ding zur Berechnung von Quadern
            Öffentliche Attribute:

            private Attribute:
                    geerbte: _symbol, _dichte, __volumen
                    Erweiterungen: __laenge, __breite, __hoehe (in cm

            Öffentliche Methoden und Überladungen:
                    geerbte: getVolumen(), getMasse()
                    überschrieben: __str__()"""

                    

    def __init__(self, symbol, laenge, breite, hoehe):
        Ding.__init__(self, symbol, laenge * breite * hoehe)    # Als Wert für das Attribut "__volumen" wird das Produkt aus Länge, Breite und Höhe übergeben
        self.__laenge = float(laenge)                           # nicht vergessen die Werte der Attribute zu definieren (float, int, str)
        self.__breite = float(breite)
        self.__hoehe = float(hoehe)

    def getName(self):
        for key, value in Ding._dichte.items() :
            if key==self._symbol:
                return (value[0])

    def getLaenge(self):
        return self.__laenge

    def getBreite(self):
        return self.__breite

    def getHoehe(self):
        return self.__hoehe

    def __eq__(self):
        return self.getMasse()==other.getMasse()

    def __gt__(self, other):
        return self.getMasse() > other.getMasse()

    def __ge__(self, other):
        return self.getMasse()>= other.getMasse()
        

    def __str__(self):                                              # Wie kann hier formuliert werden, wie sich die Massen verschiedener Quader zueinander verhalten?
        beschreibung = "Der Quader aus " +\
                       self._dichte[self._symbol][0] +\
                       ", mit der Länge, Breite und Höhe von " +\
                       format(self.__laenge,".2f") + " cm, " +\
                       format(self.__breite,".2f") + " cm bzw." +\
                       format(self.__hoehe,".2f") + " cm," +\
                       " hat eine Masse von " +\
                       format(self.getMasse(), ".2f") + " g."
                       
        return beschreibung
    

#Hauptprogramm
print()

quader1=Quader("Au", 2, 3, 4)
print(quader1.getSymbol() + ":")
print("Dichte: ", quader1.getDichte())
print("Volumen: ", quader1.getVolumen())
print("Masse: ", quader1.getMasse())

print(quader1)

quader2=Quader("Ag", 2, 3, 4)
print(quader2.getSymbol() + ":")
print("Dichte: ", quader2.getDichte())
print("Volumen: ", quader2.getVolumen())
print("Masse: ", quader2.getMasse())

print(quader2)

print()

print("Vergleich der beiden Quader:")

if quader1.getMasse() == quader2.getMasse():
    print("Die beiden Quader haber die gleiche Masse.")
elif quader1.getMasse() > quader2.getMasse():
    print("Der 1. Quader ist schwerer als der 2. Quader.")
else:
    print("Der 1Quader ist leichter als der 2Quader.")

print()

if quader1.getMasse() == quader2.getMasse():
    print("Die beiden Quader haber die gleiche Masse.")
elif quader1.getMasse() > quader2.getMasse():
    print("Der Quader aus " +\
          quader1.getName() +\
          " ist schwerer als der Quader aus " +\
          quader2.getName() + ".")
else:
    print("Der Quader aus " +\
          quader1.getName() +\
          " ist leichter als der Quader aus " +\
          quader2.getName() + ".")

