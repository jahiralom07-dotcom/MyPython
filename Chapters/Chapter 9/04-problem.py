word = "Donkey"

with open("04-file.txt") as f:
    content = f.read()

contentNew = content.replace(word, "Don##y")

with open("04-file.txt", "w") as f:
    f.write(contentNew)
