#try and except Anweisung in Kurzform

try:
    zahl=int(input("Bitte geben Sie eine Zahl ein: "))
    print("Danke fü die Zahl.")
except:
    print("Eingabe nicht in Ordnung.")
    

#try and except Anweisung in einer Langform

while True:
    try:
        zahl=int(input("Bitte geben Sie eine ganze Zahl ein: "))
        print("Danke für die Zahl.")
        break
    except ValueError:
        print("Ihre Eingabe kann ich nicht in eine ganze Zahl umwandeln.")
    except:
        print("Eingabe nicht in Ordnung.")
    
