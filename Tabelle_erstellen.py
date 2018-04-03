# Erstellen einer Tabelle mit Platzhaltern und Zeichenformatierung
# die Zahlen sollen rechtbündig in der Tabelle erscheinen (">") und
# die Spalten sollen eine Breite von 7 Punkten ("7") haben

tabelle1 = ""
for i in range(1,6):
    tabelle1 += "{a:>7}{b:>7}{c:>7}\n".format(a=i, b= i*i, c=i*i*i)

print(tabelle1)

print()

# die Zahlen sollen linksbündig in der Tabelle erscheinen ("<") und
# die Spalten sollen eine Breite von 7 Punkten ("7") haben

tabelle2 = ""
for i in range(1,6):
    tabelle2 += "{a:<7}{b:<7}{c:<7}\n".format(a=i, b= i*i, c=i*i*i)

print(tabelle2)

print()

# die Zahlen sollen zentriert in der Tabelle erscheinen ("^") und
# die Spalten sollen eine Breite von 7 Punkten ("7") haben

tabelle3 = ""
for i in range(1,6):
    tabelle3 += "{a:^7}{b:^7}{c:^7}\n".format(a=i, b= i*i, c=i*i*i)

print(tabelle3)
