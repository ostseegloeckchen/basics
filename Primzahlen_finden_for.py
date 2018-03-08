#Schleife mit for-Anweisung
n=int(input("Zahl: "))
for i in range(2,n):
    if n%i==0:
        print(n,"==",i,"*",n//i)
        break
    if i==n-1:
        print(n,"ist eine Primzahl")
        
#Schleife mit if-Anweisung
n=int(input("Zahl: "))
for i in range(2,n):
    if n%i==0:
        print(n,"==",i,"*",n//i)
        break
else:
    print(n,"ist eine Primzahl")
    
