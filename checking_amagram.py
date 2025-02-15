a=input("Enter first string:")
b=input("Enter second string:")
r=list(a)
s=list(b)
def sort(a):
 for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            temp=a[j]
            a[j]=a[i]
            a[i]=temp
 return a
if sort(r)==sort(s):
    print("true")
else:
    print("false")