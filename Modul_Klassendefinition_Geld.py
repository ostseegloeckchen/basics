# Definition einer eigenen Klasse, hier die Klasse "Geld" (kopiert aus Geld_3 (14.3.2018))

# Dokumentationsstil:
"""
Klassen zur Modellierung von Geld

Geld -- modelliert Geld-Objekte mit Betrag und Währung
"""

class Geld(object):                               
    __wechselkurs ={"USD":0.85,                       
                    "GBP":1.39,
                    "EUR":1.0,
                    "JPY":0.0072}       

    def __init__(self, waehrung, betrag):           
        self.waehrung=waehrung
        self.betrag=float(betrag)
        
    def get_Euro(self):                             
        return self.betrag*self.__wechselkurs[self.waehrung]

    def __add__(self, geld):
        a=self.get_Euro()
        b=geld.get_Euro()
        faktor=1.0/self.__wechselkurs[self.waehrung]
        summe=Geld(self.waehrung,(a+b)*faktor)    

        return summe                                

    def __lt__(self, other):                        
        a=self.get_Euro()
        b=other.get_Euro()

        return a<b                                  

    def __le__(self, other):                        
        a=self.get_Euro()
        b=other.get_Euro()

        return a<=b                                 

    def __eq__(self, other):                        
        a=self.get_Euro()
        b=self.get_Euro()

        return a==b                                 

    def __str__(self):                              

        return self.waehrung + " " + format(self.betrag, ".2f")

# Hauptprogramm
if __name__=="__main__":        #1 
    eur100=Geld("EUR", 100)
    usd100=Geld("USD", 100)

    print("100 Euro: ", eur100)
    print("100 Euro + 100 USD: ", eur100 + usd100)
    print("100 Euro > 100 USD: ", eur100>usd100)
    print("100 USD in Euro: ", usd100.get_Euro())
    
#1 Die "if"-Anweisung wird genutzt um das Modul zu testen,
#1 wenn es importiert werden soll, dann soll die Testergebnisse nicht mit ausgegeben werden
#1 Die Variable "__name__" enthält den Namen des Moduls,
#1      zum Testen: "__main__", und
#1      zum Importieren: "Geld" bzw. den Dateinamen ohne Extension ".dy", hier: "Modul_Klassendefinition_Geld"
