#Berechnung der Oberfläche eines Quaders
laenge=6
breite=2
hoehe=3

oberflaeche=2*(
            breite*hoehe    #Vorder- und Rückseite
            +laenge*breite  #Ober- und Unterseite
            +laenge*hoehe)   #rechte und linke Seite

print(oberflaeche)
            
