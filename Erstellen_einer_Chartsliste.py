#Erstellen einer Chartsliste

def eingabe(charts):
    print("Eintragungen (mit ENTER beenden)")
    titel=input("Titel: ")
    while titel:                                        
        interpret=input("Interpret: ")
        charts+=[[0,titel,interpret]]
        titel=input("Titel: ")
    print()
    print("Vielen Dank. Ihre Liste wird gespeichert.")

def speichern(charts):
    import pickle                                       #1
    f=open("c:\\charts\\charts.txt","wb")               #2
    pickle.dump(charts,f)                               #3
    f.close()                                           #4

def ausgabe(charts):
    print("Die Charts")
    print("------------")
    for i in range (len(charts)):                       #5
        eintrag=charts[i]
        print("Platz",i+1,":",eintrag[1],"\t von",
              eintrag[2],"\t",eintrag[0],"Stimmen")


#Hauptprogramm
print("Erstellen Sie eine Hitliste.")
charts=[]
eingabe(charts)
ausgabe(charts)
speichern(charts)

#1 Mithilfe der dump()-Funktion des Moduls pickle kann ein beliebiges Objekt gespeichert werden.
#2 Hier wird ein File-Objekt mit dem Namen f erzeugt.
#2 Dabei wird eine Datei mit dem Dateipfad "" zum Schreiben geöffnet bzw. neu angelegt.
#2 Die Escape-Sequenz \\ stellt einen einzelnen Backslash "\" dar.
#2 Das Argument "wb" bedeutet: Die Datei wird zum Schreiben geöffnet (w) und es wird ein Bytestring (b) gespeichert.
#3 Die Liste charts wird im File-Objekt f in Form eines Bytestrings abgespeichert
#4 Die Datei wird geschlossen und damit physisch abgespeichert.
#5 Die Tabelle mit den Musiktiteln wird zeitweise ausgegeben. Die Escape-Sequenz "\t" repräsentiert ein Tabulatorzeichen

