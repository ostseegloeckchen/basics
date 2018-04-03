# Ableitung von der Standardklasse "list"

class Default_list (list):
    def __init__(self, s=[], default=0):            #1"s" und "default" sind obtionale Attribute
        self.default=default
        list.__init__(self,s)                       #2 Aufruf der Methode "__init__()" der Basisklasse "list"                      

    def __getitem__(self, index):
        try:
            return list.__getitem__(self, index)    #3 mit der Methode "__getitem__" wird versucht auf einen bestimmten Index der Liste zu zugreifen
        except IndexError:
            return self.default                     #4 wenn Zugriff misslingt, wird Defaultwert zurück gegeben

    def __add__(self,other):                        #5 Zusätzlich eingefügte Definition
        result=list.__add__(self, other)
        return Default_list(result, self.default)

#Beispiel
p=["Merkur","Venus","Erde"]
planeten=Default_list(p,"unbekannter Planet")   # "p" ist der Listenname und "unbekannter Planet" ist der Defaultwert

print(planeten)
print(planeten[2])
print(planeten[3])                                  # wird den Defaultwert "unbekannter Planet" zurück geben, da der Listenplatz 3 nicht belegt ist.


#Test der Basisklasse
planeten.append("Mars")
print(planeten) 

# Problem, wenn zwei Objekte der Klasse Default_list konkateniert werden sollen,
# wenn Definition von __add__() in der Klasse Default_list fehlt

mehr_Planeten=Default_list(["Jupiter", "Saturn"], "unbekannter Planet")
planeten=planeten + mehr_Planeten
print(planeten)
print(planeten[10])

