#Berechnung von Reisekosten per individuell eingegebenen Daten

print("Kosten für eine Reise")
print("---------------------")

#Eingabe
bus=float(input("Kosten für den Reisebus (€): "))
hotel=float(input("Hotelkosten pro Person (€): "))
events=float(input("Gesamtkosten für touristische Events (€): "))
teilnehmer=float(input("Anzahl der Teilnehmer: "))
print("")

#Verarbeitung
gesamtkosten=float(bus+hotel*teilnehmer+events)
gesamtkosten_teilnehmer=float(gesamtkosten/teilnehmer)

#Ausgabe
print("Die Gesamtkosten betragen",gesamtkosten,"€.")
print("Die Kosten pro Person betragen",gesamtkosten_teilnehmer,"€.")
      
      
            

      
