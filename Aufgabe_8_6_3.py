#Erstellen eines Englisch-Deutsch-Wörterbuches
vokabeln={"hat":["Hut"],"shirt":["Hemd","Bluse"],"sock":["Socke","Strumpf"]}

for key in vokabeln.keys():     #diese Schreibweise liefert Werte ohne [],
    print(key + ":", end=" ")   #ist also schöner als mit [], wie in #1
    for w in vokabeln[key]:
        print(w, end=" ")
    print()

print()

for key in vokabeln.keys():         #1 liefert Werte in[] = Liste, sieht nicht so schön aus
    print(key, ": ",vokabeln[key])

print()

vokabeln["cap"]=["Mütze"]
print(vokabeln["cap"])

vokabeln["cap"]=vokabeln["cap"]+["Kappe"]
print(vokabeln["cap"])
