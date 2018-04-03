# mit der assert-Anweisung testen, ob das als Argument übergebene Objekt eine nicht-leere Liste ist

# selbst definierte Funktion entfernt kleinstes Element aus einer Liste

def entferneMin(s):
    assert type(s) == list  # Sichert zu, dass "s" eine Liste ist
    assert len(s) > 0       # Sichert zu, dass Liste nicht leer ist

    m = min(s)
    s.remove(m)


# mit der assert-Anweisung testen, ob eine Diversität vorliegt

def diversitaet(s):
    assert hasattr(s, "__iter__")
    menge = set(s)
    return len(menge)

# mit der assert-Anweisung testen, ob das Objekt eine ganze Zahl ist

assert type(x) == type(1)

# mit der assert-Anweisung testen, ob das Objekt eine Zeichenkette ist

assert type(x) == type("Abend")

# mit der assert-Anweisung testen, ob das Objekt eine (reelle) Zahl ist

assert type(x) in[type(1), type(1.0)]
