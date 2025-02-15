n=int(input("number:"))
a=n-1
for i in range(n):
    if(a!=0):
     n=a*n
     a=a-1
print(n)