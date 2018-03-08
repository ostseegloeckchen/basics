#Strukturierung eines langen Anweisungsblocks
for i3 in [0, 1]:
    for i2 in [0, 1]:
        for i1 in [0, 1]:
            for i0 in [0, 1]:
                print(i3, i2, i1, i0, end="  ") #zwischen den beiden "" stehen zwei Leerzeichen, dann trennen sich die Blöcke der binären Zahlen
                #ende for i0
            #ende for i1
        print()
        #ende for i2
    #ende for i3
