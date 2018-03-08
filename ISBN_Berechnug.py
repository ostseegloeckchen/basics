#Berechnung der Prüfziffer (=10. Ziffer) einer ISBN
#Eingabe
a=int(input("Bitte geben Sie die 1. Nummer der ISBN ein: "))
b=int(input("Bitte geben Sie die 2. Nummer der ISBN ein: "))
c=int(input("Bitte geben Sie die 3. Nummer der ISBN ein: "))
d=int(input("Bitte geben Sie die 4. Nummer der ISBN ein: "))
e=int(input("Bitte geben Sie die 5. Nummer der ISBN ein: "))
f=int(input("Bitte geben Sie die 6. Nummer der ISBN ein: "))
g=int(input("Bitte geben Sie die 7. Nummer der ISBN ein: "))
h=int(input("Bitte geben Sie die 8. Nummer der ISBN ein: "))
i=int(input("Bitte geben Sie die 9. Nummer der ISBN ein: "))

#Verarbeitung
s=1*a+2*b+3*c+4*d+5*e+6*f+7*g+8*h+9*i

ziffer=s%11

#Ausgabe
print("\nQuersumme: ",s)
print("Ihre Prüfziffer lautet",ziffer)
