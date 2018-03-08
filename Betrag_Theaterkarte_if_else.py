#Mehrfache Fallunterscheidungen (lange Fassung)
kategorie=input("Platzkategorie (Loge, Parkett, Vorparkett, Rang): ")
if kategorie=="Loge":
    preis=50
else:
    if kategorie=="Parkett":
        preis=37
    else:
        if kategorie=="Vorparkett":
            preis=29
        else:
            preis=20

print("\nDie Theaterkarte kostet",preis,"€.")


#Mehrfache Fallunterscheidungen (kurze Fassung mit elif)
kategorie1=input("Platzkategorie (Loge, Parkett, Vorparkett, Rang): ")
if kategorie=="Loge":
    preis1=50
elif kategorie=="Parkett":    #elif ist die Kurzfassung von else: if
    preis1=37
elif kategorie=="Vorparkett":
    preis1=29
else:
    preis1=20

print("\nDie Theaterkarte kostet",preis1,"€")


