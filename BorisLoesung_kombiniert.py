import random

def s():

    buchstaben="abcdefghijklmnopqrstuvwxyz"
    random_buchstaben=[]
    random_zahlen=[]

    random_zahlen=random.sample(range(1, 26), 16)
    random_zahlen.sort()

    
    for i in range(16):
        random_buchstaben.append(buchstaben[random_zahlen[i]])
        
    for i in range(16):
        print(random_zahlen[i], end=' ')
        print(random_buchstaben[i])

    kombiniert=[(i,j) for i in random_buchstaben for j in random_zahlen]
    print(kombiniert)       

s()

