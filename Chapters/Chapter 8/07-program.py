def rem(l, word):
    for item in l:
        l.remove(word)
        return l
    
l = ["harry", "jahir", "rohan", "an"]

print(rem(l, "an"))