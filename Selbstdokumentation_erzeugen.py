# Das Programm dazu bringen zu dokumentieren, was es gerade gemacht hat

import random

def quicksort(s):
    if __name__ == "__main__":
        if len(s) > 0:
            print("Ich sortiere: ", s)
            print("Element zum Spalten der Liste: ", s[0])

    if len(s) <= 1:
        return s

    else:
        return quicksort([x for x in s[1:] if x < s[0]]) \
               + [s[0]] \
               + quicksort([y for y in s[1:] if y >= s[0]]) # Rekursive Schleife

if __name__ == "__main__":
    s = [random.randint(0, 100) for i in range(8)]
    print(quicksort(s))
