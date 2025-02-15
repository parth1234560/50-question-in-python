n=int(input("Enter a number: "))

def sum_of_digits(n):
 sum=0
 a=n
 while a>0:
    sum=sum+a%10
    a=a//10
 return sum
num=sum_of_digits(n)
while num>10:
    num= sum_of_digits(num)
print(num)