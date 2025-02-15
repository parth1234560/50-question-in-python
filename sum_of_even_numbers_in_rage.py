n=input("Enter maximum number: ")
sum=0
for i in range(int(n)+1):
    if i % 2 == 0:
     sum=sum+i
print(sum)