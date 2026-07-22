def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>b and c>b):
        return c
    
a = int(input("Enter 1st number: "))
b = int(input("Enter 2st number: "))
c = int(input("Enter 3st number: "))

print(greatest(a, b, c))