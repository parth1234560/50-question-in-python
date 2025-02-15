n=input("Enter string")
vowels=['a','e','i','o','u']
v=0
consonants=['b','c','d','f','g','h','i','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
c=0
for i in n:
 if i in vowels:
    v=v+1
 else:
    c=c+1
print(f'Vowels: {v}, Consonants: {c}')