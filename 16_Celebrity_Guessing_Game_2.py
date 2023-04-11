import random

celebrities = {
    "Prince": ["His name is royalty", "One of his songs is named after a cocktail", "He has a little red corvette"],
    "Elvis": ["He is also known as the King", "He has a quiff", "He sang Jailhouse Rock"],
    "Drake": ["His name rhymes with fake", "He started from the bottom", "He is on his worst behaviour"],
}

secret_celebrity = random.choice(list(celebrities))

guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    clue = celebrities[secret_celebrity][guess_count]
    print(clue)
    guess = input("Guess: ")
    guess_count += 1
    if guess.lower() == secret_celebrity.lower():
        print("You win!")
        break
else:
    print("You lose!")


