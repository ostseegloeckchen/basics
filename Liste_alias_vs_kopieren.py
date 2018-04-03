#ein Objekt bekommt zwei Namen
liste1=[[1,2],[3,4]]
print(liste1)

liste2=liste1
print(liste2)

print()

#das Objekt liste1 wird kopiert
liste3=liste1[:]   #liste3 ist der Name eines neuen Objektes (mit eigener Identität)
print(liste3)

print()

#an liste1 wird ein Element angehängt --> mit Auswirkung auf liste2
liste1.append([5,6])
print(liste1)
print(liste2)
print(liste3)

print()


