d={"E260":"Essigsäure","E200":"Sorbinsäure","E210":"Benzoesäure"} #Erstellt ein Dictionary

print(d)

print()

for k in d.keys():          #gibt alle Schlüsselwörter mit ihrem Wert aus (Schlüsselwort : Wert)
	print(k+": "+d[k])

print()

d["E239"]="Kaliumnitrit"    #fügt das Element mit dem Schlüsselwort und seinem Wert in das bestehende Dictionary ein
for k in d.keys():          #gibt alle Schlüsselwörter aus
    print(k)

print()

if "E260" in d:
    print(d["E260"])
