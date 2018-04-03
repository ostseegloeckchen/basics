# Definiere eine Klasse "Ding"
# schwach privates Klassenattribut "dichte" --> Dictionary (Elementsymbol : Tupel(Elementname, Dichte)
# privates Objekt-Attribut: "__masse"
# schwach privates Objekt-Attribut: "_symbol"
# Öffentliche Methoden:
#       getMasse()
#       getVolumen()
#       __str__()




class Ding(object):
    _dichte={"Fe":("Eisen",7.87),
             "Au":("Gold",19.32),
             "Ag":("Silber",10.5)}  #Klassenatribut: _dichte

    def __init__(self, symbol, volumen):
        self._symbol=symbol
        self.__volumen=float(volumen)
                           
    def getSymbol(self):
        return self._symbol
    
    def getDichte(self):
        for key, value in Ding._dichte.items() :
            if key==self._symbol:
                return (value[1])
        
    def getVolumen(self):
        return self.__volumen

    def getMasse(self):
        return self.__volumen*self._dichte[self._symbol][1] # "[self._symbol][1]" steht für das 2. Element in dem Tupel

    

    def __str__(self):
        beschreibung =  "Ein Ding aus " +\
                       self._dichte[self._symbol][0] +\
                       " mit einer Dichte von " +\
                       format(self.getDichte(), ".2f") + " g/ml" +\
                       " mit einem Volumen von " +\
                       format(self.getVolumen(), ".2f") + " ml" +\
                       " hat eine Masse von " +\
                       format(self.getMasse(), ".2f") + " g."
        return beschreibung


#Hauptprogramm

krone=Ding("Au", 200)

print(krone.getSymbol() +":")
print("Dichte: ", krone.getDichte())
print("Volumen: ", krone.getVolumen())
print("Masse: ", krone.getMasse())
print(krone)

print()

krone1=Ding("Ag", 100)

print(krone1.getSymbol() +":")
print("Dichte: ", krone1.getDichte())
print("Volumen: ", krone1.getVolumen())
print("Masse: ", krone1.getMasse())
print(krone1)


