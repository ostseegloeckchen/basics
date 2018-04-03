#Erstelle ein Englisch-Deutsches Wörterbuch

def erschaffe_woerterbuch():
    d={}
    englisch=input("Englisches Wort: ")
    while englisch:                             #1
        deutsch=input("Deutsche Übersetzung: ")
        d[englisch]=deutsch
        englisch=input("Englisches Wort: ")
    return d

print(erschaffe_woerterbuch())

#1 Die "while"-Schleife bricht ab,
#1 wenn der Benutzer nach dem Promt "Englisches Wort:"
#1 sofort die ENTER-Taste drückt.
#1 In diesm Fall erhält die Variable "englisch" einen leeren String
#1 mit dem Wahrheitswert FALSCH.
