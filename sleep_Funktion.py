# lasse das Programm für eine gewisse Zeit (Sekunden) schlafen

from time import ctime, sleep

for i in range(3):
    print(ctime().split()[0])   #1 Zerteil den 24-Zeichen-String in einzelne Wörter und das vierte Wort ausgegeben

    sleep(2)    # lässt das Programm 2 Sekunden schlafen


#1  [0] Wochentag (Montag)
#1  [1] Monat (März)
#1  [2] Tag (26)
#1  [3] Uhrzeit (10:41:23)
#1  [4] Jahr

