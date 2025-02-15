n=int(input("Enter a number: "))
a=n ; sum=0
while a>0:
    sum=sum+(a%10)**2
    a=a//10
print(sum)
