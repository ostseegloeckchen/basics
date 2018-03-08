print("Wenn Sie wissen möchten, ob ein Jahr ein Schaltjahr war oder ist,",
      "dann geben Sie bitte eine Jahreszahl ein.")
jahr=int(input("Jahreszahl: "))
if jahr%400==0:    #Die Zahl ist durch 400 ohne Rest teilbar
    print(jahr,"ist ein Schaltjahr")
elif jahr%4==0 and jahr%100!=0:  #Die Zahl ist durch 400 ohne Rest teilbar
    print(jahr,"ist ein Schaltjahr")
else:
    print(jahr,"ist kein Schaltjahr")
