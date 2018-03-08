#Schreiben Sie eine Funktion mit zwei Argumenten s und n,
#die einen Klartext s auf folgende Weise durch Steganografie
#unleserlich macht
#Der String s wird in Großbuchstaben umgewandelt
#Hinter jedes Zeichen werden n zufällige Großbuchstaben eingefügt
#Das Argument n ist optional (Default=1)

def zufallsbuchstabe():
    buchstaben="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    import random
    return buchstaben[random.randint (0,25)]  #der Aufruf liefert eine ganze Zufallszahl zwischen n und m

def verstecke(s,n=1):      
    text_Gross=s.upper()    #Umwandlung des Textes in Großbuchstaben
    versteckt=""
    for c in text_Gross:
        versteckt+=c
        for i in range(n):  #Hängt große Zufallsbuchstaben an alle Buchstaben in s an.
            versteckt+=zufallsbuchstabe()
    return versteckt
