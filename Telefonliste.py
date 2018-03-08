#Telefonliste erstellen
print("Bitte geben Sie Name und Telefonnummer ein.")

tel_liste=[]

name=input("Name: ")
tel=input("Telefonnummer: ")
tel_liste+=[(name,tel)]

name=input("Name: ")
tel=input("Telefonnummer: ")
tel_liste+=[(name,tel)]

name=input("Name: ")
tel=input("Telefonnummer: ")
tel_liste+=[(name,tel)]

print(tel_liste)

print("Telefonliste: ")
print(tel_liste[0][0], tel_liste[0][1])
print(tel_liste[1][0], tel_liste[1][1])
print(tel_liste[2][0], tel_liste[2][1])
