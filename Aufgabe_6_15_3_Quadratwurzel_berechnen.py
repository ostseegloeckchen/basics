#rekursive Funktion um die Quadratwurzel einer Zahl
#nach dem Heronschen Verfahren zu berechnen

def wurzel(x,z=10):   #Wurzel aus x mit der voreingestellten Näherung z
    if z ==1:
        return 1
    else:
        return(0.5*(wurzel(x,z-1)+x/wurzel(x,z-1))) #rekursive Aufrufe "wurzel" aber mit z-1
              
   
    
