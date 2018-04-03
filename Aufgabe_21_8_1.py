# Schreiben Sie eine Funktion

from math import *


def quadGl(p, q):

    # Prüfe Vorbedingung
    assert (p/2)**2-q >= 0

    x1 = -p/2 + sqrt((p/2)**2 - q)
    x2 = -p/2 - sqrt((p/2)**2 - q)

    # Prüfe Nachbedingung
    assert (x1**2 + p*x1 +q ==0) and (x2**2 + p*x2 +q ==0)

    return x1, x2
    
