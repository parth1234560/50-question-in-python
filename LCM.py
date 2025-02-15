a= int(input("Enter the first number: "))
b= int(input("Enter the second number: "))
c=0
if a>b:
    c=a
else:
    c=b
for i in range(c,1000000):
     if i%a==0 and i%b==0:
        print(i)
        break