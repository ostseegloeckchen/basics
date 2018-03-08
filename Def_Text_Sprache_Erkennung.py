def deutsch (s):
    def h(text,buchstabe):
        text.upper()
        anzahl=text.count(buchstabe)
        relative_Haeufigkeit=float(anzahl)*100/len(text)
        return relative_Haeufigkeit

        #Ende def h

    if (4<h(s,"a")<9) and (14<h(s,"e")<20) and (h(s,"y")<1):
        return True
    else:
        return False

        #Ende def deutsch

text=input("Text: ")
if deutsch(text):
    print("Der Text ist vermutlich auf deutsch.")
else:
    print("Der Text ist vermutlich nicht auf deutsch.")
    
