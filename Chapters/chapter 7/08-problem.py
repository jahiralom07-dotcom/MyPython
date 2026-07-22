'''
for n = 3
*
**
***
'''
n = int(input("Enter the no of row: "))

for i in range(1, n+1):
    print("*"*i, end="")
    print("")