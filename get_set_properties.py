#Einfügen von "get"- und "set"- Methoden für private Attribute
#Es ist anscheinend besser mit der "get"- und "set"-Funktion zu arbeiten

class Behaelter(object):
    def __init__(self, volumen):
        self.__volumen = float(volumen)    
    
    def setVolumen(self, neues_Volumen):
        self.__volumen=float(neues_Volumen)
    
    def getVolumen(self):
        return self.__volumen

     #volumen=property(setVolumen,getVolumen)


#Beispiel

becher=Behaelter(5)
print(becher.getVolumen())

becher.setVolumen(100)
print(becher.getVolumen())


