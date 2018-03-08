print("Bitte geben Sie eine Zahl zwischen 1 und 10 ein.")
while True:         #Heißt das, solange man eine Zahl eingibt erfolgt der Test, dass die Zahl zwischen 1 und 10 liegt?
    zahl=input("Zahl: ")
    if 1<=int(zahl)<=10:
        break       #Zahl ist in Ordnung
    else:
        print("Die Zahl muss zwischen 1 und 10 liegen.")
print("Danke für die Zahl.")
