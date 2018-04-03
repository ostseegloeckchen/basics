#Dieses Skript funktioniert nicht!!!

#Erstellen einer Liste von wilkürlich gewählten Buchstaben



def enthalten_buchstaben(s,      #Wilkürlich erstellte Liste von Buchstaben
                        x       #gewählter Buchstabe nach dem gesucht werden soll
                        ):
    
    print(s)            
    if len(s)==1:       #1
        if s[0]==x:     #2
            return "Ja"
        else:
            return "Nein"
    else:
        m=s[len(s)//2]
        if x>=m:        #dieser Ausdruck funktioniert nicht, da Str nicht mit int vergleichbar ist!!!
            return enthalten_buchstaben(s[len(s)//2:],x) #rekursiver Aufruf, Suche rechts weiter
        else:
            return enthalten_buchstaben(s[:len(s)//2],x) #rekursiver Aufruf, Suche links weiter


import random
def s():

    buchstaben="abcdefghijklmnopqrstuvwxyz"
    random_buchstaben=[]
 
    random_buchstaben=random.sample(range(1,26),16)
    random_buchstaben.sort()
    print(random_buchstaben)

    for i in range(16):    
        print(buchstaben[random_buchstaben[i]])

#1 Dokumentation der Arbeitsweise der Funktion (gibt den aktuellen Suchbereich aus)
#2 Wenn der Suchbereich nur noch aus einem einzigen Element besteht, dann vergleicht die Funktion
#2 dieses Element mit dem gesuchten Objekt
