'''
for n = 3
*
***
*****
'''
n = int(input("Enter the Number of row: "))

for i in  range(1, n+1):
    print("*"*(2*i-1), end="")
    print("")