n=int(input("Enter a number:"))
a=n
sum=0
while a>0:
  b=a%10
  sum=sum+b
  a=a//10
print(sum)