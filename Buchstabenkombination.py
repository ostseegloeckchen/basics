#Drucke alle Kombinationen mit zwei großen Buchstanben

alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for a in alphabet:
    for b in alphabet:
        print(a+b,end=" ")


