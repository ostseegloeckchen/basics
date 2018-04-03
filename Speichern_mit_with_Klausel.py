#öffnen einer Datei mit der "with"-Funktion als sicherheit 
with open("Daten\gold.txt") as f:   #nach dem with-Statement schließt sich die Datei wieder 
    print(f.readline())
