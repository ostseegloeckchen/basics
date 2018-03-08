def summe(liste):
    if len(liste)==0:
        return 0
    else:
        return liste[0]+summe(liste[1:])  #rekursiver Aufruf
