def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)
    return "done"

num = int(input("Enter the number of row: "))
print(f"{pattern(num)}")