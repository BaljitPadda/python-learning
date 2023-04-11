import random

"""
Friday 4th February 2022.
Create a game of Guess Who. The player is given clues and has 3 attempts to guess correctly else they lose.
"""

celebrities = ["Simon Cowell", "Prince", "Jake Gyllenhall"]
clues = ["He wears v-necks", "He has pearly whites", "People think he had a fling with Sinitta",
         "His name is royalty", "One of his songs has the same name as a cocktail", "He has a little red corvette",
         "Tom's favourite actor", "He features in a lot of rom-coms", "He did a movie sat in one position"]

print("Welcome to Guess Who! You have 3 attempts to guess the celebrity.")

start = input("Ready to begin? ")
if start == "yes".lower():
    print("Let's go! Clue 1: " + random.choice(clues))
    input("First Guess: ")
elif start == "no".lower():
    print("In your own time.")
else:
    print("I didn't understand that.")

guess_limit = 3
current_guess = 1
while current_guess <= guess_limit:
    current_guess += 1
    guess = input("Guess the Celeb: ")
    if guess == celebrities in celebrities:
        print("you won!")
        break