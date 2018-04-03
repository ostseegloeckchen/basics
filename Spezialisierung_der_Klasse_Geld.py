# Spezialisierung der Klasse "Geld_2"

import time

from geld2 import Geld_2                     # Der Name der Basisklasse "Geld_2" wird aus dem Modul "geld2" importiert, was sich im gleichen Verzeichnis befindet

class Konto(Geld_2):
    """Spezialisierung der Klasse Geld zur Verwaltun eines Kontos

        Öffentliche Attribute:
            geerbt: waehrung, betrag, wechselkurs

        Öffentliche Methoden und Überlagerungen:
            geerbt: __add__(), __lt__(),
                    __le__(), __eq__(), get_Euro()
            überschrieben: __str__()

            Erweiterungen: einzahlen(), auszahlen(),drucke_Kontoauszug()"""

    def __init__(self, waehrung, inhaber):
        Geld_2.__init__(self, waehrung, 0)  #2 Aufruf der __init__()-Methode der Basisklasse "Geld_2", bei der Eröffnung des Kontos hat das Attribut "Betrag" den Wert "0"
        
        self.__inhaber = inhaber            #3  neues Attribut: "Inhaber"
        self.__kontoauszug = [str(self)]    #4 Der Kontoauszug wird als String ausgegeben. Warum [str(self)] in []?

    def einzahlen(self, waehrung, betrag):  #5 Erhöhung des Kontostandes um den eingezahlten Geldwert
        einzahlung=Geld_2(waehrung, betrag)
        self.betrag=(self + einzahlung).betrag  #6 Beschreibung siehe S. 303
        eintrag=time.asctime() + " " + str(einzahlung) +\
                 "neuer Kontostand: " + self.waehrung +\
                 "" + format(self.betrag, ".2f")
        self.__kontoauszug += [eintrag]     # Warum [eintrag] in []?

    def auszahlen(self, waehrung, betrag):
        self.einzahlen(waehrung, -betrag)   #Ist hier "self.einzahlen" richtig oder muss hier "self.auszahlen" hin?

    def drucke_Kontoauszug(self):           
        for i in self.__kontoauszug:
            print(i)
        self.__kontoauszug = [str(self)]    # Warum [str(self)] in  []?

    def __str__(self):                      
        return "Konto von" +self.__inhaber + \
               ": \n Kontostand am " +time.asctime() + \
               ":" + format(self.betrag, ".2f") + \
               + " " + self.waehrung

