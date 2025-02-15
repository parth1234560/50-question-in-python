def prime_checker(number):
    if number <= 1:
        return False
    elif number==2:
        return True
    else:
        for i in range (3,number):
            if number % i == 0:
                return False

        return True
a=int(input("Enter a number: "))
for i in range(2,a):
    if prime_checker(i):
        print(i)