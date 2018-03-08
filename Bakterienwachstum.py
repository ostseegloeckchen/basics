print("Ausgangsabundanz der Bakterienpopulation 100 Exemplare")
print("Verdopplung alle 30 min")


abundanz=100
stunde=0

while stunde<=48:
    stunde+=1
    abundanz=abundanz*4
    print("Stunde",stunde,abundanz,"Ind.")

abundanz1=100
for zeit in range(49):
    print("Stunde",zeit,"",abundanz1,"Ind.")
    abundanz1*=4
