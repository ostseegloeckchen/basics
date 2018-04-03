#Programmieren eines Wörterbuches
#Das Wörterbuch muss erst noch geschrieben werden, jetzt ist es leer

import random

def dict_laden(pfad):           #Das Wörterbuch wird aus einer Textdatei erstellt
    d={}
    try:
        datei=open(pfad)
        liste=datei.readlines()
        for eintrag in liste:
            l_eintrag=eintrag.split()
            d[l_eintrag[0]]=l_eintrag[1:]
        datei.close()
    except:
        pass
    return d

def aufgabe(d):
    zufall=random.randint(0,len(d.keys())-1)
    vokabel=list(d.keys())[zufall]              #2 Auswahl einer zufälligen Vokabel
    print("Wie lautet das deutsche Wort für",vokabel+"?")
    antwort=input()                             # Eingabe der Übersetzung

    if antwort not in d[vokabel]:               #4 falls Eingabe nicht mit gespeichertem übereinstimmt, Ausgabe des Gespeicherten
        print("Leider falsch.")
        print(vokabel,"bedeutet:",end=" ")
        for wort in d[vokabel]:
            print(wort,end=" ")
        print()
    else:                                       #5 wenn gewusst, wird Eintrag gelöscht
        print("Richtig!")
        del d[vokabel]

#Hauptprogramm
print("Vokabeltrainer")
print()
woerterbuch=dict_laden("c:\\python\\projekt\\woerterbuch.txt")
while woerterbuch:                              #6
    aufgabe(woerterbuch)
print("Sie haben alle Vokabeln gelernt.")
eingabe=input()

#2 Bei einer Aufgabe wird aus der Schlüsselmenge des Dictionarys
#2 (englische Vokabeln) eine Vokabel nach dem Zufallsprinzip ausgewählt.
#2 Das "dict_keys"-Objekt, welches die Methode keys() zurückgeibt,
#2 muss in eine Liste umgewandelt werden,
#2 damit auf beliebige Elemente zugegriffen werden kann.

#4 Falls die Eingabe nicht mit einem Wort aus der Liste der Übersetzungen übereinstimmt,
#4 gibt es eine negative Rückmeldung und die Liste der deutschen Wörter wird ausgegeben.
#4 Ansosten gilt die Vokabel als gelernt --> positive Rückmeldung --> löschen des Eintrages

#6 Es werden so lange Aufgaben gestellt, bis das Wörterbuch leer ist.
