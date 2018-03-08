from turtle import *

def spirale(x):
    if x<5:
        return          #Abbruch der Rekursion = Wiederkehr
    else:
        forward(x)
        right(90)
        spirale(0.9*x)   #rekursiver Aufruf
        return
