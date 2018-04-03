# Definiere eine Klasse NewList als Erweiterung der Standardklasse list
# zusätzliche Methode "range()"
#       --> liefert Spannweite (Diff. zwischen größtem und kleinstem Element der Liste)
#       sofern es sich um eine -´Liste von Zahlen handelt 

class NewList(list):
    def __init__(self, s=[]):
        s= list(s)
        list.__init__(self, s)  # Improtiert die Klasse "List" mit ihren Attributen. Richtige Wortwahl?

    def range(self):
        try:
            return max(self)-min(self)
        except:
            return 0

#Hauptprogramm
s=NewList(["zwo", "drei","vier"])
print(s.range())
