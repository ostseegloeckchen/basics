# Ein Wörterbuch erstellen und nutzen
# Die Speicherung von Wörtern funktioniert nicht


import pickle

class Woerterbuch(object):
    def __init__(self, dateiname, sprache1, sprache2):
        self.__pfad = dateiname
        
        try:
            datei = open(self.__pfad, "rb")
            self.__vokabeln=pickle.load(datei)
            datei.close()

        except:
            self.__vokabeln={}

        self.sprache1 = sprache1    # Achtung bei der Einrückung, damit es nicht zu "except" gehöhrt
        self.sprache2 = sprache2    

    def speichere(self):
        datei = open(self.__pfad, "wb")
        pickle.dump(self.__vokabeln, datei)
        datei.close()

    def neu(self, wort1, wort2):
        if wort1 not in self.__vokabeln.keys():
            self:__vokabeln[wort1] = [wort2]
        else:
            self.__vokabeln[wort1] += [wort2]   # man kann solange ein englisches Wort eingeben, bis man ohne Eingabe auf ENTER drückt

    def uebersetze(self, wort):
        if wort in self.__vokabeln.keys():
            return self.__vokabeln[wort]
        else:
            return ["Wort unbekannt"]   # Warum in []?

class Benutzeroberflaeche(object):
    __menuetext = """Bitte wählen Sie!
    (N)eues Wort eingeben
    (U)ebersetzung
    (E)nde
    """
    def __init__(self, woerterbuch):
        self.__wb = woerterbuch

    def run(self):
        wahl = " "
        
        while wahl not in "Ee":
            print(self.__menuetext)
            wahl = input("Ihre Wahl: ")
            if wahl in "Nn":
               self.__neu()
            elif wahl in "Uu":
               self.__uebersetze()

        print("Danke für die Verwendung des Wörterbuches!")

        self.__wb.speichere()
        print(self.__wb.speichere())

    def __neu(self):
        wort = input(self.__wb.sprache1 + ":")
        uebersetzung = input(self.__wb.sprache2 + ":")
        while uebersetzung != "":                           # solange ein Wort eingegeben wird frage nach der Übersetzung
            self.__wb.neu(wort, uebersetzung)
            uebersetzung = input(self.__wb.sprache2 + ":")
            
        
    def __uebersetze(self):
        wort1 = input(self.__wb.sprache1 + ":")
        print(self.__wb.sprache2 + ": ", end = "")
        for uebersetzung in self.__wb.uebersetze(wort1):
            print(uebersetzung, end = "")

        print()
        print()

# Hauptprogramm

pfad = "englisch.wb"    # relative Addresse der Wörterbuch-Datei
w = Woerterbuch(pfad, "Deutsch", "Englisch")
menue = Benutzeroberflaeche(w)
menue.run()


    
