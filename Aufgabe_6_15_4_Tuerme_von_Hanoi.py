#Bewegung der Scheiben von den Türmen von Hanoi

def bewege(n,       #Anzahl der Scheiben des Turmes
           von,     #Anfangsposition des Turmes
           nach,    #Zielposition des Turmes
           ueber    #Zwischenposition, auf der während des Transportes Teile des Turmes abgelegt werden können
           ):
    if n ==1:
        print("Lege eine Scheibe von",von,"nach",nach,".")
    else:
        bewege(n-1,von,ueber,nach)
        bewege(1,von,nach,ueber)
        bewege(n-1,ueber,nach,von)
    
    
