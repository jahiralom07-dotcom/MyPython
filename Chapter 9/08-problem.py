with open("08-this_copy.txt") as f:
    content = f.read()

with open("08-this.txt", "w") as f:
    f.write(content)