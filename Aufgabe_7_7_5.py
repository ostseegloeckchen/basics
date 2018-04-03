# Berechnen der Anzahl an Tanzpaar-Möglichkeiten

damen=set("ABCD")
herren=set("abcd")
tanzlehrer=set("x")
tanzpaare=set(frozenset((d,h))
              for d in damen|tanzlehrer
              for h in herren|tanzlehrer
            if d !=h)
for p in tanzpaare:
    print(tuple(p))
