words = ["Donkey","bad","ganda"]

with open("05-file.txt") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("05-file.txt", "w") as f:
    f.write(content)
