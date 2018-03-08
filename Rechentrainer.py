#fünf Rechenaufgaben
print("Multiplikationstrainer")
print("----------------------")

import random

import time
start=time.time()

for i in range(5):
    a=random.randint(1,10)
    b=random.randint(1,10)

    ergebnis=-1

    while ergebnis !=a*b:
        ergebnis=int(input(str(a)+"*"+str(b)+"="))

        if ergebnis==a*b:
            print("Richtig!")
        else:
            print("Leider falsch, versuche es noch einmal.")
        
ende=time.time()

dauer=ende-start
print("Für diese Aufgaben hast du",round(dauer,1),"Sekunden benötigt.")



