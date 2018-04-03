# Definieren einer eigenen Klasse, hier die Klasse Statistik
# Erzeugen einer sogenannten Toolbox
#Skript funktioniert nicht: Bei der Berechnung des Median ist irgendetwas falsch

class Statistik(object):
    def mittelwert(s):
        if s:
            return float((sum(s))/len(s))

    def spannweite(s):          # größte minus kleinste Zahl der Zahlenliste s
        if s:
            return max(s)-min(s)

    def median(s):
        if s:
            s1=sorted(s)
            if len(s1)%2==0:     # Länge der Liste ist gerade
                return (s1[len(s1)/2-1]+s1[len(s1)/2])/2    # (Wert von s1 an der Position len(s)/2-1 addiert mit dem Wert von s1 an der Position len(s)/2) dividiert durch 2
            else:               # Länge der Liste ist ungerade
                return s1[((len(s1)-1))/2] # Wert an der Position (len(s)-1 dividiert durch 2)

    mittelwert=staticmethod(mittelwert) #2
    spannweite=staticmethod(spannweite)
    median=staticmethod(median)

#2 durch den Aufruf "staticmethod" werden die definierten Methoden zu statischen Methoden der Klasse "Statistik"


#Beispiele

s=[1,4,9,11,5]

Statistik.mittelwert(s)
Statistik.median(s)
Statistik.spannweite(s)
