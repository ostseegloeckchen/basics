#Sicherung einer Datei als Sicherungskopie  mithilfe der "finally"-Klausel

daten=input("Daten: ")  #Daten ohne "" eingeben
pfad=input("Pfad: ")    #Daten ohne "" aber mit Endung (z.B. ".txt")eingeben

try:
    f=open(pfad,"w")
    f.write(daten)
    f.close()
    print("Daten gespeichert")
finally:                
    f=open("Daten\daten.bak","w")
    f.write(daten)
    f.close()
    print("Sicherheitskopie im Verzeichnis'\Daten'")
print("Programm beendet")
