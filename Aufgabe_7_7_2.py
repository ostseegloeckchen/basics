A=[1,2,3,4]
B=[2,3,4,5]
s=[i for i in A+B if(i not in A) or (i not in B)]
print(s)
