# Eine Datenbank anlegen

import sqlite3

verbindung1 = sqlite3.connect("Dateien/beispiel1.db") 

c = verbindung1.cursor()    #Instanziieren eines Boten = Cursors
c.execute("""CREATE TABLE person(name VARCHAR(50), tel VARCHAR(20))""") #"person" und "tel" sind die Namen der ersten und zweiten Spalte und haben jeweils den Datentyp "Varchar" 

c.execute("""INSERT INTO person VALUES("Melanie Beck", "123 987654")""")    # Einfügen von Daten in die Tabelle, zeilenweise
c.execute("""INSERT INTO person VALUES("Moritz Blau", "123 987534")""")
c.execute("""INSERT INTO person VALUES("Tim Groß", "123 987345")""")

verbindung1.commit()    # Speichern von Veränderungen

c.close()   # Schließen des Cursors


c = verbindung1.cursor()
ergebnis = c.execute("SELECT * FROM person")   # Abfrage der Daten aus allen Zeilen
for zeile in c:
    print(zeile)

verbindung1.commit()

liste = list(ergebnis)
print(liste)

print()

print(liste[0])

#verbindung.close()  # Verbindung zu der Datenbank schließen


