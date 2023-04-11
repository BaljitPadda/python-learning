import random

""" 
Sunday 30th January 2022
A package is a container for multiple modules. It is like a directory or a folder.
You can generate random values using the built-in 'random' module. This will give you a number between 0 and 1.
You can use '.randint' to generate a random whole integer in a range.
You can use 'random.choice()' to obtain a random selection from a list.

"""

members = ["Tom", "Ben", "Dave", "Jack"]
team_leader = random.randint(0, 3)
print(team_leader)
print(members[team_leader])

members = ["Baljit", "Joe", "Emily", "Tom"]
loser = (random.choice(members))
print(loser)


# Create and roll a dice
class Dice:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def roll(self):
        print(self.x, self.y)


dice_numbers = (1, 2, 3, 4, 5, 6)
x = random.choice(dice_numbers)
y = random.choice(dice_numbers)

Dice1 = Dice(x, y)
Dice1.roll()

# Thursday 3rd February 2022. Messing around using the built-in 'random' module.

words = ["clever", "stupid", "in-shape", "a fat whale"]
names = ["Baljit", "Tom", "Dave", "Jack"]
sentence = (f"{random.choice(names)} is {random.choice(words)}")
print(sentence)
