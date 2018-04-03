#Fehler: Die Datei wird nicht geöffnet und deren Inhalt wird so verändert, dass er nicht mehr erkennbar ist!!!
#Erstellen eine Voting Programmes

import pickle

def laden():
    try:
        f=open("c:\\charts\\charts.txt","rb")                   #1
        charts=pickle.load(f)                                   #2
        f=close()                                               #3
    except:
        charts=[]                                               #4
    return charts

def ausgabe(charts):
    print("Die Charts")
    print("----------")
    for i in range (len(charts)):
        eintrag=charts[i]
        print("Platz", i+1, ":", eintrag[1], "\t\ von",
              eintrag[2], "\t", eintrag[0], "Stimmen")

def voting(charts):
    if charts==[]:
        print("Sorry, keine Wahl möglich.")
    else:
        print("Die Charts")
        print()
        ausgabe(charts)
        print("Bitte wählen Sie Ihren Favoriten!",
              "(1 bis ",+str(len(charts))+")")
        wahl = int(input("Nummer: "))-1                         #5
        charts[wahl][0]+=1                                      #6
        charts.sort(reverse=True)                               #7
        print("Vielen Dank! Ihr Voting wird gespeichert.")

def speichern (charts):
    f=open("c:\\charts\\charts.txt","wb")
    pickle.dump(charts, f)
    f.close()

#Hauptprogramm
charts=laden()
voting(charts)
speichern(charts)
print("Hier der neue Stand: ")
ausgabe(charts)


#1 Hier wird ein File-Objekt mit dem Namen f erzeugt und die dazugehörige Datei zum Lesen geöffnet.
#2 Die Liste charts wird aus dem File-Objekt f geladen.
#3 Die Datei wird wieder geschlossen.
#4 Falls es beim Versuch die Datei zu öffen, einen Lauffehler gab
#4 (z.B. weil die Datei nicht existiert),
#4 wird dem Namen charts eine leere Liste zugewiesen.
#5 Die Variable "wahl" enthält den Index des gewählten Titels.
#5 Diese Nummer ist um eins kleiner als die eingegebene Zahl.
#6 Die Anzahl an Stimmen des gewählten Titels wird in den Charts um eins erhöht.
#7 Die Liste mit den Charts wird absteigend sortiert
