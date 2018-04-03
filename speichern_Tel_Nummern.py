#Speichern eine Liste mit Telefonnummern

try:
    tel="""Tim 85675 Jenny 233325 Max 89923"""
    teldatei=open("Daten/tel_nr.txt","w")   # Trennung zwischen Verzeichnis und Dateiname mit "/" nicht mit "\"!
    teldatei.write(tel)
    teldatei.close()
except:
    print("Kann Datei nicht öffnen.")

teldatei=open("Daten/tel_nr.txt","r")
