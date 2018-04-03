# Analyse eines Textes: Vorkommen einer Bankleitzahl

from re import *

def blz_check(email):
    re = compile("(Bankleitzahl|BLZ):?\s*\d+", I)   #1 ein RE-Objekt mit dem Namen "re" wird erzeugt
    if re.search(email):
        return "Danke für die Konto-Angabe."
    else:                                           # wenn "search" nicht erfolgreich wird "else" durchlaufen
        return "Leider fehlt die Bankleitzahl!"


#Hauptprogramm

email1 = """Hallo, hier ist meine Kontonummer:
SSK Bonn Kto-Nr. 1234567. MfG T."""

email2 = """Hallo,
bitte überweisen Sie das Honorar auf folgendes Konto:
Sparkasse Witten BLZ 45250035, Kontonr. 1234567. Gruß M."""

print(blz_check(email1))
print(blz_check(email2))


#1 Der reguläre Ausdruck wird im ersten Argument übergeben
#1 mit dem zweiten Argument "I" wird festgelegt,
#1 dass nicht zwischen Groß- und Kleinschreibung unterschieden wird
