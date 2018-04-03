# Definition  einer Klasse für die Modellierung von Musicals
# (zum Import in andere Programme)

class Musical(object):
    def __init__(self, titel, eintrittspreis, saal):
        self.titel = titel
        self.eintrittspreis = eintrittspreis
        self.saal = saal
        self.vorstellungen = []     # Liste von Vorstellungen

    def getVorstellung(self, datum):
        """Rückgabe eines Vorstellungsobjektes mit
            passendem Datum, falls vohanden, sonst None"""
        for vorstellung in self.vorstellungen:
            if vorstellung.datum == datum:
                return vorstellung
            # Nach dem return bricht die Ausführung der Funktion ab

    def neueVorstellung(self, vorstellung):
        """Objekt "vorstellung" wird in Liste eingefügt"""
        self.vorstellung += [vorstellung]

    def __str__(self):
        beschreibung = "\n" + self.titel + "\n" + \
                       len(self.titel)*"=" + "\n"

        for vorstellung in self.vorstellungen:
            beschreibung += str(vorstellung) + "\n"

        return beschreibung

    def storniere(self, datum):
        """Storniert eine Vorstellung"""
        self.datum = str(datum)

        vorstellung = self.getVorstellung(datum)     
        if not vorstellung:
            return "Keine Vorstellung an diesem Tag"
        else:
            zuschauerliste = vorstellung.getZuschauer()
            text = "Liste aller Zuschauer der Vorstellung am "
            text += datum + "\n\n"

            for zuschauer in zuschauerliste:
                text += zuschauer.name + "" + zuschauer.tel + "\n"

            self.vorstellungen.remove(vorstellung)  #löschen
            return text


class Vorstellung(object):      # Warum muss hier nicht "(object)" angegeben werden?
    def __init__(self, datum, beginn, saal):
        self.datum = datum
        self.beginn = beginn
        self.saalbelegung = Saalbelegung(saal)
        self.saal = saal    # "self.saal" gibt es auch in der Klasse "Musical". Ist das identisch oder zwei verschiedene Attribute? Können sie sich in die Quere kommen?

    def __str__(self):
        beschreibung = self.datum + "\n" +\
        str(self.saalbelegung.getFreiePlaetze()) +\
        "freie Plätze \n"

        return beschreibung

    def getZuschauer(self):
        """liefert eine Liste mit den Zuschauern der Vorstellung"""
        liste=[]
        for reihe in self.saalbelegung.belegung:
            for platz in reihe:
                if platz.belegt():
                    liste +=[platz.zuschauer]
        return liste

class Saalbelegung(object): # Warum muss hier nicht "(object)" angegeben werden?
    """pflegt Liste von Listen mit Platz-Objekten"""
    def __init__(self, saal):
        self.belegung = []
        self.saal = saal    # "self.saal" gibt es auch in der Klasse "Musical". Ist das identisch oder zwei verschiedene Attribute? Können sie sich in die Quere kommen?

        for i in range(len(saal.plaetzeProReihe)):
            reihe = []

            for j in range(saal.plaetzeProReihe[i]):
                platz = Platz()
                reihe += [platz]

            self.belegung += [reihe]

    def buche(self, reihe, platz, zuschauer):
        """weist dem Platz "platz" in Reihe "reihe" einen Zuschauer zu"""
        if not self.belegung[reihe][platz].belegt():
            self.belegung[reihe][platz].belege(zuschauer)

            return "Platz gebucht"
        else:
            return "Platz schon gebucht"

    def getFreiePlaetze(self):
        """liefert Anzahl der freien Plätze"""
        frei = 0
        for reihe in self.belegung:
            for platz in reihe:
                if not platz.belegt():
                    frei += 1

        return frei

    def __str__(self):
        beschreibung = "Saalbelegung \n"
        beschreibung += " Platz: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 \n"
        nr = 1          # Reihennummer

        for reihe in self.belegung:
            beschreibung += "Reihe" + format(nr, "2d") + ":"

            for platz in reihe:
                beschreibung += str(platz)
            nr += 1

            beschreibung += "\n"

        return beschreibung

class Zuschauer(object):
    def __init__(self, name, tel):
        self.name, self.tel = name, tel

class Platz(object):
    def __init__(self):
        self.zuschauer = None

    def belegt(self):
        if self.zuschauer:
            return True
        else:
            return False

    def belege(self, zuschauer):
        self.zuschauer = zuschauer

    def __str__(self):
        if self.belegt():
            return self.zuschauer.name[:2] + "" # vom Zuschauernamen nur die ersten beiden Zeichen
        else:
            return "--" # freier Platz

class Saal(object):
    def __init__(self, liste):
        self.plaetzeProReihe = liste


    
