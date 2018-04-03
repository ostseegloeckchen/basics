#Definition einer eigenen Klasse, hier die Klasse "Geld"


class Geld_1(object):                               #1 Kopf = Klassenname (Substantiv, singular, Großbuchstabe am Anfang)
    __wechselkurs ={"USD":0.85,                       #1a hier wurden 2 Unterstriche vor "wechselkurs" geschrieben, Wechselkurs (1USD = ...EUR)
                  "GBP":1.39,
                  "EUR":1.0,
                  "JPY":0.0072}                    #2 Wechselkurs ist das Klassenattribut, als Dictionary

    def __init__(self, waehrung, betrag):           #3 Konstruktormethode, mit jeweils zwei Unterstrichen vor und nach dem "init", darf keine "return"-Anweisung enthalten
        self.waehrung=waehrung
        self.betrag=float(betrag)
        
    def get_Euro(self):                             #4 siehe Buch Python 3, S. 285
        return self.betrag*self.wechselkurs[self.waehrung]

    def add(self, geld):                            #5 siehe Buch Python 3, S. 285
        summe_in_Euro=self.get_Euro()+geld.get_Euro()       #6 "geld" ist hier ein Objekt und wird daher klein geschrieben 
        summe=Geld_1(self.waehrung,
                   summe_in_Euro/self.wechselkurs[self.waehrung])

        return summe


#3 Die Methode _init_() bewirkt, dass ein neues Objekt nach dem Bauplan der Klasse "Geld" generiert wird
#3 = Konstruktormethode.
#3 Das Parameter "self" darf bei keiner Methodendefinition fehlen.
#3 Es ist eine Hauptaufgabe der Konstruktormethode die Objektattribute mit Anfangswerte zu belegen. 

#4 Beim Zugriff auf Attribute der Instanz wird zuerst der Instanzname "self",
#4 dann ein Punkt und dann der Name des Attributs aufgeschrieben.


    
#Beispiele
banknote=Geld_1("USD",100)
print(banknote.betrag,banknote.waehrung)

print()

hotelrechnung=Geld_1("USD",123.45)
mietwagen=Geld_1("EUR",527.30)

print()
summe=hotelrechnung.add(mietwagen) 
# hier werden die Kosten des Mietwagens zur Hotelrechnung addiert (--> Rechnung in USD)
print(summe.waehrung, round(summe.betrag,2))

summe=mietwagen.add(hotelrechnung)
# hier wird die Hotelrechnung zu den Kosten des Mietwages addiert (--> Rechnung in EUR)
print(summe.waehrung, round(summe.betrag,2))
