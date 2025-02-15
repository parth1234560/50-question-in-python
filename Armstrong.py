a=int(input("Enter lower limit: "))
b=int(input("Enter upper limit: "))
c=0
def arm(n):
    sum=0
    e=n
    while e>0:
        sum=sum+(e%10)**3
        e=e//10
    if sum==n:
        return True
    else:
        return False
arr=[]
for i in range(a,b+1):
    if(arm(i)):
        arr.append(i)

print("Armstrong numbers in the range",arr)