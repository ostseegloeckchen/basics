#Zerlegung eines Geldbetrages in Scheine und Münzen

geld=input("Geldbetrag in €: ")
geld=int(geld)

zwanziger=geld // 20
geld=geld % 20

zehner=geld//10
geld=geld%10

fuenfer=geld//5
geld=geld%5

zweier=geld//2
geld=geld%2

einer=geld//1
geld=geld%1

print("Der Betrag setzt sich wie folgt zusammen:")
print(zwanziger, "mal 20 €")
print(zehner, "mal 10 €")
print(fuenfer,"mal 5 €")
print(zweier,"mal 2 €")
print(einer,"mal 1 €")
      
