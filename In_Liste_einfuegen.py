#In eine bestehende Liste ein neues Element einfügen
s=[1,2,3,4]
print(s)
s.insert(1,1.5) #vor dem Element mit dem Listenindex 1 wurde der das neue Element eingefügt
s.append(4.5)
print(s)

print()

#Ein Element aus der bestehenden Liste s entfernen
s.remove(1.5)
s.remove(4.5)
print(s)

print()

#Elemente eines Tupels anhängen aber nicht das Tupel selbst
s.extend((6,7))
print(s)

print(s)

#Das String "Ende" wird als Sequenz einzelner Buchstaben angehängt
s.extend("ende")
print(s)

print()

#mit append() wird das Wort "ende" als Element angehängt

s.append("ende")
print(s)
