n=int(input())
def perfect_number(i):
    sum=0
    for i in range(1,n):
        if(n%i==0):
            sum=sum+i
    if(sum==n):
        return True
    else:
        return False
if perfect_number(n):
   print("Perfect number",n)
   quit()
else:
 print("Not perfect number")
