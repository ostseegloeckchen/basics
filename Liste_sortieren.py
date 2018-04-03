#Elemente einer Liste sortieren
liste=[9,5,4,8,3,7,6]
print(liste)

liste.sort()
print(liste)

print()

#Elemente einer Liste absteigend sortieren
liste.sort(reverse=True)
print(liste)

print()

liste1=["a","z","d","f","h","g","l","r","m","p"]
print(liste1)

liste1.sort()
print(liste1)

print()

#Elemente einer Liste absteigend sortieren
liste1.sort(reverse=True)
print(liste1)

print()

#Sequenz-Objekte können auch sortiert werden
liste2=[[1,3,9],[0,2,8],[0,2,9]]
print(liste2)

liste2.sort()
print(liste2)

print()

#Objekte nach ihrer Länge sortieren
liste3=["Gegenwart","Vergangenheit","Zukunft"]
print(liste3)

liste3.sort(key=len)
print(liste3)

print()

#Elemente einer Liste absteigend sortieren
liste3.sort(key=len,reverse=True)
print(liste3)

