low=int(input("Enter lower limit: "))
high=int(input("Enter upper limit: "))
sum=0
def prime_checker(n):
    if n==1:
        return True
    elif n==2:
        return True
    else:
        for i in range(3,n):
            if n%i==0:
                return False
    return True
for i in range(low,high+1):
    if i==1:
        continue
    elif i==2:
        sum=sum+i
    else:
        if prime_checker(i):
            sum=sum+i
print(sum)
