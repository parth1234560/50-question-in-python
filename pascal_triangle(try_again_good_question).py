from math import factorial
n=int(input("enter no of rows: "))
def Pascal(n):
    for i in range(0,n):
        for k in range(0,(n-i+1)):
            print(" ",end="")
        for j in range(0,i+1):
            sum =factorial(i)//(factorial(i-j)*factorial(j))
            print(sum,end=" ")
        print()
Pascal(n)