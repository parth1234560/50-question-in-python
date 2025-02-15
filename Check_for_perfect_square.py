from math import sqrt
n=int(input("Enter a number: "))
def check_perfect_square(n):
    Sqrt=int(sqrt(n))
    return Sqrt**2 == n
if check_perfect_square(n):
    print("Yes")
else:
    print("No")
