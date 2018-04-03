#Sortierung einer Liste mit bubblesort
def bubblesort(s):
    if len(s)>1:                                #1
        print("Liste ist sortiert")
        for i in range (len(s)-1):              #2
            for j in range (len(s)-1):
                if s[j]>s[j+1]:
                    s[j],s[j+1]=s[j+1],s[j]     #3
            print(s)                            #4
            

s=[45,4,87,12,34,51,29,14,67,22,68,11,51,48,99,2]
bubblesort(s)

#1 Wenn Länge der Liste=1, dann ist sie bereits sortiert und es geschieht nichts
#2 Die Liste wird nun von vorne nach hinten "durchwandert" und
#2 benachbarte Elemente verglichen
#3 Falls das 1. Element größer als das 2. Element, dann werden sie vertauscht
#4 Der aktuelle Zustand der Liste wird nach jedem Schleifendurchgang ausgegeben

print()

def bubblesort(s1):
    if len(s1)>1:
        for i in range (len(s1)-1):
            for j in range (len(s1)-1):
                if s1[j]>s1[j+1]:
                    s1[j],s1[j+1]=s1[j+1],s1[j]
            print(s1)

s1=[10,9,8,7,6,5,4,3,2,1]
bubblesort(s1)
