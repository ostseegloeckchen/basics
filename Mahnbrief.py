# Definition einer Klasse "Mahnung" und automatische Produktion von Mahnbriefen
#
class Mahnung:
    basistext = """{anrede} {name},
dies soll keine Mahnung sein.
Ich möchte dich nur daran erinnern,
dass du deine Clubbeiträge für die Monate
{von} bis {bis} noch nicht bezahlt hast.
Bitte überweise sie umgehend auf das unten stehede Konto.

Mit freundlichen Grüßen,
Tim (Kassenwart)
"""
    def __init_(self, geschlecht, name, von, bis):
        if geschlecht == "m":
            anrede = "Lieber"
        else:
            anrede = "Liebe"

        self.text = self.basistext.format(anrede = anrede,
                                          name = name,
                                          von = von,
                                          bis = bis)
        print(self.text)
    def __str__(self):
        return self.text


# Hauptprogramm
personen = [("m", "Sven", "Januar", "Mai"),
            ("w", "Jenny","Februar", "Juli")]

for g, n, v, b in personen:
    print(Mahnung(g, n, v, b))

input("Beenden mit <ENTER>")
