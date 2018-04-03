# Definition von Klassen für die Programmierung der Musical-Verwaltung

import pickle

from musical import *

class Manager(object):
    __menuetext ="""   
        Musical Manager
        ---------------
        (n)eue Vorstellungen
        (U)eberblick Vorstellungen
        (s)torniere Vorstellung
        (E)nde
        """                 #Klassenattribut

    def __init__(self, datei):
        self.__datei = datei
        self.__lade_musical()
        self.__run()

    def __run(self):
        """Menü und Verarbeitung von Auswahlen"""
        print(self.__menuetext)

        wahl = "-"
        while wahl not in ["e","E"]:
            wahl = input("Auswahl: ")
            if wahl in ["n", "N"]:
                self.__neueVorstellung()
            elif wahl in ["u","U"]:
                print(str(self.__musical))
                #print(self.__musical.getZuschauer())
                print(self.__menuetext)
                wahl = input("Auswahl: ")
            elif wahl in ["s", "S"]:
                self.__storniere()

        print("Danke für die Verwendung von Musical-Manager")
        self.__speichern()

    def __neueVorstellung(self):
        """Dialog zum Einrichten einer neuen Vorstellung"""
        datum = input("Termin: ")
        beginn = input("Beginn der Vorstellung: ")
        vorstellung = Vorstellung(datum, beginn, self.__musical.saal)
        self.__musical.neueVorstellung(vorstellung)

    def __neuesMusical(self):
        """Dialog zur Definition eines neuen Musicals"""
        titel = input("Titel: ")
        eintrittspreis = float(input("Eintrittspreis: "))
        anzahl_reihen = int(input("Anzahl an Sitzreihen: "))

        liste = []
        for i in range(anzahl_reihen):
            sitze = int(input("Anzahl an Sitzen pro Reihe " + str(i) + ": "))
            liste.append(sitze)
            saal = Saal(liste)
            self.__musical = Musical(titel, eintrittspreis, saal)

    def __storniere(self):
        datum = input("Datum: ")
        text = self.__musical.storniere(datum)
        print(text)

    def __lade_musical(self):
        """Musical-Objekt wird geladen, falls Datei vorhanden,
            sonst muss neues Musical definiert werden"""
        try:
            f = open(self.__datei, "rb")
            self.__musical = pickle.load(f)
            f.close()

            print("\n Willkommen")
            print("beim Management-System für das Musical",
                  self.__musical.titel)

        except:
            print("Kein Musical gespeichert.")
            print("Richten Sie ein neues Musical ein.")
            self.__neuesMusical()

    def __speichern(self):
        """Musical-Objekt speichern"""
        f = open(self.__datei, "wb")
        pickle.dump(self.__musical, f)
        f.close()

m=Manager("daten/hairspray.txt")
print(m)

