# Definition einer eigenen Klasse, hier die Klasse "Ding"
# ohne Attribute und Methoden
# im Anschluss wird ein Objekt mit zwei Attributen zugefügt
# --> Dynamische Erzeugung von Attributen

class Ding(object):
    pass                # Es wurden keine Attribute und Methoden definiert

#Hauptprogramm
kugel=Ding()            # Definition eines Objektes
kugel.masse=100         # mit dem 1. Attribut (Name: "Masse" und Wert: "100")
kugel.material="Gold"   # mit dem 2. Attribut (Name: "Material" und Wert: "Gold")

print(kugel.masse,kugel.material)
