import random

clues = ("He is a monkey man", "He is a very cute", "He likes fitness boxing", "He once did a skydive")

person = "tom"
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    print("Clue: " + random.choice(clues))
    guess = str(input("Guess: ")).lower()
    guess_count += 1
    if guess == person:
        print("You won!")
        break
    else:
        print("Wrong, try again!")
else:
    print("You lose!")