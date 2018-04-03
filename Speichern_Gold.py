#Speichern von Str und umwandeln in vorherige Datentyp

def speichern(s,dateiname):
    try:
        datei=open(dateiname,"w")
        for i in s:
            datei.write(str(i)+"\n")
        datei.close()
    except:
        print("Speichern nicht möglich")
    

liste=["Gold",123.2,-17]
speichern(liste,"Daten\gold3.txt")  #1 
f=open("Daten\gold3.txt","r")
daten=f.read()
print(daten)

#1 dieses Skript funktioniert sowohl mit einem "\" als auch
#1 mit einem "/" zwischen dem Verzeichnis und dem Dateinamen
