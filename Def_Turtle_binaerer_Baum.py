from turtle import *

def baum(x):
    if x<5: return   #Abbruch der Rekursion
    else:
        forward(x)
        left(45)
        baum(x/2)    #Rekursiver Aufruf: Links wird ein kleinerer Binärbaum gezeichnet.
        right(90)    
        baum(x/2)    #Rekursiver Aufruf: Rechts wird ein kleinerer Binärbaum gezeichnet
        left(45)     #Die Turtle wird wieder an ihre Startposition manövriert.
        back(x)
    return

left(90)             #Hier beginnt das Hauptprogramm. Zunächst wird dafür gesorgt, dass die Turtle nach oben zeigt.
baum(50)
hideturtle()         #Turtle verstecken --> schöneres Bild
