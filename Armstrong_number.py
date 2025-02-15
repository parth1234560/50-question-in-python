import array as arr
n=int(input("Enter a number: "))
a=arr.array('i',[n])
def isArmstrong(n):
    original_n=n
    while n > 0:
        i=0
        a.insert(i,n % 10)
        n=n//10
        i=i+1
    num=0
    for digit in a:
      num+=digit**3

    if num==original_n:
      print("YES")
    else:
       print("NO")
isArmstrong(n)