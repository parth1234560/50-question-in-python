arr=[]
n=int(input("no of elements in array"))
max=0;
for i in range(n):
    a=int(input())
    arr.append(a)

for i in range(n):
    for j in range(i+1,n):
        if arr[i]>arr[j]:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp

print("sorted array:-")
for i in range(n):
    print(arr[i],end=",")
