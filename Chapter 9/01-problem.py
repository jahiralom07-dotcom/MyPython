f = open("01-poem.txt")
content = f.read()

if ("twinkle" in content):
    print("The word \"twinkle\" is present in the contenr")

else:
    print("The word \"twinkle\" is not present in the contenr")

f.close()