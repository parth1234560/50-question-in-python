n=input("patter type(pyramid,diamond,rectangle,square)")
height=int(input("height"))
if n=="pyramid":
 for i in range(height-1):
    for j in range(i,height-1):
     print(" ",end="")
    for j in range(0,2*i+1):
     print("*",end="")
    print()
