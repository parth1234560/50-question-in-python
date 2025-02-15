n=int(input("Enter a number: "))
def isPrime(n):
    if(n==1):
        return False
    if (n==2):
        return True
    else:
        for i in range(2,n):
            if(n%i==0):
                return False
    return True
sum=0
for i in range(2,n):
    if(isPrime(i) and n%i==0):
        sum=sum+i
print(sum)