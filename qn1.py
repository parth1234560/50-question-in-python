from django.template.defaultfilters import divisibleby

n=int(input("Enter a number:"))
if n>=0:
 if(n%2==0):
    print(f"{n} is even")
 else:
    print(f"{n} is odd")
else:
    printf("invalid input")