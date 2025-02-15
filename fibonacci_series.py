n=int(input("Enter a number: "))
a=1
b=1
print("[",end="")
print(a)
print(b)
for i in range(1,n+1):
    print(a+b)
    b=a+b
    a=b-a
