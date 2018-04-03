def enthalten_zahl(s, #Wilkürlich erstellte Liste von Werten
              x  #gewählter Wert nach dem gesucht werden soll
              ):
    print(s)            #1
    if len(s)==1:       #2
        if s[0]==x:
            return "Ja"
        else:
            return "Nein"
    else:
        m=s[len(s)//2]
        if x>=m:
            return enthalten_zahl(s[len(s)//2:],x) #rekursiver Aufruf, Suche rechts weiter
        else:
            return enthalten_zahl(s[:len(s)//2],x) #rekursiver Aufruf, Suche links weiter


#Hauptprogramm
import random
s=[random.randint(0,100) for i in range(16)] #Gibt wilkürlich 19 Werte aus dem Bereich 1 bis 100 aus
s.sort()

#1 Dokumentation der Arbeitsweise der Funktion (gibt den aktuellen Suchbereich aus)
#2 Wenn der Suchbereich nur noch aus einem einzigen Element besteht, dann vergleicht die Funktion
#2 dieses Element mit dem gesuchten Objekt
