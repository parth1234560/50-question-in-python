n=int(input("Enter a number: "))
p=int(input("Enter a digit to find in above number: "))
sum=0
while n>0:
    if n%10==p:
        sum=sum+1
    n=n//10
print(sum)
