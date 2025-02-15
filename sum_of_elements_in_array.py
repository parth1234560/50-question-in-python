arr=[]
a=int(input("no of elements: "))
sum=0
for i in range(a):
    b=int(input())
    arr.append(b)
    sum=b+sum
print(sum)