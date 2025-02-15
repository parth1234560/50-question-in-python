n=int(input("Enter a number[1-infinity]: "))
if(n<=0):
 print("Entered number is less than 0")
 quit()

if(n==1):

 print("the number is not prime")
 quit()
if(n==2):
 print("prime");
 quit()
for i in range(2,n):
    if(n%i==0):
     print("not prime")
     quit()
print("prime")
