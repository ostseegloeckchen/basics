wort=input("Wort: ")
anzahl=0
for c in wort:
    if c in 'aeiouAEIOU':
        continue
    anzahl=anzahl+1
print("Das Wort",wort,"enthält",anzahl,"Konsonanten.")
