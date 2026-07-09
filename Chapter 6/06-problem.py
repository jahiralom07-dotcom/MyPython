marks = int(input("Enter your mark: "))

if(100>=marks>=90):
    print("Grade:Ex")

elif(90>=marks>=80):
    print("Grade: A") 

elif(80>=marks>=70):
    print("Grade: B")

elif(70>=marks>=60):
    print("Grade: C")

elif(60>=marks>=50):
    print("Grade: D")

elif(50>=marks):
    print("Grade: F")

else: 
    print("Invalid marks! Please enter marks between 0 and 100.")