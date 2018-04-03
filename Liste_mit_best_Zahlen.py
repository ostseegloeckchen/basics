#Gebe aus alle Zahlen von 0-100, welche durch 7 teilbar sind
c=[i for i in range(100) if i%7==0]
print(c)

print()

#Gebe nur diese Werte aus, die sich in zwei verschiedenen Listen identisch sind
a=[1,3,5,7,9,11,13,15]
b=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
c=[i for i in a if i in b]
print(c)

print()

#Gebe ein Liste aus mit allen Kombinationen der Werte aus zwei verschiedenen Listen
a=["a","b","c"]
b=[1,2,3]
c=[(i,j) for i in a for j in b]
print(c)

print()

#Quadriere alle Werte in der Liste b
b=[i**2 for i in b] #die Quardierung geht auch mit i*i
print(b)
