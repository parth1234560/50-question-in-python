n=list((input("Enter a number: ").split(",")))
sum=0
for i in range(0,len(n)):
    sum=sum+int(n[i])
print(sum/len(n))