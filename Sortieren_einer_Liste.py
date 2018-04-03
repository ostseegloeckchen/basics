#Sortieren einer Liste nach dem "divide and conquere"-Prinzip

def quicksort(s):
    if len(s)>0:
        print("Ich sortiere: ",s)       #1
    if len(s)<=1:
        return s                        #2
    else:
        return quicksort([x for x in s[1:] if x<s[0]])\
               +[s[0]]\
               +quicksort([y for y in s[1:] if y>=s[0]])    #3




#1 Die ursprüngliche Liste wird ausgegeben
#2 Wenn die Liste nur aus einem Element besteht ist sie sortiert und wird ausgegeben
#3 Die logische Zeile wird mithilfe des Verbindungsoperators "\" auf drei physikalische Zeilen aufgeteilt
#3 Es entsteht eine Konkatenation von drei Teillisten
#3 <s[0]
#3 ==s[0]
#3 >s[0]
    




