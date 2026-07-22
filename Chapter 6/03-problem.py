p1 = "Make a lot of monay"
p2 = "buy now"
p3 = "subscribe this"
p4 = "Click this"

massage = input("Enter your comment: ")

if((p1 in massage) or (p2 in massage) or (p3 in massage) or (p4 in massage)):
    print("This comment is a spam")

else:
    print("This comment is not a spam")

print("Thank you !!")