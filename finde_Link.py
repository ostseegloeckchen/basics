# Analyse eines Textes: Vorkommen von Links

from re import *

def linkfind(datei):
    re = compile("https?://.+(?:html?|/)", I)   #1
    f = open(datei, "r")
    text = f.read()
    f.close()

    return re.findall(text)


#Hauptprogramm
linkliste = linkfind("LICENSE.txt")

print("Links in der Python-LICENSE-Datei: ")
for link in linkliste:
    print(link)

#1 Die Sequenz "?:" am Anfang des Ausdrucks "(?:html?|/)"
#1 ist notwendig, damit "findall()" den gesamten passenden
#1 Substring zurückgibt
    
