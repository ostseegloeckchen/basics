# Abfrage ob Programm beendet werden soll

import sys

antwort = input("Programm beenden? (j/n)")
if antwort=="j":
    sys.exit(0)

else:
    print("Programm läuft weiter")
