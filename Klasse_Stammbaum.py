# Klassen-Definitionen um einen Stammbaum zu erstellen

class Stammbaum(object):
    def __init__(self, name, vater, mutter):
        self.name = name    # String!!
        self.vater = vater
        self.mutter = mutter

    def __str__(self):
        s=""
        if self.name:
            s += self.name + "\n"
            if self.mutter:
                s += "Mutter von " + self.name +\
                     ": " + str(self.mutter)    # Rekursiver Aufruf

            if self.vater:
                s += "Vater von " + self.name +\
                     ": " + str(self.vater)     # Rekursiver Aufruf

        return s

#Hauptprogramm

sarah = Stammbaum("Sarah", None, None)      # mit den Großeltern von "Jenny" anfangen
willy = Stammbaum("Willy", None, None)

marianne = Stammbaum("Marianne", None, None)
anton = Stammbaum("Anton", None, None)

marlene = Stammbaum("Marlene", willy, sarah)
werner = Stammbaum("Werner", anton, marianne)

jenny = Stammbaum("Jenny", werner, marlene)

print(jenny)

input("Beenden mit <ENTER>")
