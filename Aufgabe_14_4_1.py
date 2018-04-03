# Abfrage des Namens einer Person und
# erstellen eines Verzeichnisses für diese Person
# mit dem entsprechenden Namen

from os import mkdir    # Es geht auch "import os" --> aber dann "os" vor die Funktion schreiben (siehe #2)?

vorname=input("Wie lautet dein Vorname: ")
nachname=input("Wie lautet dein Nachname: ")
verzeichnisname=(vorname[:2] + nachname[:2]).lower()    #fügt die ersten beiden Buchstaben des Vornamens und Nachnamens zusammen

try:
    mkdir("Dateien/" + verzeichnisname) #erzeugt einen Unterordner im Ordner "Dateien" mit dem Namenkürzel der Person
#   os.mkdir("Dateien/" + verzeichnisname)    #2 
    print("Verzeichnis angelegt")

except:
    print("Verzeichnis existiert bereits")
