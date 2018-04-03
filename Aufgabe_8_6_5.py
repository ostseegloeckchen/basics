#Schreibe eine Funktion "haeufigkeiten()",
#welche zu jedem Zeichen eines übergebenen Strings
#die Häufigkeit ermittelt, mit der dieses Zeichen im String vorkommt.
#Zurückgegeben wird ein Dictionary,
#in welchem jedes Zeichen dessen Vorkommenshäufigkeit zugeordnet wird.

def haeufigkeiten(text):    #der Text muss in "" eingegeben werden
    d={}
    for key in text:
        d[key]=text.count(key)
    return d
    
