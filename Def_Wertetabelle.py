def wertetabelle (anzahl=10,   #Anzahl der Funktionswerte
                  schritt=0.5  #Anstand zwischen zwei Zahlen
                  ):
    x=0.0
    print('Wertetabelle')
    for i in range(anzahl):
        print(x,' ',x*x)
        x +=schritt
        
