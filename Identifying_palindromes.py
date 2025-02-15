n=input("srting=")
len=len(n)
flag=0
for i in range(len):
    if(n[i]!=n[len-i-1]):
        flag =1;
        break;
if(flag==0):
    print("palindrome");
else:
    print("not palindrome");