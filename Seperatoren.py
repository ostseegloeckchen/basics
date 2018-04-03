print("1: ",1,2,3,sep="-")

print()

print("2: ",1,2,3,sep="\t")   #Tabulator

print()

print("3: ",1,2,3,sep="\n")   #neue Zeile (Zeilenumbruch)

print()

print("4: ",1,2,3,end="")    #voreingestellt, verhindert einen Zeilenumbruch

print()

print("5: ",1,2,3)

print()

for i in range(5):
    print(i, end=" ")       #verhindert Zeilenumbruch, bei "end=" "" ist ein Leerzeichen zwischen in den Anführungszeichen

print()

for i in range(5):
    print(i)                #voreingestellt ist hier ein "\n", also ein Zeilenumbruch

print()

s=["Äpfel","Birnen","Pflaumen","Krischen"]
for obst in s:                                          #ende mit einem "oder" wenn obst ist nicht gleich dem letzten Element, 
    print(obst, end=" oder " if obst!=s[-2] else "\n")  # ansonsten mache einen Zeilenumbruch
    
