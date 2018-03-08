import time
stunde=time.localtime().tm_hour
print(stunde)

gruss="Guten Morgen" if stunde<12 else "Guten Tag"

print(gruss)
