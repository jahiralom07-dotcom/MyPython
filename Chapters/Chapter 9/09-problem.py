with open("08-this.txt") as f:
    content1 = f.read()
    
with open("08-this_copy.txt") as f:
    content2 = f.read()

if (content1 == content2):
    print("Yes these file are identical")

else:
    print("No these file are not identical")