n=int(input("Enter number of inputs in list"))
list=[]
for i in range(n):
    a=int(input("Enter number in list"))
    list.append(a)
for i in range(n):
    for j in range(i+1,n):
        if(list[i]>list[j]):
            temp=list[i]
            list[i]=list[j]
            list[j]=temp
print(list[n//2])

