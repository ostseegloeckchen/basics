#Anfertigen einer Datei mit den Startnummern von Marathonläufern
#und ihren Ankunftszeiten

import time

startnr= " "

try:
   f=open("Daten\Marathon.txt","w")
   while startnr !="":
       startnr=input("Startnummer (Ende mit <ENTER>): ")
       f.write(startnr + ":" + time.asctime() + "\n")
       f.flush()
   print()
   print("Die Daten befinden sich in der Datei/Daten/Marathon.txt")
   f.close()
except:
    print("Speichern hat nicht geklappt.")




