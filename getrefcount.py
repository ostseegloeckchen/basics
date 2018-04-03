# Zählen wie viele Namen = Referenzen ein Objekt hat

import sys

class Ding:
    pass

a = Ding    # Objekt der Klasse Ding mit Namen a

print(sys.getrefcount(a))

print()

b = c = a   # weitere Namen für das gleiche Objekt

print(sys.getrefcount(a))

print()

print(sys.getrefcount(b))

print()

del b

print(sys.getrefcount(a))

print()

print(sys.getrefcount(10))

print()

x=10

print(sys.getrefcount(10))
