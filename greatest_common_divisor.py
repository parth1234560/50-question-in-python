a= int(input("Enter a number: "))
b= int(input("Enter b number: "))
c=0
if a>b:
    c=b
else:
    c=a
while c>0:
    if(a%c==0 and b%c==0):
        print(f"The GCD of {a} and {b} is {c}")
        break;
    c=c-1