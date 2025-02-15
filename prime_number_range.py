def primechecker(n):
    if n==1:
        return False
    if n==2:
        return True
    for i in range(2,n):
        if n % i == 0:
            return False
        else:
            return True
m=int(input("enter the Lower Limit"))
k=int(input("enter the Upper Limit"))
for i in range(m,k+1):
    if primechecker(i):
        print(i)

