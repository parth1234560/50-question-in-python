a=list(map(int,input("Enter array elemnets sepearted by (,) :-").split(",")))
sum=[0]*len(a)
for i in range(0,len(a)):
    for j in range(i,len(a)):
        if i!=j:
         if a[i]==a[j]:
            sum[i]=sum[i]+1

max=0
for i in range(0,len(a)):

    if int(sum[i])>max:
        max=i
print(a[max])