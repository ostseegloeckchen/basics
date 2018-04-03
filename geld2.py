#Definition einer eigenen Klasse, hier die Klasse "Geld_2" mit privaten Attributen

class Geld_2(object):
    __wechselkurs={"USD":0.85,
                   "GBP":1.39,
                   "EUR":1.0,
                   "JPY":0.0072}
    def __init__(self, waehrung, betrag):
        self.__waehrung=waehrung
        self.__betrag=float(betrag)

    def get_Betrag(self):                                #get-Funktion (Lesen), wegen privatem Attribut
        return self.__betrag

    def get_Waehrung(self):                             # get-Funktion (Lesen), wegen privatem Attribut
        return self.__waehrung

    def get_Euro(self):                         
        return self.__betrag*\
               self.__wechselkurs[self.__waehrung]

    def set_Betrag(self,neuer_Betrag):                  # set-Funktion (Schreiben), wegen privatem Attribut
        self.__betrag = float(neuer_Betrag)

    def set_Waehrung(self, neue_Waehrung):              # set-Funktion (Schreiben), wegen privatem Attribut
        if neue_Waehrung in self.__wechselkurs.keys():
            alt = self.__wechselkurs[self.__waehrung]
            neu = self.__wechselkurs[neue_Waehrung]
            self.__betrag = alt/neu * self.__betrag
            self.__waehrung = neue_Waehrung

    def add(self, geld):                         
        summe_in_Euro=self.get_Euro()+geld.get_Euro()        
        summe=Geld_2(self.__waehrung,
                   summe_in_Euro/self.__wechselkurs[self.__waehrung])

        return summe

#Hauptprogramm
##preis=Geld_2("USD",1000)
##preis.set_Waehrung("EUR")
##print(preis.get_Betrag(),preis.get_Waehrung())




