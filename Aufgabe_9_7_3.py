#Programmierung eines Telefonbuches

import pickle

def erzeuge_tel():
    try:                                #1 Laden eines Dictionary, welches zuvor mit pickle.dump()gespeichert wurde
        f=open("Daten/tel.txt","rb")   #1.1 Trennung von Verzeichnis und Dateiname mit "/" nicht mit "\"!!! 
        t=pickle.load(f)
        f.close
    except:                             #2 bei Fehler wird leeres Dictionary zurück gegeben
        t={}
    return t

def recherche():                        #3 Zugriff auf globales Dictionary
    name=input("Name: ")
    if name in tel.keys():
        print("Nummer: ",tel[name])
    else:
        print("Name unbekannt")

def verabschiedung():                   #4 Speicherung des globalen Dictionary "tel" in einem Unterverzeichnis
    print("Danke, dass Sie dieses Produkt verwendet haben.")
    f=open("Daten/tel.txt","wb")
    pickle.dump(tel,f)
    f.close()

def menue():
    eingabe=""                          #5 Zuweisung eines Anfangswertes zur Variablen "eingabe"
    while eingabe not in ["e","E"]:     #6 solange Benutzer nicht e oder E eingibt, Durchlauf der while-Schleife
        print()
        print("(S)uche nach Telefonnummer")
        print("(N)eue Nummer eintragen")
        print("(A)lle Nummern ausgeben")
        print("(E)nde")
        print()

        eingabe=input("Ihre Wahl: ")
        if eingabe in ["S","s"]:recherche()     #7 
        elif eingabe in ["A","a"]:ausgeben()
        elif eingabe in  ["N","n"]:neu()

def ausgeben():
    print("Name","Nummer",sep="\t") #8 Tabulator als "Trennmittel" für tabellarische Wiedergabe
    print(30*"_")
    for k in tel.keys():
        print(k, tel[k],sep="\t")

def neu():
    global tel                      #9 Veränderung des globalen Dictionarys "tel"
    name=input("Name: ")
    nummer=input("Nummer: ")
    tel[name]=nummer
    print("Neuer Eintrag gespeichert.")

#Hauptprogramm

tel=erzeuge_tel()                   #10
menue()
verabschiedung()


#3 globales Dictionary heißt, das der Name "tel" im Hauptprogramm definiert wird und
#3 nicht in dieser Funktionsdefinition

#5 Zuweisung eines Anfangswertes zur Variablen "eingabe", sonst gibt es bei der while-Schleife einen Fehler

#7 Falls der eingegebene Buchstabe (Inhalt der Variablen eingabe) in der Liste ["S","s"] enthalten ist,
#7 wird die Funktion recherche() aufgerufen.

#9 Eintrag eines neuen Schlüssel : Wert-Paares, daher global

#10 An dieser Stelle wird durch einen Aufruf der Funktion erzeuge_tel() die Variable tel defiiert,
#10 welche von mehreren Funktionen als globale Variable verwendet wird.
