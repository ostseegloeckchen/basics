from turtle import *

def baum(x):
    if x<5: return   #Abbruch der Rekursion
    else:
        forward(x)
        left(30)
        baum(7*x/10)    #Rekursiver Aufruf: Links wird ein kleinerer Binärbaum gezeichnet.
        right(90)    
        baum(x/2)    #Rekursiver Aufruf: Rechts wird ein kleinerer Binärbaum gezeichnet
        left(60)     #Die Turtle wird wieder an ihre Startposition manövriert.
        back(x)
    return

speed(1)             #Verringerung der Gesdchwindigkeit
left(90)             #Hier beginnt das Hauptprogramm. Zunächst wird dafür gesorgt, dass die Turtle nach oben zeigt.
baum(100)
hideturtle()         #Turtle verstecken --> schöneres Bild


