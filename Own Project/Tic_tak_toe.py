word = "python" #secret word
display = ["_"] * len(word)
chance = 6

print("Wellcome to Hungman")

# Game loop
while chance > 0:
    print("\nword:", " ".join(display))    # for current progress

    guess = input("Enter your letter: ").lower()

    # check word in letter form or word form
    if guess in word:
        for i in range(len(word)): # check word position

            if word[i] == guess:  # If word are same
                display[i] = guess

        print("Correct")

    else:
        chance -= 1
        print("Wrong!!")
        print("Chance left: ",chance)

        if "_" not in display:
            print("\nWord: ", " ".join(display))
            print("You Win !!")
            break
    if chance == 0:
        print("\nYou Lose!")
        print("The Word was: ",word)
