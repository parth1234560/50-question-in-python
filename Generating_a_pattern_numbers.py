r=int(input("Enter a number: "))
n=1
for i in range(1,r+1):
    for j in range(i):
        print(n,end="")
        n=n+1
    print()
