#Einfügen zweier Zahlen in eine Zeichenkette

text = "Leistung ({} kW) und Höchstgeschwindigkeit ({} km/h) sind hoch" # "{}" sind Platzhalter

print(text.format(80+10, 187.2)) # die Zahlen-Objekte 90 und 187.2 wurden in den String "text" eingefügt

print()

text1 = "Es war {} auf der Treppe und {} im Keller als ich hinunter lief."
print(text1.format("dunkel", "hell")) # die String-Objekte "dunkel" und "hell" wurden in den String "text1" eingefügt

print()

# Einfügen von Objekten in Platzhalter per Angabe der Position in der Parameterliste

basistext = """{0} war {1} Jahre alt.
Mit {1} war sie schon sehr weise.
Eines Morgens, als {0} in den Spiegel schaute, ...."""

print(basistext.format("Tanja", 19))

print()

# Einfügen von Objekten in Platzhalter per Angabe der Schlüsselwortagumente in der Parameterliste

basistext1 = """{name} war {alter} Jahre alt.
Mit {alter} war sie schon sehr weise.
Eines Morgens, als {name} in den Spiegel schaute, ...."""

print(basistext1.format(name="Tanja", alter = 19))

print()

# Einfügen von Objekten in Platzhalter per Angabe der Schlüsselwortagumente
# und einer Zahlenformatierung in der Parameterliste

basistext2 = "Ein Teil kostet {preis:.2f} EUR"  # ":.2f" ist der Formatspezifikator, d.h. die Gleitkommazahl ist auf 2 Stellen hinter dem Komma begrenzt

print(basistext2.format(preis=123.4567))
      
