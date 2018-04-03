#Aufbau eines Dictionarys aus einer Liste
#ordnet den Schlüsselwörtern A, B und C die Elemente mit gleichem Anfangsbuchstaben zu


liste=["Auto","Apfel","Cello","Banane","Berg"]
d={}
for key in "ABC":
    d[key]=[w for w in liste if w[0]==key]

print(d)

