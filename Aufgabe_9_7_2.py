#Anfertigen eines Programms zur Wiedergabe von Daten in tabellarischer Form

inhalt=[("Gold",0.1234),("Silber",23.45),("Platin",0.0678)]

for i in inhalt:                                    # for-Schleife wichtig!
    print(i[0],":", format(i[1],"6.2f"),sep="\t")   #1

#1 Schreibe das 1. Element des Tupels (i[0]) und
#1 formatiere das 2. Element des Tupels (i[1])
