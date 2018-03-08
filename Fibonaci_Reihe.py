#Fibonacci-Folge
a1=1
a2=1

print("Die ersten 20 Zahlen der Fibonacci-Folge sind:")
print(a1,a2,end=" ")
for i in range (18):
    a=a1+a2
    print(a,end=" ")
    a1, a2=a2, a
