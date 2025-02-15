n=int(input("year"))
if n%4==0 and n%100!=0:
    print("leap year")
elif n%100==0 and n%400==0:
    print("leap year")
else:
    print("not leap year")