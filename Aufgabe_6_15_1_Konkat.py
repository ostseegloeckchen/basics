#Schreiben Sie eine Funktion konkat(),
#die beliebig viele String-Objekte als Argumente akzeptiert und
#die Konkatenation dieser Strings zurück gibt.

def konkat(*worte):         #1     
    ergebnis=''
    for wort in worte:
        ergebnis +=wort
    return(ergebnis)

#1 Dem Parameter worte in der Parameterliste wird ein Stern vorangestellt
#1 --> definiert ein Tupel mit ungewisser Länge
