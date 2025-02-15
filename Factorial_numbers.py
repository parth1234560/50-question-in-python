n=int(input())
for i in range(1,n):
    n=n*i
sum=0
while n>0:
    sum=sum+n%10
    n=n//10
print(sum)