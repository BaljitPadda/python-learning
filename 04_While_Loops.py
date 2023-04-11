# While_loops: While loops are used to execute a block of code multiple times.

x = 1
while x <= 5:
    print(x)
    x += 1

Task: "Create a guessing game using the while loop."
"You can use 'else' in while loops as you do with 'if' statements."
"You can also use the break clause to stop a loop."

secret_number = 5
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You win!")
        break
else:
    print("You lose!")