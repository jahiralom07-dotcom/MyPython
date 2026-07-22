import random
'''
1 for snake
-1 for water 
0 for gun

'''

computer = random.choice([-1,0,1])
youstr = input("Enter your choice: ")

youDict = {"s" : 1, "w" : -1, "g" : 0}
you = youDict[youstr]
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# By now we have 2 numbers (variables), You and Computer

print(f"You Chose {reverseDict[you]}\nComputer Chose {reverseDict[computer]}")
if(computer == you):
    print(" It's a draw !!")

else:    
    if(computer == -1 and you == 1):
        print("You Win !!")

    elif(computer == -1 and you == 0):
        print("You Lose !!")

    elif(computer == 1 and you == -1):
        print("You Lose !!")

    elif(computer == 1 and you == 0):
        print("You Win !!")

    elif(computer == 0 and you == -1):
        print("You Win !!") 

    elif(computer == -1 and you == 0):
        print("You Lose !!")

    else:
        print("Somthing Went Wrong !!")

