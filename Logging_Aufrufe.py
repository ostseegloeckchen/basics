# Auftrag an das Programm Log-Einträge zu schreiben

import logging

logging.basicConfig(filename = "Log_Dateien/logging1.txt",
                    level = logging.INFO,
                    filemode = "w") # info siehe Text in Buch S. 589

def merge(s1, s2):                  # die Funktion "merge" mischt zwei sortierte Listen so, dass eine einzige längere sortierte Liste entsteht
    logging.debug("Starte merge({}, {}): ".format(str(s1), str(s2)))

    if s1 == []:
        ergebnis = s2               #wenn eine der beiden Listen leer ist, dann ist die andere Liste das ergebnis

    elif s2 == []:
        ergebnis = s1

    else:
        a, b = s1[0], s2[0]
        if a <= b:
            ergebnis = [a] + merge(s1[1:], s2)  # stellt das kleinste Element der einen bzw. der anderen Liste an den Anfang 
        else:
            ergebnis = [b] + merge(s1, s2[1:])

    logging.debug("Ergebnis von merge({}, {}): {}".format(str(s1), str(s2), str(ergebnis)))

    return ergebnis

def msort(s):
    logging.info("msort({})".format(str(s)))

    if len(s) <= 1:
        ergebnis = s

    else:
        n = len(s)//2   # Ganzzahlige Division
        s1 = s[:n]      # Aufteilung einer Kopie der Liste in zwei Hälften
        s2 = s[n:]

        ergebnis = merge(msort(s1), msort(s2))  # Rekursiver Aufruf zum sortieren und mischen der Elemente der beiden Hälften

    logging.info("Ergebnis von msort({}): {}".format(str(s), str(ergebnis)))

    return ergebnis

# Test des Programms

if __name__ =="__main__":
    s = [7, 13, 15, 1, 12, 11, 3, 6, 10, 2, 8, 14, 0, 4, 9, 5]
    print(msort(s))
