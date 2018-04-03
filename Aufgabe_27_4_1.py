# Modelliere eine Warteschlange von Autos beim TÜV
# Aufgaben: Eingabe des Autokennzeichens eines neuen Kunden
#           Anhängen des neuen Kfz-Kennz. an die bestehende Warteschlange
#           Ausgabe des Kfz-Kennz. des nächsten Autos
#           Entfernen dieses Kennz. anschließend
#           Programm beenden

from module_Queue import Queue

print("""Warten beim TÜV
---------------""")

warteschlange = Queue()     # Erzeugt ein Objekt "warteschlange" der Klasse "Queue"

warteschlange.__menuetext = """
(N)euer Kunde
(A)bfertigen des nächsten Kunden
(E)nde
"""

wahl = "x"
while not (wahl in "eE" and warteschlange.empty()):
    print(warteschlange.__menuetext)

    wahl = input("Auswahl: ")

    if wahl in ["n", "N"]:
        kennzeichen = input("Kennzeichen: ")
        warteschlange.enqueue(kennzeichen)

    elif wahl in ["a","A"]:
        if not warteschlange.empty():
            print("Der Nächste ist: ",
                  warteschlange.dequeue())
        else:
            print("Die Warteschlange ist leer")

    elif (wahl in "eE") and not warteschlange.empty():
        print("Es warten noch Kunden!")
        print("Kfz-Kennzeichen: ", warteschlange.front())
        

print("Ich wünsche einen schönen Feierabend!")

    
