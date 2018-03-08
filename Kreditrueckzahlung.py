#Berechnung der Rückzahlungssummen eines Kredites

print("Kreditberechnung")

schulden=float(input("Kreditsumme: "))
zinssatz=float(input("Zinssatz(Prozent pro Jahr): "))
zahlung=float(input("Jährliche Rückzahlung in €: "))

import time
jahr=time.localtime()[0] #gibt aktuelles Jahr aus

while schulden>zahlung:
      zinsen=schulden*zinssatz/100
      tilgung=zahlung-zinsen
      schulden=schulden-tilgung
      jahr+=1

      
      print(jahr,"Zinsen:",round(zinsen),"€","Tilgung",round(tilgung),"€",
            "Restschulden:",round(schulden),"€")
print("Restforderung:",round(schulden,2),"€")
