# assert-Anweisungen einbauen, um logische Fehler zu vermeiden

def primfak(zahl):

    # Prüfe Vorbedingung
    assert (type(zahl) == int) and (zahl > 1)

    x = zahl
    fak = [1]
    faktor = 2
    while x > 1:                # zahl muss größer als 1 sein
        while x%faktor == 0:    # zahl muss von Typ int sein
            fak.append(faktor)
            x /= faktor
        faktor += 1

    # Prüfe Nachbedingung
    produkt = 1
    for i in fak:
        produkt *= i
    assert produkt == zahl
        
    return fak

# Hauptprogramm

zahl = (int(input("Zahl: ")))
print(primfak(zahl))

# Testaufruf

if __name__ == "__main__":
    primfak(15)
    primfak(-2)
