#Speichern eines Textes

try:                                    #1
    daten=open("Daten\daten1.txt","w")   #2 
    text=input("Bitte geben Sie Ihren Namen ein: ")
    daten.write(text)                   #3
    daten.flush()                       #Zwischenspeicherung der Datei ohne sie zu schließen!
    daten.close()                       # Schließen und speichern der Datei
except:
    print("Kann Datei nicht öffnen.")
    
#1 "Try and excet" -Funktion, um Laufzeitfehler zu vermeiden,
#1 falls Fehler im Pfad oder Ähnliches.

#2 Generierung eines neuen file-Objektes mit dem Namen "daten"
#2 und Verknüpfung mit der externen Datei über den relativen Pfad verknüpft.

#3 Der String "text" wird in die Datei geschrieben und
#3 vorher vorhandener Text gelöscht.
