def baum(x):
    if x<5: return   #Abbruch der Rekursion
    else:
        forward(x)
        left(90)
        baum(x/2)    #Rekursiver Aufruf: Links wird ein kleinerer Binärbaum gezeichnet.
        right(180)    
        baum(x/2)    #Rekursiver Aufruf: Rechts wird ein kleinerer Binärbaum gezeichnet
        left(90)     
        back(x)     #Die Turtle wird wieder an ihre Startposition manövriert.
    return

speed(1)
left(90)             #Hier beginnt das Hauptprogramm. Zunächst wird dafür gesorgt, dass die Turtle nach oben zeigt.
baum(100)
hideturtle()         #Turtle verstecken --> schöneres Bild
