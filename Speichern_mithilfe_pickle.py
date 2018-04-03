#Erzeugen eines Telefonbuchs
telefonbuch=[("Tim","123"),("Jenny","456"),("Max","789")]
datei=open("Daten/tel1.txt","wb")   #hier Trennung zwischen Vereichnis und Dateinamen mit "/" nicht mit "\"!

import pickle

pickle.dump(telefonbuch,datei)

datei.close()
