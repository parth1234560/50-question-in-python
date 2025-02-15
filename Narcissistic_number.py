n=int(input("enter the number"))
sum=0
a=n
while n>0:
    sum=sum+(n%10)**3
    n=n//10
if sum==a:
    print("Narcissistic number")
else:
    print("Not Narcissistic number")
