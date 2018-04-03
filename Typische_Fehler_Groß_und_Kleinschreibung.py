#Typische Fehler beim Erzeugen von neuen Klassen

#versehentliches Verwechseln von Groß- und Kleinschreibung

class Behaelter(object):
    def __init__(self, volumen):
        self.volumen=volumen        # Volumen in ml

#Hauptprogramm

tasse=Behaelter(250)
print("In der Tasse sind",tasse.volumen,"ml")

ex=input("wie viel ml möchten Sie entnehmen: ")

tasse.Volumen=tasse.volumen - float(ex)       # Hier wurde "volumen" versehentlich mit einem großen "V" geschrieben, was ein neues Attribut erzeugt hat
print("Neuer Inhalt:",tasse.volumen, "ml")

#richtig:
tasse.volumen=tasse.volumen - float(ex)
print("Neuer Inhalt:",tasse.volumen, "ml")

