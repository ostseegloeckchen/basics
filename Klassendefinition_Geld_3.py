#Definition einer eigenen Klasse, hier die Klasse "Geld"


class Geld_3(object):                               
    __wechselkurs ={"USD":0.85,                       
                    "GBP":1.39,
                    "EUR":1.0,
                    "JPY":0.0072}                   # Wechselkurs ist das Klassenattribut, als Dictionary

    def __init__(self, waehrung, betrag):           
        self.waehrung=waehrung
        self.betrag=float(betrag)
        
    def get_Euro(self):                             
        return self.betrag*self.__wechselkurs[self.waehrung]

    def __add__(self, geld):                        # hier wurden vor und nach dem Wort "add" je 2 Unterstriche geschrieben um den "+"-Operator zu überladen
        a=self.get_Euro()
        b=geld.get_Euro()
        faktor=1.0/self.__wechselkurs[self.waehrung]
        summe=Geld_3(self.waehrung,(a+b)*faktor)    # Hier wird ein neues Objekt der Klasse Geld generiert und in der Funktion

        return summe                                # "return" zurück gegeben

    def __lt__(self, other):                        # Überladen des Kleiner als Operators (<)
        a=self.get_Euro()
        b=other.get_Euro()

        return a<b                                  # gibt Wahrheitswerte zurück

    def __le__(self, other):                        # Überladen des Kleiner-gleich als Operators (<=)
        a=self.get_Euro()
        b=other.get_Euro()

        return a<=b                                 # gibt Wahrheitswerte zurück

    def __eq__(self, other):                        # Überladen des Gleichheitsoperators (==)
        a=self.get_Euro()
        b=self.get_Euro()

        return a==b                                 # gibt Wahrheitswerte zurück

    def __str__(self):                              # formatiert die Werte der Objekte in ein String um

        return self.waehrung + " " + format(self.betrag, ".2f")


    
#Beispiele
hotelkosten=Geld_3("USD",120.00)
mietwagen=Geld_3("EUR",100.00)

print()

# hier werden die Hotelkosten zu den Kosten des Mietwagens addiert (--> Rechnung in EUR)
print(mietwagen+hotelkosten)

print()

if mietwagen > hotelkosten:
    print("Der Mietwagen ist teurer")
else:
    print("Der Mietwagen ist nicht teurer")
