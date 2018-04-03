import random
def s():

    buchstaben="abcdefghijklmnopqrstuvwxyz"
    random_buchstaben=[]

    random_buchstaben=random.sample(range(1, 26), 16)
    random_buchstaben.sort()
    
    for i in range(16):
        print(buchstaben[random_buchstaben[i]])

    
    print("Zufallsbuchstaben : ")
    print(random_buchstaben)



s()
